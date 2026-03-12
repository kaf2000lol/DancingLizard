import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import random

root = tk.Tk()

# remove window border
root.overrideredirect(True)

# always on top
root.attributes("-topmost", True)

# transparent background 
root.config(bg="white")
root.wm_attributes("-transparentcolor", "white")

# load gif
gif = Image.open("Lizard.gif")

frames = [ImageTk.PhotoImage(frame.copy())
          for frame in ImageSequence.Iterator(gif)]

label = tk.Label(root, bd=0, bg="white")
label.pack()

frame_index = 0

# screen size
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

x = random.randint(0, screen_w - 200)
y = random.randint(0, screen_h - 200)

dx = 5
dy = 0


def update_frame():
    global frame_index
    label.config(image=frames[frame_index])
    frame_index = (frame_index + 1) % len(frames)
    root.after(50, update_frame)


def move():
    global x, y, dx, dy

    x += dx
    y += dy

    # bounce off edges
    if x < 0 or x > screen_w - 150:
        dx = -dx

    if y < 0 or y > screen_h - 150:
        dy = -dy

    root.geometry(f"+{x}+{y}")
    root.after(30, move)


update_frame()
move()

root.mainloop()
