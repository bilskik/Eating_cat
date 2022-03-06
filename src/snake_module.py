import pygame
import os.path
import random

WIDTH, HEIGHT = 600, 600
board_width,board_height = 570,570
snake_size = 30
FPS = 60
VEL = 4
BLACK = (0,0,0)
WHITE = (255,255,255)
RED= (255,0,0)
GREEN = (0,250,0)

direction = ""

class snake():

    def __init__(self, window):
        self.window = window
    def main_loop(self):
        win = pygame.display.set_mode((WIDTH, HEIGHT))

        cat_image = pygame.image.load(os.path.join('cat.png'))
        cat = pygame.transform.scale(cat_image, (snake_size, snake_size))

        apple_image = pygame.image.load(os.path.join('apple.png'))
        apple = pygame.transform.scale(apple_image, (snake_size, snake_size))


        red = pygame.Rect(30, 30,snake_size,snake_size)
        head = pygame.Rect(300,300, snake_size,snake_size)


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

            print(head.x)
            print(head.y)
            print(red.x)
            print(red.y)
            key_pressed = pygame.key.get_pressed()
            self.moving(head, key_pressed)
            self.draw(cat, win, head, border_top,border_down,border_right,border_left,apple, red)


        pygame.quit()

    def draw(self, cat, win, head, border_top,border_down,border_right,border_left, apple, red):

        win.fill(WHITE)

        pygame.draw.rect(win, GREEN, border_top)
        pygame.draw.rect(win,GREEN,border_down)
        pygame.draw.rect(win,GREEN,border_left)
        pygame.draw.rect(win,GREEN,border_right)

        if self.apple_check(head,red) == 1:
            self.apple_coor(red)
            win.blit(apple, (red.x, red.y))
        else:
            win.blit(apple,(red.x,red.y))


        win.blit(cat,(head.x,head.y))
        pygame.display.update()

    def moving(self, head, key_pressed):

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

    def apple_coor(self, red):
        red.x = random.randrange(30,570,30)
        red.y = random.randrange(30,570,30)

    def apple_check(self,head,red):
        if head.colliderect(red):
            print("touch")
            return 1
        else:
            print("not touch")
            return 0




