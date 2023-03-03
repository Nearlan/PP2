import re

def find(text):
    ToFind = '[ .,]'
    return " ".join(re.findall("[A-Z][a-z]*", text))



print(find("HelloMyNameIsArlan"))