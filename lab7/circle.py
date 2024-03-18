import pygame

pygame.init()
W,H = 400,300
screen = pygame.display.set_mode((W, H))
done = False
is_blue = True
x = W//2
y = H//2
radius = 25
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y -3 - radius>=0:
             y -= 3
        if pressed[pygame.K_DOWN] and y + 3 + radius <= H:
             y += 3
        if pressed[pygame.K_LEFT] and x - 3 - radius >= 0:
             x -= 3
        if pressed[pygame.K_RIGHT] and x + 3 + radius<=W:
             x += 3

        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (0,255,0), (x, y), radius)
        pygame.display.flip()
        clock.tick(60)