from time import sleep
from PIL import Image, ImageTk
import cv2

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


def play_gif(label, gif : list):
    """
    
    label : tkinter.Label
    gif : list of frames

    This function plays frames infinity times

    """
    for frame in gif:
        init_image = Image.fromarray(frame)

        width, height = init_image.width, init_image.height

        init_image = init_image.resize((width // 2, height // 2), Image.ANTIALIAS)
        frame_image = ImageTk.PhotoImage(init_image)

        label.config(image=frame_image, height=height // 2.5, width=width // 2.5)
        label.image = frame_image

        sleep(.05)

    play_gif(label, gif)
