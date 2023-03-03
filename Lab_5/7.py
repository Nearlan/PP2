import re

def find(text):
    ToFind = '[ .,]'
    return "".join(x.capitalize() for x in text.split("_"))



print(find("hello_my_name_is_arlan"))
