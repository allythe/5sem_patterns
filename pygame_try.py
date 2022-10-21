
import time

import pygame

WIDTH = 640
HEIGHT = 480
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Player Test")
clock = pygame.time.Clock()
FPS = 60

def create_car(surface, x, y, w, h, color):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(surface, color, rect)
    return rect

running = True
vx = 0
vy = 0
player_x = WIDTH / 2 # middle of screen width
player_y = HEIGHT / 2 # middle of screen height
player_speed = 5
while running:
    clock.tick(FPS)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                vx = -player_speed
            elif e.key == pygame.K_RIGHT:
                vx = player_speed
            if e.key == pygame.K_UP:
                vy = -player_speed
            elif e.key == pygame.K_DOWN:
                vy = player_speed
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT or\
               e.key == pygame.K_UP or e.key == pygame.K_DOWN:
                vx = 0
                vy = 0

    player_x += vx
    player_y += vy
    display.fill((200, 200, 200))
    ####make the player#####
    player = create_car(display, player_x, player_y, 10, 10, (255, 0, 0))
    pygame.display.flip()