import pygame
import os.path
import random

WIDTH, HEIGHT = 600, 600
snake_size = 30
FPS = 60
VEL = 3
BLACK = (0,0,0)
WHITE = (255,255,255)
RED= (255,0,0)
GREEN = (0,255,0)
app_x = 30
app_y = 30
direction = ""

class snake():
    def __init__(self, window):
        self.window = window
    def main_loop(self):
        win = pygame.display.set_mode((WIDTH, HEIGHT))

        snake_image = pygame.image.load(os.path.join('kwadrat.png'))
        apple_image = pygame.image.load(os.path.join('apple.png'))
        apple = pygame.transform.scale(apple_image, (snake_size, snake_size))
        part_snake = pygame.transform.scale(snake_image, (snake_size,snake_size))

        head = pygame.Rect(100,400, snake_size,snake_size)

        border_left = pygame.Rect(0,0,30,HEIGHT)
        border_top = pygame.Rect(0,0,WIDTH,30)
        border_right = pygame.Rect(WIDTH-30,0,WIDTH,HEIGHT)
        border_down = pygame.Rect(0,HEIGHT-30,WIDTH,HEIGHT)

        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            key_pressed = pygame.key.get_pressed()
            self.moving(head, key_pressed,border_top,border_down,border_right,border_left)
            checker = self.apple_check(apple,head,win)
            self.draw(part_snake, win, head, border_top,border_down,border_right,border_left,apple, checker)

        pygame.quit()

    def draw(self, part_snake, win, head, border_top,border_down,border_right,border_left, apple, checker):

        win.fill(WHITE)

        pygame.draw.rect(win, GREEN, border_top)
        pygame.draw.rect(win,GREEN,border_down)
        pygame.draw.rect(win,GREEN,border_left)
        pygame.draw.rect(win,GREEN,border_right)

        if checker == 0:
            win.blit(apple,(app_x,app_y))
        else:
            self.apple_coor()
            win.blit(apple,(app_x,app_y))

        win.blit(part_snake,(head.x,head.y))
        pygame.display.update()

    def moving(self, head, key_pressed, border_top,border_down,border_right,border_left):

        global direction

        if key_pressed[pygame.K_UP] :  # up and head.y - head.height > border_top.y
            direction = "up"
        elif key_pressed[pygame.K_DOWN] :  # down and head.y + head.height < border_down.y
            direction = "down"
        elif key_pressed[pygame.K_RIGHT]:   # right and head.x  + head.width < border_right.x
            direction = 'right'
        elif key_pressed[pygame.K_LEFT]:   #left and head.x  - head.width > border_left.x
            direction = 'left'

        if direction == 'up':
            head.y -= VEL
        elif direction == 'down':
            head.y += VEL
        elif direction == 'right':
            head.x += VEL
        elif direction == 'left':
            head.x -= VEL

    def apple_coor(self):
        global app_x
        global app_y
        #app_x = 30
        #app_y = 30
        app_x = random.randrange(30,570,30)
        app_y = random.randrange(30,570,30)
        print("app_x " +str(app_x) + " app_y " +str(app_y))
    def apple_check(self,apple,head,win):
        #print("head.x " + str(head.x) + "app_x " + str(app_x) )
        if head.x == app_x and head.y == app_y:
            return 1
        else:
            return 0

