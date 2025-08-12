import tkinter as tk

root = tk.Tk()
root.title("Checkbox")

check_var = tk.BooleanVar()
tk.Checkbutton(root, text="CheckBox", variable=check_var).pack()

root.mainloop()

