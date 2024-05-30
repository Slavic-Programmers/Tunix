import tkinter
import customtkinter
from tunix_main_page import TunixMainPage
from tunix_music_player import TunixMusicPlayer
from settings import *

class TunixApp(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.__music_player = TunixMusicPlayer()
        self.__music_player.load('./music/song1.mp3')

        
        customtkinter.set_appearance_mode(SYSTEM_MODE)
        customtkinter.set_default_color_theme(BLUE)
        self.geometry("400x400")
        self.title("Tunix")
        
        self.current_ui = []
        self.main_content = TunixMainPage(self, self.__music_player, self.change_color_theme)
        self.main_content.pack(pady=10, padx=10, expand=True, fill=customtkinter.BOTH)
        self.current_ui.append(self.main_content)     
    
    
    def change_color_theme(self, choice: str) -> None:
        customtkinter.set_default_color_theme(choice.lower())
        self.reset_current_ui()
    
    
    def reset_current_ui(self) -> None:
        for widget in self.current_ui:
            widget.destroy()
        self.main_content = TunixMainPage(self, self.__music_player, self.change_color_theme)
        self.main_content.pack(pady=10, padx=10, expand=True, fill=customtkinter.BOTH)
        self.current_ui.append(self.main_content)