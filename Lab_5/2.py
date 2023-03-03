import re

def find(text):
    ToFind = 'ab{2,3}'
    return re.search(ToFind, text)



print(find("abbsa"))
print(find("abb"))
print(find("vadffabbbsa"))
print(find("abbbbbsa"))
print(find("abbbbbbb"))
print(find("vadffabbbbbbbsa"))