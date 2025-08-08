import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app=ctk.CTk()
app.geometry("600x400")
app.title("Task Manager")

label=ctk.CTkLabel(app, text="Task Manager", font=("Arial",20))
label.pack(pady=20)

label=ctk.CTkLabel(app, text="Enter Your Task : ", font=("Arial",20))
label.pack(pady=10)

entry=ctk.CTkEntry(app, placeholder_text="Enter here", width=300, height=40, border_width=2, corner_radius=10)
entry.pack(pady=10)

label_result=ctk.CTkLabel(app, text="", font=("Arial",20))
label_result.pack(pady=10)

def submit():
   user_input=entry.get()
   label_result.configure(text=user_input)


button=ctk.CTkButton(app, text="Add Task", font=("Arial",20), width=200, height=40, corner_radius=8, command=submit)
button.pack(pady=10)







app.mainloop()
