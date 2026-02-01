# trains.py
# This program reads in an XML file and prints data for all trains in Ireland
# Author: Zoe McNamara Harlowe

import requests
import csv
from xml.dom.minidom import parseString

url = "https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

doc = parseString(page.content)

# Tags to retrieve
retrieveTags = [
    'TrainStatus',
    'TrainLatitude',
    'TrainLongitude',
    'TrainCode',
    'TrainDate',
    'PublicMessage',
    'Direction'
]

# Get all objTrainPositions nodes
objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")

with open("train_data.csv", "w", newline="") as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for node in objTrainPositionsNodes:
        # Extract the train code
        traincode_node = node.getElementsByTagName("TrainCode").item(0)
        traincode = traincode_node.firstChild.nodeValue.strip()

        # Filter: only trains starting with D
        if not traincode.startswith("D"):
            continue

        # Build the row of data
        dataList = []
        for tag in retrieveTags:
            datanode = node.getElementsByTagName(tag).item(0)
            value = datanode.firstChild.nodeValue.strip() if datanode.firstChild else ""
            dataList.append(value)

        # Write filtered row to CSV
        train_writer.writerow(dataList)
