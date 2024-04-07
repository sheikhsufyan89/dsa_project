from pyweb import pydom
from pyodide.http import open_url
from pyscript import display
from js import console


def csv_to_html_table(fname,headers=None,delimiter=","):
    with open ("student_records.csv") as f :
        content = f.readlines()
    #reading file content into list
    rows = [x.strip() for x in content]
    table = "<table>"
    #creating HTML header row if header is provided 
    if headers is not None:
        table+= "".join(["<th>"+cell+"</th>" for cell in headers.split(delimiter)])
    else:
        table+= "".join(["<th>"+cell+"</th>" for cell in rows[0].split(delimiter)])
        rows=rows[1:]
    #Converting csv to html row by row
    for row in rows:
        table+= "<tr>" + "".join(["<td>"+cell+"</td>" for cell in row.split(delimiter)]) + "</tr>" + "\n"
    table+="</table><br>"
    return table

def login(event):
    print( pydom['#StuPage'].html)
    t = csv_to_html_table("student_records.csv",headers=None,delimiter=",")
    pydom['#StuPage'].html = t
    pydom['#StuPage'].style['display'] = 'flex'
    pydom['.login-container'].style['display'] = 'none'
    return
