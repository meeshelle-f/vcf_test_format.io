
import asyncio
import panel as pn
import pandas as pd
from panel.io.pyodide import show
from js import document, FileReader
from pyodide import create_proxy

fileInput = pn.widgets.FileInput(accept='.csv')
uploadButton = pn.widgets.Button(name='Upload', button_type = 'primary')

table = pn.widgets.Tabulator(pagination='remote', page_size=10)

document.getElementById('table').style.display = 'none'

def process_file(event):
    if fileInput.value is not None:
        table.value = pd.read_csv(io.BytesIO(fileInput.value))
        document.getElementById('table').style.display = 'block'

uploadButton.on_click(process_file)



