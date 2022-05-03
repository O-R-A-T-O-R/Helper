from tkinter import *

from App import App
from utils.utils import *

from threading import Thread
from random import randint
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
society = create_circle(0, 0, items_radius, ROOT)

# menu items position
coords(ROOT, society, screen_width // 2 - items_radius,
       500, items_radius * 2, items_radius * 2)

# main body position
coords(ROOT, main_body, screen_width // 2 -
       body_radius, 0, body_radius * 2, body_radius * 2)

# eyes field
eye = Label(ROOT, compound='top', width=296, height=150)
ROOT.create_window(245 + screen_width // 2 - body_radius, 190, window=eye,)
# ----------------------------


# ------ paths of eyes images ------
opened_eyes = APP.get_opened_eyes()
closed_eyes = APP.get_closed_eyes()
left_closed_eye = APP.get_left_closed()
right_closed_eye = APP.get_right_closed()
# ----------------------------


# ------ eye animations ------
def animate_eye(label: Label):
    """ Eye Animation (constant blinking) """

    while True:
        if not APP.on_left_eye and not APP.on_right_eye:
            set_image(label, opened_eyes)
            APP.set_state('opened')

        sleep(randint(3, 5))

        set_image(label, closed_eyes)
        APP.set_state('closed')

        sleep(.3)


def on_eye(label: Label):
    while True:
        if APP.on_left_eye:
            # cursor located on left eye
            set_image(label, left_closed_eye)

        elif APP.on_right_eye:
            # cursor located on right eye
            set_image(label, right_closed_eye)

        else:
            if APP.eye_state in ('left_closed', 'right_closed'):
                set_image(label, opened_eyes)

        sleep(.05)


eye_animation = Thread(target=animate_eye, args=(eye, ), daemon=True)
on_eye_animation = Thread(target=on_eye, args=(eye, ), daemon=True)

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
