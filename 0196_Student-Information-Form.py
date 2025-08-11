import customtkinter as ctk
from pyexpat.errors import messages
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

ctk.set_appearance_mode("light")

app = ctk.CTk()
app.geometry("500x600")
app.title("Student Information Form")

ctk.CTkLabel(app, text="Name:", font=("Helvetica", 15)).pack(pady=(20, 5))
user_name = ctk.CTkEntry(app, placeholder_text="Enter your name", width=300, height=35, corner_radius=15)
user_name.pack(pady=5)

ctk.CTkLabel(app, text="Father Name:", font=("Helvetica", 15)).pack(pady=(10, 5))
father_name = ctk.CTkEntry(app, placeholder_text="Enter father's name", width=300, height=35, corner_radius=15)
father_name.pack(pady=5)

ctk.CTkLabel(app, text="Age:", font=("Helvetica", 15)).pack(pady=(10, 5))
user_age = ctk.CTkEntry(app, placeholder_text="Enter your age", width=300, height=35, corner_radius=15)
user_age.pack(pady=5)

ctk.CTkLabel(app, text="Qualification:", font=("Helvetica", 15)).pack(pady=(10, 5))
user_qualification = ctk.CTkEntry(app, placeholder_text="Enter qualification", width=300, height=35, corner_radius=15)
user_qualification.pack(pady=5)

ctk.CTkLabel(app, text="Experience:", font=("Helvetica", 15)).pack(pady=(10, 5))
user_experience = ctk.CTkEntry(app, placeholder_text="Enter experience", width=300, height=35, corner_radius=15)
user_experience.pack(pady=5)

def submit():
    name=user_name.get()
    father=father_name.get()
    age=user_age.get()
    qualification=user_qualification.get()
    experience=user_experience.get()

    if not name:
        ctk.CTkMessagebox(title="Error",message="Please enter your name")
        return

    name_set="".join(c for c in name if c.isalnum() or c in (" ","-","_")).strip()
    pdf_filename=f"{name_set}.pdf"

    c = canvas.Canvas(pdf_filename,pagesize=letter)
    c.setFont("Helvetica", 15)
    c.drawString(100,650,f"Name:{name}")
    c.drawString(100,630, f"Father Name:{father}")
    c.drawString(100,610,f"Age:{age}")
    c.drawString(100, 590, f"Experience:{experience}")
    c.drawString(100, 570, f"Qualification:{qualification}")
    c.save()


submit_btn = ctk.CTkButton(app, text="Submit", width=150, height=40, corner_radius=20, command=submit)
submit_btn.pack(pady=20)

app.mainloop()