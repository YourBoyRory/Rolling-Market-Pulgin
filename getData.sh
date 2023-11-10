#!/bin/bash
wget -O ./worth.csv "https://docs.google.com/spreadsheets/d/e/2PACX-1vTFCLa96scKKGwVu77zSCAHW1JPs_Y8XswXykfGYYLUaJI7sV-pyar_BCkZlvKPiafMemV1jatSakg9/pub?output=csv"
cat worth.csv > worthRange.yml

sed -i '/^[,:]\+$/d' worthRange.yml
sed -i 's/,/:\n  max: /' worthRange.yml
sed -i 's/,/\n  min: /' worthRange.yml
sed -i 's/,//g' worthRange.yml
echo "wrote worthRange.yml"
