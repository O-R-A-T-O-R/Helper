from tkinter import Canvas
from time import sleep

class Item:
    def __init__(
            self,
            x: int,
            y: int,
            width: int,
            height: int,
            canvas: Canvas, 
            model: any):

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.canvas = canvas  # canvas parent
        self.model = model    # object like create_oval

    def coords(self, x, y):
        self.canvas.coords(self.model, x, y, x + self.width, y + self.height)

        self.x, self.y = x, y

    def smoothed_coords(self, x, y):
        dis_x, dis_y = x - self.x, y - self.y # distances
        step_x, step_y = dis_x // 29, dis_y // 29

        init_x, init_y = self.x, self.y

        for i in range(1, 30):
            self.coords(init_x + step_x * i, init_y + step_y * i)

            sleep(.01)