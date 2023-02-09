from itertools import permutations 

text = str(input())
textList = []
for i in text:
    textList.append(i)

perm = permutations(textList)
for i in perm:
    print(i)
