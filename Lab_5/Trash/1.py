import re


file = open('2.txt', encoding='utf-8')
text = file.read()
find = "a(b*)"
binvalue = re.search(find, text)
print(binvalue) 