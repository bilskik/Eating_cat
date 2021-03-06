import tkinter
from tkinter import *
from cat_module import *
from PIL import Image, ImageTk




class main_page_GUI():
    def __init__(self, difficulty):
        self.difficulty = difficulty
    def set_up(self):
        window = Tk()
        window.geometry("800x600")
        window.title("cat.exe")
        back_photo = (Image.open('images/cat_background.png'))
        resized_back_photo = back_photo.resize((800,600), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_back_photo)
        main_label = Label(window, image = new_image)
        main_label.place(x = 0 , y = 0)


        self.buttons(window, new_image)
        window.mainloop()
   
    def buttons(self,window, new_image):
        game_but = Button(window, text = "Nowa gra", font=('Arial',40)  ,bg = 'black',  fg = 'white',
                          command = lambda: cat(self.difficulty).main_loop())
        game_but.place(x= 290 , y = 200)

        options_but = Button(window, text = "Opcje", font=('Arial',40) , bg = "black" ,fg = 'white',
                             command = lambda: self.create_options())
        options_but.place(x= 340 , y = 300)

        quit_but = Button(window, text = "Wyjście", font=('Arial',40) , bg = "black" ,fg = 'white',
                          command = lambda: window.destroy())
        quit_but.place(x= 315 , y = 400)

    def create_options(self):
        options_win = Toplevel()
        options_win.geometry('400x300')
        new_image = tkinter.PhotoImage(file='images/options.png')
        main_canvas = Canvas(options_win, width=400, height=300)
        main_canvas.pack()
        main_canvas.create_image(138,160,image=new_image)
        main_canvas.image = new_image
        options_win.title('opcje')

        back_button = Button(options_win, text = "Powrót", font = ('Arial', 20), bg = 'black', fg = 'white',
                             command  = lambda : options_win.destroy())
        back_button.place(x = 150, y = 0)

        label_difficulty = Label(options_win,text = 'Poziom trudności:',
                                 font = ('Arial', 20), bg = 'white', fg = 'black')
        label_difficulty.place(x = 90, y = 70)

        mode_button = Button(options_win, text="łatwy", font=('Arial', 20), bg='black', fg='white',
                             command=lambda: self.changeText(mode_button))
        mode_button.place(x = 150, y = 110)
        
    def changeText(self, mode_button):

        if mode_button['text'] == 'łatwy':
            self.difficulty = 'hard'
            mode_button['text'] = 'trudny'
        else:
            self.difficulty = 'easy'
            mode_button['text'] = 'łatwy'

def main():
    difficulty = 'easy'
    main_win = main_page_GUI(difficulty)
    main_win.set_up()




if __name__ == "__main__":
        main()
