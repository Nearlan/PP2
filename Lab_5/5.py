
import re

def find(text):
    ToFind = 'a.*b$'
    return re.search(ToFind, text)



print(find("dadabasaddfadb"))
print(find("abadsddsab"))
print(find("v_sfgfasddsa54654b"))
print(find("_aasd"))
print(find("_Akndpo"))
print(find("45_A_Da"))