def levelbuilding():
    level = open(f"Levels\Level_{1}.txt", 'r')
    blocks = []
    x,y = 0, 0
    for j in level:
        for i in j:  
            if i == '#':
                blocks.append((x, y))
            x += 50
        y += 50
        x = 0 
    level.close()   
    return blocks

blocks = levelbuilding()
for i in blocks:
    print(i)
cnt = 0
level = open(f"Levels\Level_{1}.txt", 'r')
for j in level:
        for i in j: 
            cnt += 1
        
            
print(cnt)
level.close()