import tkinter
import customtkinter

class Tunix:
    def __init__(self) -> None:
        self.__root = tkinter.Tk()
        self.__root.geometry('400x400')
        self.__root.title('Tunix')
        
        button = customtkinter.CTkButton(master=self.__root, corner_radius=10)
        button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def run(self) -> None:
        self.__root.mainloop()