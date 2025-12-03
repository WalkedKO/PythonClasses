import sys
from random import randint

import pygame
import flakes
pygame.init()

width =  800
height = 600
screen = pygame.display.set_mode((width, height))

FPS = 60
clock = pygame.time.Clock()

spawn_flake = pygame.USEREVENT + 1
left_max = 800
flake_size = 80
flakes_list = []

pygame.time.set_timer(spawn_flake, 1000)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == spawn_flake:
            flakes_list.append(flakes.Flake(randint(0, left_max), 0, flake_size, flake_size))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for id, fl in enumerate(flakes_list):
                if fl.collidepoint(pos) and fl.moving:
                    flakes_list.pop(id)
    screen.fill('black')
    for id, fl in enumerate(flakes_list):
        if fl.moving:
            fl.move_ip(0, 2)
            pygame.draw.rect(screen, 'white', fl)
            col = False
            for idel, el in enumerate(flakes_list):
                if fl.colliderect(el) and idel != id:
                    col = True
                    break
            if col or fl.top >= height - fl.height:
                flakes_list[id].moving = False
        else:
            pygame.draw.rect(screen, 'gray', fl)

    pygame.display.flip()
    clock.tick(FPS)
