# htmlpdf.py
# This script demonstrates how to convert a website to a PDF using the pdf2HTML library
# Author: Zoe McNamara Harlowe

import requests
import urllib.parse
from labs.week04.config import config as cfg

targeturl = "https://andrewbeatty1.pythonanywhere.com/bookviewer.html"
apiKey = cfg["htmltopdfkey"]
apiurl = "https://api.html2pdf.app/v1/generate"

params = {'url': targeturl,'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
requesturl = apiurl +"?" + parsedparams
response = requests.get(requesturl)
print (response.status_code)
result = response.content

with open("books.pdf", "wb") as handler:
    handler.write(result)