import time
import pygame

pygame.init()

screen = pygame.display.set_mode((400,200))
pygame.display.set_caption('Timer')
screen.fill((200,200,200))
pygame.display.update()

music = pygame.mixer.music.load('wake-up.wav')

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

    if not begin:
        pygame.draw.rect(screen, (0,155,0), (box[3][0],box[3][1],box_w,box_h))
        start = font.render('Start', True, (0,0,0))
        screen.blit(start, (55, 150))

        pygame.draw.rect(screen, (255,255,0), (box[5][0],box[5][1],box_w,box_h))
        reset = font.render('Reset', True, (0,0,0))
        screen.blit(reset, (300, 150))

    else:
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
    font = pygame.font.SysFont('Arial', 45)
    num = font.render(number, True, (0,0,0))
    numRect = num.get_rect(center=(x+box_w/2, y+box_h/2))
    screen.blit(num, numRect)

def exchange(string):
    if string == '':
        return '00'
    else:
        if int(string) < 10:
            return '0' + str(int(string))
        else:
            return str(int(string))

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
        if not begin:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                b, pos = get_box(x,y)
                if b == 'hour':
                    h, m, s = True, False, False
                elif b == 'min':
                    h, m, s = False, True, False
                elif b == 'sec':
                    h, m, s = False, False, True
                else:
                    h, m, s = False, False, False
                    if b == 'start':
                        begin = True
                    elif b == 'reset':
                        pygame.mixer.music.stop()
                        begin = False
                        hour, minute, second = '', '', ''
        
            if event.type == pygame.KEYDOWN and b == 'hour':
                if event.unicode.isdigit():
                    hour += event.unicode
                    if int(hour) >= 24:
                        hour = ''
                elif event.key == pygame.K_BACKSPACE:
                    hour = ''
                elif event.key == pygame.K_RETURN:
                    h, m, s = False, False, False

            elif event.type == pygame.KEYDOWN and b == 'min':
                if event.unicode.isdigit():
                    minute += event.unicode
                    if int(minute) >= 60:
                        minute = ''
                elif event.key == pygame.K_BACKSPACE:
                    minute = ''
                elif event.unicode == pygame.K_RETURN:
                    h, m, s = False, False, False
            
            elif event.type == pygame.KEYDOWN and b == 'sec':
                if event.unicode.isdigit():
                    second += event.unicode
                    if int(second) >= 60:
                        second = ''
                elif event.key == pygame.K_BACKSPACE:
                    second = ''
                elif event.key == pygame.K_RETURN:
                    h, m, s = False, False, False
        
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                b, pos = get_box(x,y)
                if b == 'stop':
                    begin = False

    if begin:
        if int(hour) == 0 and int(minute) == 0 and int(second) == 0:
            begin = False
            pygame.mixer.music.play(-1)
        else:
            if int(hour) == 0:
                if int(minute) == 0:
                    second = str(int(second) - 1)
                else:
                    if int(second) == 0:
                        second = '59'
                        minute = str(int(minute) - 1)
                    else:
                        second = str(int(second) - 1)
            else:
                if int(minute) == 0:
                    minute = '59'
                    hour = str(int(minute) - 1)
                if int(second) == 0:
                    second = '59'
                    minute = str(int(minute) - 1)

        time.sleep(1)
    
    screen.fill((200,200,200))

    hour = exchange(hour)
    minute = exchange(minute)
    second =exchange(second)

    reset(hour, box[0][0], box[0][1], h)
    reset(minute, box[1][0], box[1][1], m)
    reset(second, box[2][0], box[2][1], s)

    set_time(screen, begin)
    
    pygame.display.update()