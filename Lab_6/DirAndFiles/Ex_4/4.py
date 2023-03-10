

f = open("text_1.txt", "r")
print(len(f.readlines()))
f.close()
f = open("text_2.txt", "r")
print(len(f.readlines()))
f.close()