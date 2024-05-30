import tkinter
import customtkinter
from settings import *

class Tunix:
    def __init__(self) -> None:
        self.__root = tkinter.Tk()
        self.__root.geometry('400x400')
        self.__root.title('Tunix')
        customtkinter.set_appearance_mode(SYSTEM_MODE)
        
        
        
        

    def run(self) -> None:
        self.__root.mainloop()