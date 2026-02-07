import tkinter as tk
from datetime import datetime

app = tk.Tk()
app.geometry("800x350")
app.title("Age Calculator")
app.config(bg="pink")
lbl = tk.Label(app, text="AGE Calculator", font=("Roboto", 30, "underline"), bg="pink")
lbl.pack(fill="x", pady=20)
dob = tk.Entry(app, font=("Roboto", 20, "bold"))
dob.pack(pady=10)
dob.insert(0, "DD-MM-YYYY")
result = tk.Label(app, text="", font=("Roboto", 18), bg="pink")
result.pack(pady=10)
def calculate_age():
    try:
        birth_date = datetime.strptime(dob.get(), "%d-%m-%Y")
        today = datetime.today()
        age = today.year - birth_date.year - (
            (today.month, today.day) < (birth_date.month, birth_date.day)
        )
        result.config(text=f"Your Age is: {age} years")
    except:
        result.config(text="❌ Please enter DOB in DD-MM-YYYY format")
but = tk.Button(app, text="Check Age", font=("Roboto", 14), command=calculate_age)
but.pack(pady=10)

app.mainloop()