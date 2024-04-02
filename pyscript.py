from pyweb import pydom
from pyodide.http import open_url
from pyscript import display
from js import console


def showSpin(event):
    pydom['#spinnerdiv'].style['display'] = 'flex'
    return