import pygame
import sys
pygame.font.init()
 
sc = pygame.display.set_mode((300, 200))
sc.fill((255, 255, 255))
need_input = False
score = ''
 
f2 = pygame.font.Font('EightBits.ttf', 48)
text2 = f2.render(str(score), False,
                  (0, 180, 0))
place = text2.get_rect( center=(150, 100))
sc.blit(text2, place)
pygame.display.update()

while 1:
    sc.fill((255, 255, 255))
    
    key = pygame.key.get_pressed()
    if key[pygame.K_5]:
        need_input = True
        
        

    text2 = f2.render(str(score), False,
                  (0, 180, 0))
    place = text2.get_rect( center=(150, 100))
    sc.blit(text2, place)
    pygame.display.update()
    
    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if need_input and i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RETURN:
                need_input = False
                score = '' 
            elif i.key == pygame.K_BACKSPACE:
                score = score[0: -1]
            else:
                score += i.unicode