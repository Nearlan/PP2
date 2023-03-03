import re

def find(text):
    ToFind = '[A-Z]{1}[a-z]+'
    return re.search(ToFind, text)



print(find("abbsa"))
print(find("abb"))
print(find("v_sfgfb"))
print(find("_aasd"))
print(find("_Akndpo"))
print(find("45_A_Da"))