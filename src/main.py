from tunix import Tunix
from tunix_music_player import TunixMusicPlayer

def main() -> None:
    tunix = Tunix()
    tmp = TunixMusicPlayer()
    tmp.load('./music/song1.mp3')
    tmp.play()
    

if __name__ == "__main__":
    main()