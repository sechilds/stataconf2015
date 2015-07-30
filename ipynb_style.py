
import IPython.core.display
import matplotlib as mpl

def clean():
    # set mpl defaults for nice display
    mpl.rcParams['font.size'] = 12
    mpl.rcParams['figure.figsize'] = (18, 6)
    mpl.rcParams['lines.linewidth'] = 1

    return IPython.core.display.HTML("""
<style type="text/css">
div.input {
width: 105ex; /* about 80 chars + buffer */
}

div.text_cell {
width: 105ex /* instead of 100%, */
}

div.text_cell_render {
/*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
font-family: "Charis SIL", serif; /* Make non-code text serif. */
line-height: 145%; /* added for some line spacing of text. */
width: 105ex; /* instead of 'inherit' for shorter lines */
}

/* Set the size of the headers */
div.text_cell_render h1 {
font-size: 18pt;
}

div.text_cell_render h2 {
font-size: 14pt;
}

.CodeMirror {
 font-family: Consolas, monospace;
 }

.rendered_html ol {list-style:decimal; margin: 1em 2em;}

</style>
<style>table.dataframe {
border-collapse: collapse;
border: none;
font-size:100%;
}</style>

<style>table.dataframe tr {
border: none;
}
table.dataframe td, table.dataframe th {
margin: 0;
border: 1px solid white;
padding-left: 0.25em;
padding-right: 0.25em;
}
table.dataframe th:not(:empty) {
background-color: #fec;
text-align: left;
font-weight: normal;
}
table.dataframe tr:nth-child(2) th:empty {
border-left: none;
border-right: 1px dashed #888;
}
table.dataframe td {
border: 2px solid #ccf;
background-color: #f4f4ff;
}</style>
""")


def presentation():
    # set mpl defaults for nice display
    mpl.rcParams['font.size'] = 15
    mpl.rcParams['figure.figsize'] = (12, 6)
    mpl.rcParams['lines.linewidth'] = 3

    return IPython.core.display.HTML("""
<style type="text/css">
div.input {
width: 1024px; /* about 80 chars + buffer */
}

div.text_cell {
width: 1024px /* instead of 100%, */
}

div.text_cell_render {
/*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
font-family: "Charis SIL", serif; /* Make non-code text serif. */
line-height: 145%; /* added for some line spacing of text. */
font-size: 28pt;
}

/* Set the size of the headers */
div.text_cell_render h1 {
font-size: 36pt;
}

div.text_cell_render h2 {
font-size: 32pt;
}

div.text_cell_render li {
line-height: 1.2em;
}

div.text_cell_render p {
font-size: 14pt;
line-height: 1em;
}

.CodeMirror {
font-size: 14pt;
 font-family: Consolas, monospace;
 }

.CodeMirror-lines {
font-size: 120%;
font-family: Consolas monospace;
}

.output_area {
font-size: 120%;
font-family: Consolas;
}

.rendered_html ol {list-style:decimal; margin: 1em 2em;}

</style>
""")

def pres2():
    # set mpl defaults for nice display
    mpl.rcParams['font.size'] = 15
    mpl.rcParams['figure.figsize'] = (12, 6)
    mpl.rcParams['lines.linewidth'] = 3

    return IPython.core.display.HTML("""
<style>.rendered_html {
font-size: 200%;
line-height: 1.3;
}</style>

<style>.rendered_html li {
line-height: 2.3;
}</style>

<style>.rendered_html h1{
margin: 0.5em 0;
line-height: 1.3;
}</style>

<style>.rendered_html h2{
margin: 0.15em 0;
line-height: 1.2;
}</style>

<style>.input_prompt {
font-size: 140%;
font-family: Consolas;
}</style>

<style>.CodeMirror-lines {
font-size: 140%;
font-family: Consolas;
}</style>

<style>.output_area {
font-size: 140%;
font-family: Consolas;
}</style>

<style>table.dataframe {
border-collapse: collapse;
border: none;
font-size:65%;
}</style>

<style>table.dataframe tr {
border: none;
}
table.dataframe td, table.dataframe th {
margin: 0;
border: 1px solid white;
padding-left: 0.25em;
padding-right: 0.25em;
}
table.dataframe th:not(:empty) {
background-color: #fec;
text-align: left;
font-weight: normal;
}
table.dataframe tr:nth-child(2) th:empty {
border-left: none;
border-right: 1px dashed #888;
}
table.dataframe td {
border: 2px solid #ccf;
background-color: #f4f4ff;
}</style>
""")
