import re

def find(text):
    ToFind = '^a(b*)$'
    return re.search(ToFind, text)



print(find("abbsa"))
print(find("abb"))
print(find("vadffabbbsa"))
    