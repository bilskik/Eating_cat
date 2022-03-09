from tkinter import *
from cat_module import *
from PIL import Image, ImageTk


difficulty = ' '

class main_page_GUI():
    def __init__(self):
        pass
    def set_up(self):
        window = Tk()
        window.geometry("800x600")
        window.title("cat.exe")
        back_photo = (Image.open('cat_background.png'))
        resized_back_photo = back_photo.resize((800,600), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_back_photo)
        main_label = Label(image = new_image)
        main_label.place(x = 0 , y = 0)


        self.buttons(window, new_image)
        window.mainloop()
   
    def buttons(self,window, new_image):
        game_but = Button(window, text = "Nowa gra", font=('Arial',40)  ,bg = 'black',  fg = 'white',  command = lambda: cat().main_loop())
        game_but.place(x= 290 , y = 200)

        options_but = Button(window, text = "Opcje", font=('Arial',40) , bg = "black" ,fg = 'white', command = lambda: self.create_options())
        options_but.place(x= 340 , y = 300)

        quit_but = Button(window, text = "Wyjście", font=('Arial',40) , bg = "black" ,fg = 'white',  command = lambda: window.destroy())
        quit_but.place(x= 315 , y = 400)

    def create_options(self):
        global difficulty
        options_win = Toplevel()
        options_win.geometry('400x300')
        options_win.config(background='grey')
        options_win.title('opcje')

        back_button = Button(options_win, text = "Powrót", font = ('Arial', 20), bg = 'black', fg = 'white',
                             command  = lambda : options_win.destroy())
        back_button.place(x = 150, y = 0)

        label_difficulty = Label(options_win,text = 'Poziom trudności:' ,
                                 font = ('Arial', 20), bg = 'black', fg = 'white')

        label_difficulty.place(x = 90, y = 70)

        print(difficulty)
        mode_button = Button(options_win, text="łatwy", font=('Arial', 20), bg='black', fg='white',
                             command=lambda: self.changeText(mode_button))


        mode_button.place(x = 150, y = 110)
        
    def changeText(self, mode_button):
        global difficulty
        if mode_button['text'] == 'łatwy':
            difficulty = 'hard'
            mode_button['text'] = 'trudny'
        else:
            difficulty = 'easy'
            mode_button['text'] = 'łatwy'











def main():
    main_win = main_page_GUI()
    main_win.set_up()
    


if __name__ == "__main__":
        main()
