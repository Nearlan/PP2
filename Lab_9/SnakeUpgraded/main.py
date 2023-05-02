import pygame
from random import randrange
from random import choice

pygame.init()

res = 800
size = 50

x, y = 400, 400
apple = randrange(0 , res, size), randrange(0 , res, size)

dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
# scoreboard
f = pygame.font.Font('EightBits.ttf', 70)
score = 0

# Apple weight
wght = [1, 2]
apsc = choice(wght)
if apsc == 1:
    apcol = 'red'
else:
    apcol = 'pink'



fps = 5
lvl = 0
Play = True


def levelbuilding():
    level = open(f"Levels\Level_{lvl}.txt", 'r')
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
            
sc = pygame.display.set_mode([res, res])
clock = pygame.time.Clock()


while Play:
    # Control
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}
        
    
    # Level change
    if length >= 6:
        length = 1
        x, y = 400, 400
        dx, dy = 0, 0
        lvl += 1
        blocks = levelbuilding()
        
        
    
    # Snake moving
    x += dx * size
    y += dy * size
    snake.append((x,y))
    snake = snake[-length:]
    
    

           
                   
    # Drawing
    sc.fill(pygame.Color('black'))
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, size, size))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color(apcol), (*apple, size, size))
    for i in blocks:
        pygame.draw.rect(sc, pygame.Color('white'), (i[0], i[1], size, size))
        
    # Scoreboard rendering
    text2 = f.render(str(score), False, (0, 180, 0))
    place = text2.get_rect( center=(400, 400))
    sc.blit(text2, place)

    

    
    # Eating apples
    if snake[-1] == apple:
        
        length += apsc
        fps += 1
        score += apsc
        # Apple new appearance
        wght = [1, 2]
        apsc = choice(wght)
        if apsc == 1:
            apcol = 'red'
        elif apsc == 2:
            apcol = 'pink'
        apple = randrange(0 , res, size), randrange(0 , res, size)
            # Collision check
        for i in blocks:
            while apple == i:
                apple = randrange(0 , res, size), randrange(0 , res, size)
        for i in snake:
            while apple == 1:
                apple = randrange(0 , res, size), randrange(0 , res, size)                  

        
    
    
    pygame.display.flip()
    clock.tick(fps)
    
    
    # Game over
    if x < 0 or x > res - size or y < 0 or y > res - size:
        break
    if len(snake) != len(set(snake)):
        break
    for i in blocks:
        lose = (i[0], i[1])
        if snake[-1] == lose:
            Play = False
            
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
