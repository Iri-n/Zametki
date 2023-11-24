from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfilename


root = Tk()
root.title("Заметки")
root.geometry("400x400")

menu_bar = Menu(root)
file_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Файл", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()

