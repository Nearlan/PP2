import re


file = open('row.txt', encoding='utf-8')
text = file.read()
BinP = "\nБИН\s+[0-9]{12}"
binvalue = re.search(BinP, text).group()
print(binvalue)