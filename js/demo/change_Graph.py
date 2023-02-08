import pandas as pd 
import ftplib
from pyodide import create_proxy, to_js
from js import chartasm
from pyodide import create_proxy



ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)

ftp_server.encoding = "utf-8"

filename = "public_html//reports//abba//data//ReportGraphC.csv"

file = "ReportGraphC.csv"

    # Command for Downloading the file "RETR filename"
ftp_server.retrbinary(f"RETR {filename}", open(file, "wb").write)

file= open(file, "r")

DF_REPGRH = pd.DataFrame(data=file)

ARRAY_REPGRH = pd.array(DF_REPGRH[0][1:5])

ARRAY_GRHC = []

def JS_ARRAY():

    for i in range(len(ARRAY_REPGRH)):
        NEW_ELEMENT = ARRAY_REPGRH[i].replace("\n", "")

        ARRAY_GRHC.append(NEW_ELEMENT)

    updateChart(to_js(ARRAY_GRHC))

proxy = create_proxy(JS_ARRAY)

JS_ARRAY
