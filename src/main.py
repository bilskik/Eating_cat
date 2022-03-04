from tkinter import *


class main_page_GUI():
    def __init__(self):
        pass
    def set_up(self):
        window = Tk()
        window.geometry("800x600")
        window.title("Snake.exe")
        window.config(background="black")
        label = Label(window, text="SNAKE", font=('Arial',40), fg = "green", bg = "black")
        label.place(x = 320, y = 25)

        photo=PhotoImage(file= "2.png")
        photo_label = Label(image=photo)
        photo_label.place(x =350 , y = 100)
        self.buttons(window)
        window.mainloop()
   
    def buttons(self,window):
        game_but = Button(window, text = "Nowa gra", font=('Arial',40) , bg = "black" ,fg = 'white', activebackground= 'black', activeforeground='white' , command = lambda: snake_gui(window).setup())
        game_but.place(x= 290 , y = 200)

        options_but = Button(window, text = "Opcje", font=('Arial',40) , bg = "black" ,fg = 'white', activebackground= 'black', activeforeground='white', command = lambda: self.create_options)
        options_but.place(x= 340 , y = 300)

        quit_but = Button(window, text = "Wyjście", font=('Arial',40) , bg = "black" ,fg = 'white', activebackground= 'black', activeforeground='white' , command = lambda: window.destroy())
        quit_but.place(x= 315 , y = 400)

    def create_options(self):
        new_window = Toplevel()

class snake_gui():
    def __init__(self, window):
        self.window = window
    def setup(self):
        new_window = Toplevel()



def main():
    main_win = main_page_GUI()
    main_win.set_up()
    


if __name__ == "__main__":
        main()
