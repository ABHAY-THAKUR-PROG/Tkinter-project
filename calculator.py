import tkinter as tk
from tkinter import font

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Modern Calculator")
        self.configure(bg="#222831")
        self.resizable(False, False)

        self.custom_font = font.Font(family="Segoe UI", size=18, weight="bold")
        self.display_font = font.Font(family="Segoe UI", size=24, weight="bold")

        self.expression = ""

        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self, font=self.display_font, bg="#393E46", fg="#eeeeee",
                                bd=0, relief=tk.FLAT, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=15, pady=(20, 10), ipady=15, sticky="nsew")

        buttons = [
            ('C', 1, 0, "#00adb5"), ('±', 1, 1, "#00adb5"), ('%', 1, 2, "#00adb5"), ('/', 1, 3, "#ff5722"),
            ('7', 2, 0, "#393E46"), ('8', 2, 1, "#393E46"), ('9', 2, 2, "#393E46"), ('*', 2, 3, "#ff5722"),
            ('4', 3, 0, "#393E46"), ('5', 3, 1, "#393E46"), ('6', 3, 2, "#393E46"), ('-', 3, 3, "#ff5722"),
            ('1', 4, 0, "#393E46"), ('2', 4, 1, "#393E46"), ('3', 4, 2, "#393E46"), ('+', 4, 3, "#ff5722"),
            ('0', 5, 0, "#393E46"), ('.', 5, 1, "#393E46"), ('=', 5, 2, "#00adb5"),
        ]

        for (text, row, col, color) in buttons:
            btn = tk.Button(self, text=text, font=self.custom_font, bg=color, fg="#eeeeee",
                            bd=0, relief=tk.FLAT, activebackground="#222831", activeforeground="#fff",
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=8, pady=8, ipadx=20, ipady=20, sticky="nsew")
        
       
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                
                result = str(eval(self.expression.replace('×', '*').replace('÷', '/')))
                self.expression = result
            except Exception:
                self.expression = "Error"
        elif char == '±':
            if self.expression and self.expression[0] == '-':
                self.expression = self.expression[1:]
            else:
                self.expression = '-' + self.expression
        elif char == '%':
            try:
                self.expression = str(float(self.expression)/100)
            except:
                self.expression = "Error"
        else:
            self.expression += str(char)
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()