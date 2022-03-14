import pygame
from tkinter import *
import os.path
import random
from main import *

pygame.init()
WIDTH, HEIGHT = 600, 600
board_width,board_height = 570,570
CAT_SIZE = 45
FPS = 60
VEL = 7
VEL_OBJECT = 2
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED= (255,0,0)
GREEN = (0,250,0)
LIVE_COUNTER = 3
SCORE = 0
SCORE_FONT = pygame.font.SysFont('comicsans', 40)
STARTING_Y = 30


class cat():

    def __init__(self, difficulty):
       self.dif = difficulty
    def main_loop(self):
        global LIVE_COUNTER
        global SCORE
        global VEL
        global VEL_OBJECT
        global HEALTH_FONT
        pygame.init()
        HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
        if self.dif == 'easy':
            VEL = 8
            VEL_OBJECT = 2
            LIVE_COUNTER = 30
        elif self.dif == 'hard':
            VEL = 10
            VEL_OBJECT = 4
            LIVE_COUNTER = 10

        win = pygame.display.set_mode((WIDTH, HEIGHT))


        cat_image = pygame.image.load(os.path.join('images','cat.png'))
        cat = pygame.transform.scale(cat_image, (CAT_SIZE, CAT_SIZE))

        apple_image = pygame.image.load(os.path.join('images','apple.png'))
        apple = pygame.transform.scale(apple_image, (CAT_SIZE, CAT_SIZE))

        banana_image = pygame.image.load(os.path.join('images', 'banana.png'))
        banana = pygame.transform.scale(banana_image,(CAT_SIZE,CAT_SIZE))

        cookies_image = pygame.image.load(os.path.join('images', 'cookies.png'))
        cookies = pygame.transform.scale(cookies_image,(CAT_SIZE, CAT_SIZE))

        shake_image = pygame.image.load(os.path.join('images', 'shake.png'))
        shake = pygame.transform.scale(shake_image,(CAT_SIZE,CAT_SIZE))

        bomb_image = pygame.image.load(os.path.join('images', 'bomb.png'))
        bomb = pygame.transform.scale(bomb_image,(CAT_SIZE, CAT_SIZE))


        shake_rect = pygame.Rect(self.starting_positions(),STARTING_Y,CAT_SIZE,CAT_SIZE)
        cookies_rect = pygame.Rect(self.starting_positions(),STARTING_Y,CAT_SIZE,CAT_SIZE)
        bomb_rect = pygame.Rect(self.starting_positions(),STARTING_Y, CAT_SIZE, CAT_SIZE)
        banana_rect = pygame.Rect(self.starting_positions(),STARTING_Y,CAT_SIZE,CAT_SIZE)
        apple_rect = pygame.Rect(self.starting_positions(), STARTING_Y,CAT_SIZE,CAT_SIZE)
        head = pygame.Rect(300,300, CAT_SIZE,CAT_SIZE)



        border_left = pygame.Rect(0,0,30,HEIGHT)
        border_top = pygame.Rect(0,0,WIDTH,30)
        border_right = pygame.Rect(WIDTH-30,0,WIDTH, HEIGHT)
        border_down = pygame.Rect(0,HEIGHT-5,WIDTH, HEIGHT)

        SCORE = 0
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
            self.moving(head, key_pressed,border_top, border_down, border_right, border_left)
            self.object_move(apple_rect, banana_rect, bomb_rect, cookies_rect, shake_rect)
            self.draw(cat, win, head, border_top,border_down,border_right,border_left,apple, apple_rect,banana,
                      banana_rect, bomb, bomb_rect, cookies, cookies_rect,shake,shake_rect)

            if LIVE_COUNTER == 0:
                run = False


        if checker == 0:
            final_win_GUI(self.dif).main()
        else:
            pygame.quit()
        pygame.display.quit()
        pygame.quit()

    def draw(self, cat, win, head, border_top,border_down,border_right,border_left, apple, apple_rect,banana,banana_rect,
             bomb, bomb_rect, cookies,cookies_rect,shake,shake_rect):

        win.fill(WHITE)

        pygame.draw.rect(win, GREEN, border_top)
        pygame.draw.rect(win,GREEN,border_down)
        pygame.draw.rect(win,GREEN,border_left)
        pygame.draw.rect(win,GREEN,border_right)

        checker = self.object_check(head,border_down,apple_rect,banana_rect, bomb_rect, cookies_rect, shake_rect)

        if checker == 1:
            self.apple_coor(apple_rect,banana_rect,bomb_rect, cookies_rect, shake_rect, 1 )
            win.blit(apple, (apple_rect.x, apple_rect.y))
            win.blit(banana,(banana_rect.x, banana_rect.y))
            win.blit(bomb, (bomb_rect.x, bomb_rect.y))
            win.blit(cookies, (cookies_rect.x, cookies_rect.y))
            win.blit(shake, (shake_rect.x, shake_rect.y))


        elif checker == 2:
            self.apple_coor(apple_rect,banana_rect,bomb_rect, cookies_rect, shake_rect, 2)
            win.blit(apple, (apple_rect.x, apple_rect.y))
            win.blit(banana, (banana_rect.x, banana_rect.y))
            win.blit(bomb, (bomb_rect.x, bomb_rect.y))
            win.blit(cookies, (cookies_rect.x, cookies_rect.y))
            win.blit(shake, (shake_rect.x, shake_rect.y))

        elif checker == 3:
            self.apple_coor(apple_rect,banana_rect,bomb_rect,cookies_rect, shake_rect,  3)
            win.blit(apple, (apple_rect.x, apple_rect.y))
            win.blit(banana, (banana_rect.x, banana_rect.y))
            win.blit(bomb, (bomb_rect.x, bomb_rect.y))
            win.blit(cookies, (cookies_rect.x, cookies_rect.y))
            win.blit(shake, (shake_rect.x, shake_rect.y))

        elif checker == 4:
            self.apple_coor(apple_rect, banana_rect, bomb_rect, cookies_rect, shake_rect, 4)
            win.blit(apple, (apple_rect.x, apple_rect.y))
            win.blit(banana, (banana_rect.x, banana_rect.y))
            win.blit(bomb, (bomb_rect.x, bomb_rect.y))
            win.blit(cookies, (cookies_rect.x, cookies_rect.y))
            win.blit(shake, (shake_rect.x, shake_rect.y))


        elif checker == 5:
            self.apple_coor(apple_rect, banana_rect, bomb_rect, cookies_rect, shake_rect, 5)
            win.blit(apple, (apple_rect.x, apple_rect.y))
            win.blit(banana, (banana_rect.x, banana_rect.y))
            win.blit(bomb, (bomb_rect.x, bomb_rect.y))
            win.blit(cookies, (cookies_rect.x, cookies_rect.y))
            win.blit(shake, (shake_rect.x, shake_rect.y))


        else:
            win.blit(apple, (apple_rect.x,apple_rect.y))
            win.blit(banana, (banana_rect.x, banana_rect.y))
            win.blit(bomb, (bomb_rect.x, bomb_rect.y))
            win.blit(cookies, (cookies_rect.x, cookies_rect.y))
            win.blit(shake, (shake_rect.x, shake_rect.y))

        health_text = HEALTH_FONT.render("Życia: " + str(LIVE_COUNTER), 1, BLACK)
        win.blit(health_text, (WIDTH - health_text.get_width() - 10, 5))

        score_text = SCORE_FONT.render("Punkty: " + str(SCORE), 1 , BLACK)
        win.blit(score_text, (10, 5))

        win.blit(cat, (head.x,head.y))
        pygame.display.update()

    def moving(self, head, key_pressed, border_top, border_down, border_right, border_left):

        if key_pressed[pygame.K_UP] and head.y - head.height > border_top.y :  # up
            head.y -= VEL
        elif key_pressed[pygame.K_DOWN] and head.y + head.height < border_down.y:  # down
            head.y += VEL
        elif key_pressed[pygame.K_RIGHT] and head.x + head.width < border_right.x:   # right
            head.x += VEL
        elif key_pressed[pygame.K_LEFT] and head.x - head.width > border_left.x:   #left
            head.x -= VEL

    def object_move(self, apple_rect, banana_rect, bomb_rect, cookies_rect, shake_rect):

        apple_rect.y += VEL_OBJECT
        banana_rect.y += VEL_OBJECT
        bomb_rect.y += VEL_OBJECT
        cookies_rect.y += VEL_OBJECT
        shake_rect.y += VEL_OBJECT


    def apple_coor(self, apple_rect, banana_rect, bomb_rect, cookies_rect, shake_rect, checker):
        if checker == 1:
            apple_rect.x = random.randrange(60, 540)
            apple_rect.y = 30
        elif checker == 2:
            banana_rect.x = random.randrange(60, 540)
            banana_rect.y = 30
        elif checker == 3:
            bomb_rect.x = random.randrange(60, 540)
            bomb_rect.y = 30
        elif checker == 4:
            cookies_rect.x = random.randrange(60, 540)
            cookies_rect.y = 30
        elif checker == 5:
            shake_rect.x = random.randrange(60, 540)
            shake_rect.y = 30


    def object_check(self,head,border_down, apple_rect, banana_rect, bomb_rect, cookies_rect, shake_rect):
        global LIVE_COUNTER
        global SCORE

        if apple_rect.colliderect(border_down):
            LIVE_COUNTER -= 1
            return 1
        elif banana_rect.colliderect(border_down):
            LIVE_COUNTER -= 1
            return 2
        elif cookies_rect.colliderect(border_down):
            LIVE_COUNTER -= 1
            return 4
        elif shake_rect.colliderect(border_down):
            LIVE_COUNTER -= 1
            return 5
        elif bomb_rect.colliderect(border_down):
            self.apple_coor(apple_rect, banana_rect, bomb_rect,cookies_rect,shake_rect, 3)

        if head.colliderect(apple_rect):
            SCORE += 1
            return 1
        elif head.colliderect(banana_rect):
            SCORE += 1
            return 2
        elif head.colliderect(bomb_rect):
            LIVE_COUNTER -= 1
            return 3
        elif head.colliderect(cookies_rect):
            SCORE += 1
            return 4
        elif head.colliderect(shake_rect):
            SCORE += 1
            return 5
        else:
            return 0
    def starting_positions(self):
        a = random.random()
        random.seed(a)
        return random.randint(60,540)


class final_win_GUI():
    def __init__(self, dif):
        self.dif = dif
    def main(self):
        score = Tk()
        score.geometry('300x300')
        score.title('koniec')
        score.config(background='white')
        label = Label(score, text="Wynik punktowy:", font=('Arial', 20), fg="black", bg = "white")
        label.place(x=50, y=20)

        point_label = Label(score, text = str(SCORE), font= ('Arial', 20), fg = 'black', bg = 'white')
        point_label.place(x=145, y=50)

        play_again_but = Button(score, text="Zagraj ponownie", font=('Arial', 20), fg='white', bg="black",  command = lambda : self.close_func(score,0) )
        play_again_but.place(x = 35 , y = 130)

        quit_but = Button(score, text = "Wyjdź z gry" , font = ('Arial',20) , fg = 'white' , bg = 'black', command = lambda : self.close_func(score,1))
        quit_but.place(x = 70, y = 180)
        score.mainloop()
    def close_func(self, score, checker):
        if checker == 0:
            score.destroy()
            cat(self.dif).main_loop()
        else:
            score.destroy()
            exit()



