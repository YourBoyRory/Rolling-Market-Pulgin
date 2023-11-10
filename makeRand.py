import yaml
import random
import csv
from pprint import pprint
from urllib.request import urlretrieve

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTFCLa96scKKGwVu77zSCAHW1JPs_Y8XswXykfGYYLUaJI7sV-pyar_BCkZlvKPiafMemV1jatSakg9/pub?output=csv"
filename = './cache/worth.csv'
try:
    urlretrieve(url, filename)
except:
    print("Failed to download file")
    pass

newItems = {}
newItems['worth'] = {} 

worthRangeDictionary = {}

with open('./cache/worth.csv') as f:
   for line in csv.DictReader(f, fieldnames=('item', 'max', 'min')):
        worthRangeDictionary[line['item']] = {}
        worthRangeDictionary[line['item']]['max'] = float(line['max'])
        worthRangeDictionary[line['item']]['min'] = float(line['min'])
    

for item in worthRangeDictionary:
    newItems['worth'][item] = round(random.uniform(worthRangeDictionary[item]['min'], worthRangeDictionary[item]['max']), 2)


with open('worth.yml', 'w') as worthFile:
    yaml.dump(newItems, worthFile)

with open('worthRange.yml', 'w') as worthRangeFile:
    yaml.dump(worthRangeDictionary, worthRangeFile)
