import tkinter
import customtkinter
from settings import *

class Tunix:
    def __init__(self) -> None:
        self.__app = customtkinter.CTk()
        self.__app.geometry('400x400')
        self.__app.title('Tunix')
        customtkinter.set_appearance_mode(SYSTEM_MODE)
        
        
        
        

    def run(self) -> None:
        self.__app.mainloop()