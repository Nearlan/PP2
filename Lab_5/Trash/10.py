import re

def find(text):
    y = re.split("[A-Z]", text)
    s = "_0".join(y)
    return s



print(find("hello"))
