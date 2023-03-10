f = open("Copy.txt", "r")
bufer = f.readlines()
f.close()
f = open("Paste.txt", "w")
for i in bufer:
    f.write(i)
f.close    
