import tkinter as tk
import random

# movement speed
dx = 3
dy = 3

root = tk.Tk()

# remove window borders
root.overrideredirect(True)

# keep window above others
root.attributes("-topmost", True)

# transparent background
root.wm_attributes("-transparentcolor", "white")

# load gif
gif = tk.PhotoImage(file="Lizard.gif")

label = tk.Label(root, image=gif, bg="white")
label.pack()

# screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# starting position
x = random.randint(0, screen_width - gif.width())
y = random.randint(0, screen_height - gif.height())

def move():
    global x, y, dx, dy

    x += dx
    y += dy

    # bounce off screen edges
    if x <= 0 or x >= screen_width - gif.width():
        dx = -dx
    if y <= 0 or y >= screen_height - gif.height():
        dy = -dy

    root.geometry(f"+{x}+{y}")
    root.after(20, move)

move()

root.mainloop()
