from tunix import Tunix
from tunix_music_player import TunixMusicPlayer
import os


def set_path() -> None:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main() -> None:
    set_path()
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
    
    tunix = Tunix()
    tmp = TunixMusicPlayer()
    tunix.run()
    #tmp.load('./music/song1.mp3')
    #tmp.play()
    #input('Exit: ')
    

if __name__ == "__main__":
    main()