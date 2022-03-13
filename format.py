import sys
import csv
import json
import xml.etree.ElementTree as ET

def readFile(fileName):
    rows = []
    with open(fileName, 'r', encoding='latin1') as f:
        for line in f:
            rows.append(line.split('\t'))
    return rows

def toCSV(fileName, rows):
    with open(fileName, 'w') as fileName:
        writer = csv.writer(fileName)
        writer.writerows(rows)

def toJSON(fileName, rows):
    with open(fileName, 'w') as f:
        data = []
        for i in range(1, len(rows)):
            data.append(dict(zip(rows[0], rows[i])))
        json.dump(data, f, indent=4)

def toXML(fileName, rows):
    root = ET.Element('data')
    for i in range(1, len(rows)):
        item = ET.Element('item')
        root.append(item)
        for j in range(len(rows[i])):
            keyName = rows[0][j].replace(' ', '')
            keyName = keyName.replace('(', '')
            keyName = keyName.replace(')', '')
            cur = ET.SubElement(item, keyName)
            cur.text = rows[i][j]
    tree = ET.ElementTree(root)
    with open(fileName, 'wb') as fileName:
        tree.write(fileName)

fName = sys.argv[1]
rows = readFile(fName)
if sys.argv[2] == '-c':
    toCSV('data.csv', rows)
elif sys.argv[2] == '-j':
    toJSON('data.json', rows)
elif sys.argv[2] == '-x':
    toXML('data.xml', rows)
else :
    print('invalid format')