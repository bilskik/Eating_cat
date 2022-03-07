import pygame
from tkinter import *
import os.path
import random
from main import *

WIDTH, HEIGHT = 600, 600
board_width,board_height = 570,570
CAT_SIZE = 30
FPS = 60
VEL = 4
VEL_OBJECT = 2
BLACK = (0,0,0)
WHITE = (255,255,255)
RED= (255,0,0)
GREEN = (0,250,0)

direction = ""

class cat():

    def __init__(self):
       pass
    def main_loop(self):
        win = pygame.display.set_mode((WIDTH, HEIGHT))

        cat_image = pygame.image.load(os.path.join('images','cat.png'))
        cat = pygame.transform.scale(cat_image, (CAT_SIZE, CAT_SIZE))

        apple_image = pygame.image.load(os.path.join('images','apple.png'))
        apple = pygame.transform.scale(apple_image, (CAT_SIZE, CAT_SIZE))

        banana_image = pygame.image.load(os.path.join('images', 'banana.png'))
        banana = pygame.transform.scale(banana_image,(CAT_SIZE,CAT_SIZE))

        bomb_image = pygame.image.load(os.path.join('images', 'bomb.png'))
        bomb = pygame.transform.scale(bomb_image,(CAT_SIZE, CAT_SIZE))


        bomb_rect = pygame.Rect(100,100, CAT_SIZE, CAT_SIZE)
        banana_rect = pygame.Rect(60,60,CAT_SIZE,CAT_SIZE)
        apple_rect = pygame.Rect(30, 30,CAT_SIZE,CAT_SIZE)
        head = pygame.Rect(300,300, CAT_SIZE,CAT_SIZE)


        border_left = pygame.Rect(0,0,30,HEIGHT)
        border_top = pygame.Rect(0,0,WIDTH,30)
        border_right = pygame.Rect(WIDTH-30,0,WIDTH,HEIGHT)
        border_down = pygame.Rect(0,HEIGHT-30,WIDTH,HEIGHT)

        clock = pygame.time.Clock()
        global run
        run = True
        checker = 0
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    checker = 1

            key_pressed = pygame.key.get_pressed()
            self.moving(head, key_pressed)
            self.object_move(apple_rect, banana_rect, bomb_rect)
            self.draw(cat, win, head, border_top,border_down,border_right,border_left,apple, apple_rect,banana, banana_rect, bomb,bomb_rect)

        if checker == 0:
            final_win_GUI().main()
        else:
            pygame.quit()

    def draw(self, cat, win, head, border_top,border_down,border_right,border_left, apple, apple_rect,banana,banana_rect, bomb, bomb_rect):

        win.fill(WHITE)

        pygame.draw.rect(win, GREEN, border_top)
        pygame.draw.rect(win,GREEN,border_down)
        pygame.draw.rect(win,GREEN,border_left)
        pygame.draw.rect(win,GREEN,border_right)

        if self.object_check(head,apple_rect,banana_rect, bomb_rect) == 1:
            self.apple_coor(apple_rect,banana_rect,bomb_rect, 1 )
            win.blit(apple, (apple_rect.x, apple_rect.y))
            win.blit(banana,(banana_rect.x, banana_rect.y))
            win.blit(bomb, (bomb_rect.x, bomb_rect.y))

        elif self.object_check(head,apple_rect,banana_rect, bomb_rect) == 2:
            self.apple_coor(apple_rect,banana_rect,bomb_rect, 2)
            win.blit(apple, (apple_rect.x, apple_rect.y))
            win.blit(banana, (banana_rect.x, banana_rect.y))
            win.blit(bomb, (bomb_rect.x, bomb_rect.y))
        elif self.object_check(head,apple_rect,banana_rect, bomb_rect) == 3:
            self.apple_coor(apple_rect,banana_rect,bomb_rect, 3)
            win.blit(apple, (apple_rect.x, apple_rect.y))
            win.blit(banana, (banana_rect.x, banana_rect.y))
            win.blit(bomb, (bomb_rect.x, bomb_rect.y))
        else:
            win.blit(apple,(apple_rect.x,apple_rect.y))
            win.blit(banana,(banana_rect.x, banana_rect.y))
            win.blit(bomb, (bomb_rect.x, bomb_rect.y))


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
    #def check_difficulty(self):

    def object_move(self, apple_rect, banana_rect, bomb_rect):
       # self.check_difficulty()
        apple_rect.y += VEL_OBJECT
        banana_rect.y += VEL_OBJECT
        bomb_rect.y += VEL_OBJECT

    def apple_coor(self, apple_rect, banana_rect, bomb_rect, checker):
        if checker == 1:
            apple_rect.x = random.randrange(30, 570)
            apple_rect.y = 30
        elif checker == 2:
            banana_rect.x = random.randrange(30, 570)
            banana_rect.y = 30
        elif checker == 3:
            bomb_rect.x = random.randrange(30,570)
            bomb_rect.y = 30


    def object_check(self,head,apple_rect, banana_rect, bomb_rect):
        global run
        if apple_rect.y == HEIGHT:
            run = False
        elif banana_rect.y == HEIGHT:
            run = False
        elif bomb_rect.y == HEIGHT:
            self.apple_coor(apple_rect, banana_rect, bomb_rect, 3)

        if head.colliderect(apple_rect):
            #print("touch")
            return 1
        elif head.colliderect(banana_rect):
            return 2
        elif head.colliderect(bomb_rect):
            return 3
        else:
           # print("not touch")
            return 0

class final_win_GUI():
    def __init__(self):
        pass
    def main(self):
        score = Tk()
        score.geometry('300x300')
        score.config(background='black')
        label = Label(score, text="Wynik punktowy: ", font=('Arial', 20), fg="white", bg="black")
        label.place(x=30, y=30)

        play_again_but = Button(score, text="Zagraj ponownie", font=('Arial', 20), fg='white', bg="black",activebackground='black', activeforeground='white', command = lambda : self.close_func(score,0) )
        play_again_but.place(x = 30 , y = 130)

        quit_but = Button(score, text = "Wyjdź do głównego menu" , font = ('Arial',20) , fg = 'white', bg = 'black', activebackground = 'black' , activeforeground = 'white', command = lambda : self.close_func(score,1))
        quit_but.place(x = 30, y = 230)
        score.mainloop()
    def close_func(self, score, checker):
        if checker == 0:
            score.destroy()
            pygame.quit()
            cat().main_loop()
        else:
            score.destroy()
            pygame.quit()


