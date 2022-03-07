from tkinter import *
from cat_module import cat

class main_page_GUI():
    def __init__(self):
        pass
    def set_up(self):
        window = Tk()
        window.geometry("800x600")
        window.title("cat.exe")
        window.config(background="black")
        label = Label(window, text="Jedzacy kot", font=('Arial',40), fg = "green", bg = "black")
        label.place(x = 280, y = 25)

        photo=PhotoImage(file= "2.png")
        photo_label = Label(image=photo)
        photo_label.place(x =350 , y = 100)
        self.buttons(window)
        window.mainloop()
   
    def buttons(self,window):
        game_but = Button(window, text = "Nowa gra", font=('Arial',40) , bg = "black" ,fg = 'white', activebackground= 'black', activeforeground='white' , command = lambda: cat(window).main_loop())
        game_but.place(x= 290 , y = 200)

        options_but = Button(window, text = "Opcje", font=('Arial',40) , bg = "black" ,fg = 'white', activebackground= 'black', activeforeground='white', command = lambda: self.create_options)
        options_but.place(x= 340 , y = 300)

        quit_but = Button(window, text = "Wyjście", font=('Arial',40) , bg = "black" ,fg = 'white', activebackground= 'black', activeforeground='white' , command = lambda: window.destroy())
        quit_but.place(x= 315 , y = 400)

    def create_options(self):
        new_window = Toplevel()





def main():
    main_win = main_page_GUI()
    main_win.set_up()
    


if __name__ == "__main__":
        main()
