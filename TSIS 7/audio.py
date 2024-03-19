import pygame

pygame.init()

w, h = 800, 800
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Your broken radio")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 