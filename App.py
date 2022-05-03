import os
from tkinter import *
from utils.utils import *
from random import randint
from threading import Thread


class App(Tk):
    __width__ = 1920
    __height__ = 1080
    __indent_x__ = 0
    __indent_y__ = 50

    EYE = os.path.join('assets', 'eye.gif')

    def __init__(self):
        super().__init__()

        self.eye_state = 'opened'
        self.on_left_eye = self.on_right_eye = self.focused = False
        self.x = self.__indent_x__
        self.y = self.__indent_y__

        self.geometry(
            f'{self.__width__}x{self.__height__}+{self.__indent_x__}+{self.__indent_y__}')

        self.config(bg='#bbbbbb')

        self.lift()
        self.overrideredirect(1)
        self.wm_attributes("-topmost", True)
        self.wm_attributes("-transparentcolor", "#bbbbbb")

        # monitoring events
        self.bind('<Motion>', self.cursor_position)

        # self.attributes('-alpha', 0)
        # self.wm_attributes("-disabled", True)

    def cursor_position(self, event):
        x, y = event.x, event.y

        if x in range(0, 95) and y in range(65, 150):
            self.on_left_eye = True
            self.set_state('left_closed')

        else:
            self.on_left_eye = False

        if x in range(157, 253) and y in range(65, 150):
            self.on_right_eye = True
            self.set_state('right_closed')
        else:
            self.on_right_eye = False

    def set_state(self, state: str):
        """

        closed
        opened
        left_closed
        right_closed

        """

        self.eye_state = state

    def change_position(self, x, y):
        self.x, self.y = x, y

        self.geometry(f'+{x}+{y}')

    def get_eye(self) -> list:
        return frames_from_video(self.EYE)

    def get_opened_eyes(self) -> str:
        return os.path.join('assets', 'opened.png')

    def get_closed_eyes(self) -> str:
        return os.path.join('assets', 'closed.png')

    def get_left_closed(self) -> str:
        return os.path.join('assets', 'left_closed.png')

    def get_right_closed(self) -> str:
        return os.path.join('assets', 'right_closed.png')
