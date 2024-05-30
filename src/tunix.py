from settings import *
from tunix_app import TunixApp

class Tunix:
    def __init__(self) -> None:
        self.__app = TunixApp()
    
    
    def run(self) -> None:
        self.__app.mainloop()