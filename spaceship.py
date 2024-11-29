import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH,HEIGHT=900,500

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space Invaders Game!")

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)

BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)

HEALTH_FONT=pygame.font.SysFont("Georgia", 40)
WINNER_FONT=pygame.font.SysFont("Arial", 100)

FPS=60
VEL=5
BULLET_VEL=7
MAX_BULLETS=3

SPACESHIP_WIDTH, SPACESHIP_HEIGHT= 55, 40

YELLOW_HIT = pygame.USEREVENT+1
RED_HIT = pygame.USEREVENT=+2

YELLOW_SPACESHIP_IMAGE=pygame.image.load("Lesson 6/images/spaceship_yellow.png")
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT),90))
RED_SPACESHIP_IMAGE=pygame.image.load("Lesson 6/images/spaceship_red.png")
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT),270))

SPACE = pygame.transform.scale(pygame.image.load("Lesson 6/images/space.png"),(WIDTH,HEIGHT))

def draw_window(red, yellow, redbullets, yellowbullets, red_health, yellow_health):
    screen.blit(SPACE,(0,0))
    pygame.draw.rect(screen,BLACK,BORDER)

    red_health_text = HEALTH_FONT.render("Health: "+ str(red_health),1,WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: "+ str(yellow_health),1,WHITE)
    screen.blit(red_health_text, (WIDTH-red_health_text.get_width()-10,10))
    screen.blit(yellow_health_text, (10,10))
    screen.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    screen.blit(RED_SPACESHIP,(red.x,red.y))
