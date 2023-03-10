list = list(("My", "Name", "Is", "Arlan"))
f = open("Mylist.txt", "w")
for i in list:
    f.write(i + " ")
f.close()