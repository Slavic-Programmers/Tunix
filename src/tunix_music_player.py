import pygame

class TunixMusicPlayer:
    def __init__(self) -> None:
        pygame.mixer.init()
        self.__playing_path: str = ''
    
    
    def load(self, path: str) -> None:
        self.__playing_path = path
        pygame.mixer.music.load(self.__playing_path)
    
    
    def play(self) -> None:
        pygame.mixer.music.play(loops=0, start=0, fade_ms=0)
        
        
    def stop(self) -> None:
        pygame.mixer.music.stop()
        
    
    def pause(self) -> None:
        pygame.mixer.music.pause()
        
    
    def unpause(self) -> None:
        pygame.mixer.music.unpause()
        

    def is_playing(self) -> bool:
        return pygame.mixer.music.get_busy()