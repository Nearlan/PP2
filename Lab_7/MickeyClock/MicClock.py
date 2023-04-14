import pygame
from datetime import datetime
pygame.init()
screen = pygame.display.set_mode((500, 500))

# images
clock = pygame.image.load('clock.jpg')
longarm = pygame.image.load('longarm.png')
shortarm = pygame.image.load('shortarm.png')
# working with images
clock = pygame.transform.scale(clock, (500, 500))
# rotating
# rendering
# main
done = False
while not done:
        pygame.time.delay(60)
        screen.fill((0, 0 ,0))
        # time
        t = datetime.now().minute
        s = datetime.now().second
        spin = -t * 6
        spins = -s * 6
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.blit(clock, (0, 0))
        shrot = pygame.transform.rotate(shortarm, spin)
        longrot = pygame.transform.rotate(longarm, spins)
        screen.blit(shrot, (250 - int(shrot.get_width()) / 2, 250 - int(shrot.get_height()) / 2))
        screen.blit(longrot, (250 - int(longrot.get_width()) / 2, 250 - int(longrot.get_height()) / 2))
        pygame.display.update()