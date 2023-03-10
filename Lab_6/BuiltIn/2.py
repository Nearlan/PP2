from re import findall


def check(text):
    x = len(findall("[A-Z]",text))
    y = len(findall("[a-z]",text))
    print("A-Z :",x)
    print("a-z :",y)
    
    

check("asdfdfg")
check("MyNameIsArlan")
check("Mne 16 let")  