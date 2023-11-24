from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE


def new_file():
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)


def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except EXCEPTION:
        messagebox.showerror("Нельзя сохранить файл!")


def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return
        file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)


root = Tk()
root.title("Заметки")
root.geometry("500x500")



text = Text(root, width=500, height=500)
text.pack()

menu_bar = Menu(root)
file_menu = Menu(menu_bar)

file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Сохранить как", command=save_as)

menu_bar.add_cascade(label="Файл", menu=file_menu)

root.config(menu=menu_bar)

open_button = ttk.Button(text="Открыть файл", command=open_file)


save_button = ttk.Button(text="Сохранить файл", command=save_as)


root.mainloop()
