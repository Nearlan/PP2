import re

def find(text):
    ToFind = '[a-z]+_[a-z]+'
    return re.search(ToFind, text)



print(find("abbsa"))
print(find("abb"))
print(find("v_sfgfb"))
print(find("_aasd"))
print(find("_Akndpo"))
print(find("45_A_D"))