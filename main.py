import tkinter as tk
import random

dx = 3
dy = 3

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)

gif = tk.PhotoImage(file="Lizard.gif")

label = tk.Label(root, image=gif)
label.pack()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = random.randint(0, screen_width - gif.width())
y = random.randint(0, screen_height - gif.height())

def move():
    global x, y, dx, dy

    x += dx
    y += dy

    if x <= 0 or x >= screen_width - gif.width():
        dx = -dx
    if y <= 0 or y >= screen_height - gif.height():
        dy = -dy

    root.geometry(f"+{x}+{y}")
    root.after(20, move)

move()
root.mainloop()
