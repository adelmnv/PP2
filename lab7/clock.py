import pygame
import os
import time
import math

def rot_center(image, angle, x, y):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=(x, y)).center)
    return rotated_image, new_rect

pygame.init()

width = 500  
height = 400 

mickey = pygame.image.load("images/clock.png")
mickey = pygame.transform.scale(mickey, (width, height))
mickey_rect = mickey.get_rect()

right = pygame.image.load("images/right.png")
right = pygame.transform.scale(right, (300, 100))
right, right_rect = rot_center(right, 90, mickey_rect.centerx, mickey_rect.centery)

left = pygame.image.load("images/left.png")
left = pygame.transform.scale(left, (300, 100))
left, left_rect = rot_center(left, 90, mickey_rect.centerx, mickey_rect.centery)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    current_time = time.localtime() 
    seconds_angle = -((current_time.tm_sec / 60) * 360 )
    minutes_angle = -(((current_time.tm_min + current_time.tm_sec / 60) / 60) * 360)

    screen.fill((255, 255, 255))

    screen.blit(mickey, (0, 0))

    right_rotated, right_rect = rot_center(right, minutes_angle, mickey_rect.centerx, mickey_rect.centery)
    left_rotated, left_rect = rot_center(left, seconds_angle, mickey_rect.centerx, mickey_rect.centery)

    screen.blit(left_rotated, left_rect.topleft)
    screen.blit(right_rotated, right_rect.topleft)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()

