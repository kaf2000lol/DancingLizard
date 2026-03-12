import tkinter as tk
import random
from PIL import Image, ImageTk

dx = 3
dy = 3
@@ -8,26 +9,28 @@
root.overrideredirect(True)
root.attributes("-topmost", True)

# load image with Pillow
img = Image.open("Lizard.gif")
gif = ImageTk.PhotoImage(img)

label = tk.Label(root, image=gif)
label.pack()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = random.randint(0, screen_width - img.width)
y = random.randint(0, screen_height - img.height)

def move():
    global x, y, dx, dy

    x += dx
    y += dy

    if x <= 0 or x >= screen_width - img.width:
        dx = -dx
    if y <= 0 or y >= screen_height - img.height:
        dy = -dy

    root.geometry(f"+{x}+{y}")
