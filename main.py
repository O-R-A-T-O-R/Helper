from tkinter import *
from App import App
from utils.utils import * 
from threading import Thread

APP = App()

# ------ scene objects ------
ROOT = Canvas (
                APP,
                bg='#bbbbbb',
                height=620,
                width=620,
                bd=0,
                highlightthickness=0,
                relief='ridge'
)
ROOT.pack()

create_circle(300, 300, 300, ROOT)

eye = Label(ROOT, compound='top', width=450, height=450)

ROOT.create_window(300, 300, window=eye)
# ----------------------------

# ------ eye animation ------
eye_frames = APP.get_eye()

gif_player = Thread(target=play_gif, args=(eye, eye_frames), daemon=True)
gif_player.start()
# ----------------------------


APP.title('Let me die')
APP.mainloop()
