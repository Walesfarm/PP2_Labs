import pygame
import math
import datetime

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Stupid clock")
icon = pygame.image.load("mikkey.jpeg")
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False