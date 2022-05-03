from time import sleep
import tkinter
from PIL import Image, ImageTk
import cv2
from random import randint


def frames_from_video(video_path: str) -> list:

    vidcap, count = cv2.VideoCapture(video_path), 0
    success, image = vidcap.read()
    frames = list()

    while success:
        success, frame = vidcap.read()

        if frame is not None:
            frames.append(frame)

    return frames


def create_circle(x, y, r, canvas):
    x0, y0, x1, y1 = x - r, y - r, x + r, y + r

    return canvas.create_oval(x0, y0, x1, y1, fill='black')


def play_gif(label, gif: list):
    """

    label : tkinter.Label
    gif : list of frames

    This function plays frames infinity times

    """
    for frame in gif:
        init_image = Image.fromarray(frame)

        width, height = init_image.width, init_image.height

        init_image = init_image.resize(
            (width // 2, height // 2), Image.ANTIALIAS)
        frame_image = ImageTk.PhotoImage(init_image)

        label.config(image=frame_image, height=height //
                     2.5, width=width // 2.5)
        label.image = frame_image

        sleep(.05)

    play_gif(label, gif)


def set_image(label: tkinter.Label, image_path: str):
    image = Image.open(image_path)
    frame = ImageTk.PhotoImage(image)

    width, height = image.width, image.height

    label.config(image=frame)
    label.image = frame


def animate_eye(app: tkinter.Tk, label: tkinter.Label):
    """ Eye Animation (constant blinking) """

    while True:
        if not app.on_left_eye and not app.on_right_eye:
            set_image(label, app.get_opened_eyes())
            app.set_state('opened')

        sleep(randint(3, 5))

        set_image(label, app.get_closed_eyes())
        app.set_state('closed')

        sleep(.3)


def on_eye(app: tkinter.Tk, label: tkinter.Label):
    while True:
        if app.on_left_eye:
            # cursor located on left eye
            set_image(label, app.get_left_closed())

        elif app.on_right_eye:
            # cursor located on right eye
            set_image(label, app.get_right_closed())

        else:
            if app.eye_state in ('left_closed', 'right_closed'):
                set_image(label, app.get_opened_eyes())

        sleep(.05)



def coords(canvas: tkinter.Canvas, obj, x, y, width, height):
    canvas.coords(obj, x, y, x + width, y + height)


def smoothed_move(canvas: tkinter.Canvas, obj, x, y, width, height, cur_x, cur_y):
    distance_x, distance_y = abs(cur_x - x), abs(cur_y - y)    
    movement_range = max(distance_x, distance_y) // 5
    step_x, step_y = distance_x // movement_range, distance_y // movement_range

    for i in range(movement_range):
        coords(canvas, obj, step_x * i, step_y * i, width, height)

        sleep(.025)
