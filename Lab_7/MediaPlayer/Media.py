import pygame
import sys

pygame.init()
# main 
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400,400))
done = False
# music
id = 0 # Song Id
playlist = ["song_1.mp3", "song_2.mp3", "song_3.mp3"]
pygame.mixer.music.load(playlist[id])
pygame.mixer.music.play(-1)
# text and font
f1 = pygame.font.Font(None, 72)
pause = f1.render("||", True, (180, 0, 0))
play = f1.render("=}", True, (180, 0, 0))
Songname = f1.render("Song " + str(id), True, (180, 0, 0))
place1 = pause.get_rect(
    center=(200, 200))
place2 = play.get_rect(
    center=(200, 200))
place3 = Songname.get_rect(center = (200, 100))
pc = False 

while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    pc = not pc
# Next and Prev
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    id -= 1
                    if id == -1:
                        id = 2
                    pygame.mixer.music.load(playlist[id])
                    Songname = f1.render("Song " + str(id), True, (180, 0, 0))
                    pygame.mixer.music.play(-1)
                    
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    id += 1
                    if id == 3:
                        id = 0
                    pygame.mixer.music.load(playlist[id])
                    Songname = f1.render("Song " + str(id), True, (180, 0, 0))
                    pygame.mixer.music.play(-1)
# Pause and Play
    if pc:
            screen.fill((255, 255, 255))
            screen.blit(pause, place1)
            pygame.mixer.music.pause()
    else:
            screen.fill((255, 255, 255))
            screen.blit(play, place2)
            pygame.mixer.music.unpause()
    
    screen.blit(Songname, place3)
    pygame.display.update()
        