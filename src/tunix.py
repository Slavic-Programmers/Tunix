import tkinter
import customtkinter
from settings import *

class Tunix:
    def __init__(self) -> None:
        customtkinter.set_appearance_mode(SYSTEM_MODE)
        
        self.__app = customtkinter.CTk()
        self.__app.geometry('400x400')
        self.__app.title('Tunix')
        
        self.__main_frame = customtkinter.CTkFrame(master=self.__app)
        self.__main_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.__appearance_mode_chooser_label = customtkinter.CTkLabel(master=self.__main_frame, text="Appearance Mode:", justify=customtkinter.CENTER, anchor=customtkinter.SW)
        self.__appearance_mode_chooser_label.pack(pady=10, padx=10)
        
        self.__appearance_mode_option_menu = customtkinter.CTkOptionMenu(master=self.__main_frame, values=[SYSTEM_MODE, LIGHT_MODE, DARK_MODE])
        self.__appearance_mode_option_menu.pack(pady=10, padx=10)
        self.__appearance_mode_option_menu.set("Appearance Mode")
        

    def run(self) -> None:
        self.__app.mainloop()