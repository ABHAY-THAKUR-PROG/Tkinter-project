import tkinter as tk

app = tk.Tk()
app.geometry("700x400")
app.title("FeedbackFrom")
app.config(background = "#ff0000")

lbl0 = tk.Label(app, text = "", bg = "#ff0000")
lbl1 = tk.Label(app, text = "User Name", font = ("robort", 20, "italic", "underline"), fg = "black", bg = "#ff0000")
lbl2 = tk.Label(app, text = "User ID", font = ("robort", 20, "italic", "underline"), fg = "black", bg = "#ff0000")
lbl3 = tk.Label(app, text = "Contact", font = ("robort", 20, "italic", "underline"), fg = "black", bg = "#ff0000")
lbl4 = tk.Label(app, text = "Feedback", font = ("robort", 20, "italic", "underline"), fg = "black", bg = "#ff0000")

lbl5 = tk.Label(app, text = ":", font = ("robort", 20, "italic"), fg = "black", bg = "#ff0000")
lbl6 = tk.Label(app, text = ":", font = ("robort", 20, "italic"), fg = "black", bg = "#ff0000")
lbl7 = tk.Label(app, text = ":", font = ("robort", 20, "italic"), fg = "black", bg = "#ff0000")
lbl8 = tk.Label(app, text = ":", font = ("robort", 20, "italic"), fg = "black", bg = "#ff0000")

en1 = tk.Entry(app, font = ("robort", 20))
en2 = tk.Entry(app, font = ("robort", 20))
en3 = tk.Entry(app, font = ("robort", 20))
en4 = tk.Text(app, font = ("robort", 20), height = 1, width = 20)

btn = tk.Button(app, text = "Send ", font = ("robort", 15, "italic"), fg = "red", bg = "#D5C512")

lbl0.grid(row = 0, column = 0, padx = 50, pady = 15)
lbl1.grid(row = 1, column = 1)
lbl2.grid(row = 2, column = 1, pady = 15)
lbl3.grid(row = 3, column = 1)
lbl4.grid(row = 4, column = 1, pady = 15)

lbl5.grid(row = 1, column = 2, padx = 10)
lbl6.grid(row = 2, column = 2)
lbl7.grid(row = 3, column = 2)
lbl8.grid(row = 4, column = 2)

en1.grid(row = 1, column = 3)
en2.grid(row = 2, column = 3)
en3.grid(row = 3, column = 3)
en4.grid(row = 4, column = 3, pady = 15)


btn.grid(row = 5, column = 3)





app.mainloop()