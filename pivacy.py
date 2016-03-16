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
label_center = (160,90)
end_time_center = (160,135)
lcd = pygame.display.set_mode(pitft_screen_size)

#Type
font_big = pygame.font.Font(None, 100)
font_medium = pygame.font.Font(None, 32)

#Status
def get_status(status_file):
    with open(status_file) as status_file_opened:
        status_file_contents = status_file_opened.read()
        status_list = status_file_contents.split()
        status = status_list[0]
        end_time = status_list[1]
        return status, end_time

def set_status(status, end_time):
    pygame.mouse.set_visible(False)
    if status == 'free':
        background_color = black
        font_color = white
        label_content = 'Free until'
    if status == 'working':
        background_color = yellow
        font_color = black
        label_content = 'Working until'
    if status == 'busy':
        background_color = red
        font_color = white
        label_content = 'Busy until'
    lcd.fill(background_color)
    label_text = font_medium.render(label_content, True, font_color)
    label_rect = label_text.get_rect(center=label_center)
    end_time_text = font_big.render(end_time, True, font_color)
    end_time_rect = end_time_text.get_rect(center=end_time_center)
    lcd.blit(label_text, label_rect)
    lcd.blit(end_time_text, end_time_rect)
    pygame.display.update()

while True:
    status, end_time = get_status('status.txt')
    set_status(status, end_time)
    sleep(60)
