import tkinter
import customtkinter
from settings import *

class TunixMainPage(customtkinter.CTkFrame):
    def __init__(self, master, change_color_theme) -> None:
        super().__init__(master=master)
        
        self.__appearance_mode_chooser_label = customtkinter.CTkLabel(master=self, text="Appearance Mode:", justify=customtkinter.CENTER, anchor=customtkinter.SW)
        self.__appearance_mode_chooser_label.pack(pady=10, padx=10)
        
        self.__appearance_mode_option_menu = customtkinter.CTkOptionMenu(master=self, values=[SYSTEM_MODE, LIGHT_MODE, DARK_MODE], command=self.__appearance_mode_option_menu_callback)
        self.__appearance_mode_option_menu.pack(pady=10, padx=10)
        self.__appearance_mode_option_menu.set("Appearance Mode")
        
        self.__color_theme_chooser_label = customtkinter.CTkLabel(master=self, text="Color Theme:", justify=customtkinter.CENTER, anchor=customtkinter.SW)
        self.__color_theme_chooser_label.pack(pady=10, padx=10)
        
        self.__color_theme_option_menu = customtkinter.CTkOptionMenu(master=self, values=[BLUE, GREEN, DARK_BLUE], command=change_color_theme)
        self.__color_theme_option_menu.pack(pady=10, padx=10)
        self.__color_theme_option_menu.set("Color Theme")
        

    def __appearance_mode_option_menu_callback(self, choice) -> None:
        customtkinter.set_appearance_mode(choice)

