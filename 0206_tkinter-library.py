import tkinter as tk

def say_Hello():
   label_result.config(text="Hello Man")


root = tk.Tk()
root.title("My Application")
root.geometry("300x200")

label = tk.Label(root, text="Press the Button", font=("Arial", 18))
label.pack(pady=10)

btn = tk.Button(root, text="Say Hello", command=say_Hello)
btn.pack(pady=10)

label_result=tk.Label(root, text="", font=("Arial", 18))
label_result.pack(pady=10)

root.mainloop()

