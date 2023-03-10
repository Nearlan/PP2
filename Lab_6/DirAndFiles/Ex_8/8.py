import os

if os.path.exists("DeleteMe.txt") and os.access("DeleteMe.txt" ,os.F_OK):
    os.remove("DeleteMe.txt")
else:
    print("I can`t do it")