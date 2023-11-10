import yaml
import random
import csv
from pprint import pprint
from urllib.request import urlretrieve

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTFCLa96scKKGwVu77zSCAHW1JPs_Y8XswXykfGYYLUaJI7sV-pyar_BCkZlvKPiafMemV1jatSakg9/pub?output=csv"
downloadFile = 'download_cache/worth.csv'
essentialsWorthYML='plugins/Essentials/worth.yml'

try:
    urlretrieve(url, downloadFile)
except:
    print("Failed to update worths")
    pass

newItems = {}
newItems['worth'] = {} 
worthRangeDictionary = {}

with open(downloadFile) as worthSpreadSheet:
   for line in csv.DictReader(worthSpreadSheet, fieldnames=('item', 'max', 'min')):
        worthRangeDictionary[line['item']] = {}
        worthRangeDictionary[line['item']]['max'] = float(line['max'])
        worthRangeDictionary[line['item']]['min'] = float(line['min'])
    

for item in worthRangeDictionary:
    newItems['worth'][item] = round(random.uniform(worthRangeDictionary[item]['min'], worthRangeDictionary[item]['max']), 2)


with open(essentialsWorthYML, 'w') as worthFile:
    yaml.dump(newItems, worthFile)
