from tkinter import *

from App import App
from utils.utils import *
from models import Item

from threading import Thread
from time import sleep

APP = App()

# ------ scene objects ------
screen_width = APP.winfo_screenwidth()
screen_height = APP.winfo_screenheight()

body_radius = 220
items_radius = 50

ROOT = Canvas(
    APP,
    bg='#bbbbbb',
    height=screen_height,
    width=screen_width,
    bd=0,
    highlightthickness=0,
    relief='ridge'
)
ROOT.pack()

main_body = create_circle(0, 0, body_radius, ROOT)
society_model = create_circle(0, 0, items_radius, ROOT)

society = Item(0, 500, items_radius * 2, items_radius * 2, ROOT, society_model)


# menu items position
society.coords(screen_width // 2 - items_radius, 500)

# main body position
coords(ROOT, main_body, screen_width // 2 -
       body_radius, 0, body_radius * 2, body_radius * 2)


# eyes field
eye = Label(ROOT, compound='top', width=296, height=150)
ROOT.create_window(245 + screen_width // 2 - body_radius, 190, window=eye,)
# ----------------------------


# ------ mouse/cursor events ------
def enter(event):
    some = Thread(target=society.smoothed_coords, args=(society.x, 500), daemon=True)
    some.start()

def leave(event):
    some_ = Thread(target=society.smoothed_coords, args=(society.x, 0), daemon=True)
    some_.start()

APP.bind('<FocusIn>', enter)
APP.bind('<FocusOut>', leave)
# ----------------------------


# ------ paths of eyes images ------
opened_eyes = APP.get_opened_eyes()
closed_eyes = APP.get_closed_eyes()
left_closed_eye = APP.get_left_closed()
right_closed_eye = APP.get_right_closed()
# ----------------------------


# ------ eye animations ------
eye_animation = Thread(target=animate_eye, args=(APP, eye), daemon=True)
on_eye_animation = Thread(target=on_eye, args=(APP, eye), daemon=True)

on_eye_animation.start()
eye_animation.start()
# ----------------------------


# ------ movement animation ------
def animate_movement():
    # todo : smoothed randomized movement on screen
    while True:
        x, y = APP.x, APP.y
        APP.change_position(x + 5, y + 5)

        sleep(.025)


movement_animation = Thread(target=animate_movement,
                            daemon=True, name='Animation-Movement')
# movement_animation.start()
# ----------------------------


APP.title('Let me die')
APP.mainloop()
