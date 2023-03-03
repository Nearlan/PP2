import re


file = open('2.txt', encoding='utf-8')
text = file.read()
find = "ab{2,3}"
binvalue = re.search(find, text).group()
print(binvalue) 