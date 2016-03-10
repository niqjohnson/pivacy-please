import pygame
import os
from time import sleep

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

#Colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)

#Screen
pitft_screen_size = (320,240)
pitft_screen_center = (160,120)
lcd = pygame.display.set_mode(pitft_screen_size)

#Type
font_big = pygame.font.Font(None, 100)
font_medium = pygame.font.Font(None, 32)

#Status
def get_status(status_file):
    status_file_contents = open(status_file).read()
    status_list = status_file_contents.split()
    status = status_list[0]
    end_time = status_list[1]
    return status, end_time

def set_status(status, end_time):
    pygame.mouse.set_visible(False)
    if status == 'free':
        background_color = black
        font_color = white
        font = font_medium
        message = 'Next meeting at ' + end_time

    if status == 'working':
        background_color = yellow
        font_color = black
        font = font_big
        message = end_time
    if status == 'busy':
        background_color = red
        font_color = white
        font = font_big
        message = end_time
    lcd.fill(background_color)
    display_text = font.render(message, True, font_color)
    rect = display_text.get_rect(center=pitft_screen_center)
    lcd.blit(display_text, rect)
    pygame.display.update()

while True:
    status, end_time = get_status('status.txt')
    set_status(status, end_time)
    sleep(60)
