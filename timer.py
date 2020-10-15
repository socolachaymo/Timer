import time
import sys
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400,200))
pygame.display.set_caption('Timer')
screen.fill((200,200,200))
pygame.display.update()

def new_timer():
    return input('')

box = [(20,70), (155,70), (280,70), (40,140), (160,140), (290,140)]
control = ['hour','min','sec','start','stop','reset']
box_w = 70
box_h = 50

def set_time(screen, begin):
    text = font.render('SET TIMER', True, (0,0,0))
    screen.blit(text, (150,20))

    pygame.draw.rect(screen, (0,0,0), (box[0][0],box[0][1],box_w,box_h), 2)
    hour = font.render('hours', True, (0,0,0))
    screen.blit(hour, (100, 80))
    pygame.draw.rect(screen, (0,0,0), (box[1][0],box[1][1],box_w,box_h), 2)
    minute = font.render('min', True, (0,0,0))
    screen.blit(minute, (235, 80))
    pygame.draw.rect(screen, (0,0,0), (box[2][0],box[2][1],box_w,box_h), 2)
    sec = font.render('sec', True, (0,0,0))
    screen.blit(sec, (360, 80))

    pygame.draw.rect(screen, (0,155,0), (box[3][0],box[3][1],box_w,box_h))
    start = font.render('Start', True, (0,0,0))
    screen.blit(start, (55, 150))

    pygame.draw.rect(screen, (255,255,0), (box[5][0],box[5][1],box_w,box_h))
    reset = font.render('Reset', True, (0,0,0))
    screen.blit(reset, (300, 150))

    if begin:
        pygame.draw.rect(screen, (200,0,0), (box[4][0],box[4][1],box_w,box_h))
        stop = font.render('Stop', True, (0,0,0))
        screen.blit(stop, (175, 150))


def get_box(x,y):
    for b in box:
        if x >= b[0] and x <= b[0] + box_w:
            if y >= b[1] and y <= b[1] + box_h:
                i = box.index(b)
                return control[i], b
    return None, 0

def reset(number,x,y,background):
    if background:
        pygame.draw.rect(screen, (255,0,0), (x,y,box_w,box_h))
    if number == '':
        number = '00'
    font = pygame.font.SysFont('Arial', 45)
    num = font.render(number, True, (0,0,0))
    screen.blit(num, (x+15, y))

font = pygame.font.SysFont('Arial', 20)
hour = ''
minute = ''
second = ''
b = None
h, m, s = False, False, False
begin = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            b, pos = get_box(x,y)
            if b is None:
                h, m, s = False, False, False
                pass
            else:
                if b == 'hour':
                    h, m, s = True, False, False
                elif b == 'min':
                    h, m, s = False, True, False
                elif b == 'sec':
                    h, m, s = False, False, True

        if event.type == pygame.KEYDOWN and b == 'hour':
            if event.unicode.isdigit():
                hour += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                hour = ''
            elif event.key == pygame.K_RETURN:
                h, m, s = False, False, False

        if event.type == pygame.KEYDOWN and b == 'min':
            if event.unicode.isdigit():
                minute += event.unicode
            elif event.unicode == pygame.K_BACKSPACE:
                minute = ''
            elif event.unicode == pygame.K_RETURN:
                h, m, s = False, False, False
        
        if event.type == pygame.KEYDOWN and b == 'sec':
            if event.unicode.isdigit():
                second += event.unicode
            elif event.unicode == pygame.K_BACKSPACE:
                second = ''
            elif event.unicode == pygame.K_RETURN:
                h, m, s = False, False, False

    screen.fill((200,200,200))
    print(hour, minute, second)
    reset(hour, box[0][0], box[0][1], h)
    reset(minute, box[1][0], box[1][1], m)
    reset(second, box[2][0], box[2][1], s)

    set_time(screen, begin)
    
    pygame.display.update()
sys.exit()