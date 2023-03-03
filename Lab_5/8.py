import re

def find(text):
    ToFind = '[ .,]'
    return re.findall("[A-Z][a-z]*", text)



print(find("HelloMyNameIsArlan"))