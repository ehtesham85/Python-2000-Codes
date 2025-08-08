import customtkinter as ctk

ctk.set_appearance_mode("light")

app=ctk.CTk()
app.geometry("500x400")
app.title("Input Box")

label=ctk.CTkLabel(app,text="Enter your Name : ",font=("Times",20))
label.pack(pady=20)

entry=ctk.CTkEntry(app,width=250,font=("Arial",15))
entry.pack(pady=10)

label_result=ctk.CTkLabel(app,font=("Helvetica",20))
label_result.pack(pady=10)

def submit():
     user_input=entry.get()
     label_result.configure(text=user_input)

button=ctk.CTkButton(app,width=170,text="Submit",command=submit)
button.pack(pady=10)


app.mainloop()

