import pygame

pygame.init()

w, h = 800, 800
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Task Number 3")
icon = pygame.image.load("mikkey.jpeg")
pygame.display.set_icon(icon)

x, y = w // 2, h // 2
r = 25

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y = max(y - 20, r)
    if keys[pygame.K_DOWN]:
        y = min(y + 20, h - r)
    if keys[pygame.K_RIGHT]:
        x = min(x + 20, w - r)
    if keys[pygame.K_LEFT]:
        x = max(x - 20, r)
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, "red", (x, y), r)
    pygame.display.update()