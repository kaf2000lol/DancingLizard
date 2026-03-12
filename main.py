import tkinter as tk
import random
from PIL import Image, ImageTk, ImageSequence

dx = 3
dy = 3

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)

# load image with Pillow
img = Image.open("Lizard.gif")
frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(img)]

label = tk.Label(root, image=frames[0])
label.pack()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = random.randint(0, screen_width - img.width)
y = random.randint(0, screen_height - img.height)

frame_index = 0

def update():
    global x, y, dx, dy, frame_index

    label.config(image=frames[frame_index])
    frame_index = (frame_index + 1) % len(frames)
    
    x += dx
    y += dy

    if x <= 0 or x >= screen_width - img.width:
        dx = -dx
    if y <= 0 or y >= screen_height - img.height:
        dy = -dy

    root.geometry(f"+{x}+{y}")

    root.after(50, update)

update()
root.mainloop()
