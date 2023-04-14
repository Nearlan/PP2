import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 300))
done = False
RED = (255, 0, 0)
x = 200
y = 150

while not done:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        x1 = x
        y1 = y
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 20
        if pressed[pygame.K_DOWN]: y += 20
        if pressed[pygame.K_LEFT]: x -= 20
        if pressed[pygame.K_RIGHT]: x += 20
        if x < 25: x = 25
        if x > 375: x = 375
        if y < 25: y = 25
        if y > 275: y = 275
        pygame.draw.circle(screen, RED,(x, y), 25)
        pygame.display.flip()
        clock.tick(60)