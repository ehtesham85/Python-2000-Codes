# Adding image

import tkinter as tk
from PIL import Image, ImageTk

root=tk.Tk()
root.title("Image")

img = Image.open("image-1.jpg")
img = img.resize((400, 400))
photo = ImageTk.PhotoImage(img)

label = tk.Label(root, image=photo)
label.pack()

root.mainloop()
