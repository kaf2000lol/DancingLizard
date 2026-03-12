import tkinter as tk
from PIL import Image, ImageTk
import random

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)

# load sprite sheet
sheet = Image.open("Lizard.gif")

# frame size (you must adjust this)
FRAME_WIDTH = 128
FRAME_HEIGHT = 128

frames = []

# calculate number of frames in sheet
sheet_width, sheet_height = sheet.size
cols = sheet_width // FRAME_WIDTH
rows = sheet_height // FRAME_HEIGHT

# slice frames from sheet
for y in range(rows):
    for x in range(cols):
        box = (
            x * FRAME_WIDTH,
            y * FRAME_HEIGHT,
            (x + 1) * FRAME_WIDTH,
            (y + 1) * FRAME_HEIGHT
        )
        frame = sheet.crop(box)
        frames.append(ImageTk.PhotoImage(frame))

label = tk.Label(root)
label.pack()

# screen size
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

x = random.randint(0, screen_w - FRAME_WIDTH)
y = random.randint(0, screen_h - FRAME_HEIGHT)

dx = 3
dy = 3

frame_index = 0

def update():
    global x, y, dx, dy, frame_index

    # animate frames
    label.config(image=frames[frame_index])
    frame_index = (frame_index + 1) % len(frames)

    # move lizard
    x += dx
    y += dy

    if x <= 0 or x >= screen_w - FRAME_WIDTH:
        dx = -dx
    if y <= 0 or y >= screen_h - FRAME_HEIGHT:
        dy = -dy

    root.geometry(f"+{x}+{y}")

    root.after(60, update)

update()
root.mainloop()
