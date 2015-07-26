import sys
import subprocess as sp
from threading import Thread
from queue import Queue, Empty

class Stpy:
    """A running instance of Stata as a subprocess.

    An instance of this class can be used to run Stata commands.
    The instance holds a persistence Stata process, so the memory
    is preserved between commands.

    """
    def __init__(self):
        """Constructor method for the stpy class.

        This starts Stata running on a separate thread, where it waits
        until commands are sent to it via the `write` method.

        """
        # Open stata as pipe; make a queue for non-blocking. Start the thread.
        self.proc = sp.Popen(['stata-mp'], stdin=sp.PIPE, stdout=sp.PIPE, bufsize=1)

        self.qu = Queue()

        self.thread = Thread(target = self.enqueue_output, args = (self.proc.stdout,
            self.qu))
        self.thread.daemon = True
        self.thread.start()

        # Read the initial stdout content.
        self.genout()

    def enqueue_output(self, out, queue):
        while True:
            # Read 1 byte at a time in thread.
            self.thread = out.read(1).decode()
            queue.put(self.thread)
        out.close()

    def buffer_output(self, sbuf=[]):
        # Try to read byte.
        try:  char = self.qu.get(timeout=1)
        except Empty:
            # Catch 2 x newline, followed by ". ". Stata's done with the output.
            if ''.join(sbuf) == "\n\n. ":
                return False # Done, Stata passes control back to user.
            # Pass if we are not done.
            else:
                pass # Waiting...
        else:
            # Keep a small internal rotating buffer which can catch the '\n\n. '
            # instruction.
            if len(sbuf) >= 4:
                del sbuf[0]
            sbuf.append(char)
            return(char)

    def genout(self):
        """Read the content of stdout."""
        ch = self.buffer_output()
        while ch:
            print(ch, end='')
            ch = self.buffer_output()

    def write(self, command):
        """Pass a stata command to the running Stata instance.

        Call this method with a string that you wish to pass to Stata.
        The method adds a newline to the end, then passes it to Stata.
        The output from Stata is returned via the standard output.
        """
        # Write command in bytes plus newline then flush.
        self.proc.stdin.write(bytes(command + "\n", 'ascii'))
        self.proc.stdin.flush()

        self.genout()
