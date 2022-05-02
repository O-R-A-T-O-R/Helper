import os
from tkinter import Tk
from utils.utils import *

class App(Tk):
    __width__ = 1920
    __height__ = 1080
    __indent_x__ = 0
    __indent_y__ = 50

    EYE = os.path.join('assets', 'eye.gif')

    def __init__(self):
        super().__init__()

        self.geometry(
            f'{self.__width__}x{self.__height__}+{self.__indent_x__}+{self.__indent_y__}')

        self.config(bg='#bbbbbb')

        self.overrideredirect(1)
        self.lift()
        self.wm_attributes("-topmost", True)
        # self.wm_attributes("-disabled", True)

        self.wm_attributes("-transparentcolor", "#bbbbbb")

        # self.attributes('-alpha', 0)

    def get_eye(self) -> list:
        return frames_from_video(self.EYE)