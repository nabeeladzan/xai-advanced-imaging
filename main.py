from email.mime import image
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from PIL import ImageTk, Image
from numpy import empty, imag

root = Tk()

root.minsize(1280, 720)
root.title("XAI Photo Bank")


def about():
    messagebox.showinfo(
        'XAI', "Xai's Awesome Images")


def load_image():
    filepath = fd.askopenfilename()
    img = Image.open(filepath)
    update_label()


def update_label():
    view = (ImageTk.PhotoImage(imageActive))
    canvas.itemconfig(image_container, view)


menubar = Menu(root, background='white', foreground='black',
               activebackground='white', activeforeground='black')
file = Menu(menubar, tearoff=0, background='white', foreground='black')
file.add_command(label="New")
file.add_command(label="Open", command=load_image)
file.add_command(label="Save")
file.add_command(label="Save as")
file.add_separator()

file.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file)

edit = Menu(menubar, tearoff=0)
edit.add_command(label="Undo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
menubar.add_cascade(label="Edit", menu=edit)

help = Menu(menubar, tearoff=0)
help.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=help)


root.config(menu=menubar)

frame = Frame(root)
frame.pack(anchor=NW)

canvas = Canvas(
    frame,
    width=800,
    height=600
)
canvas.pack()


image_container = canvas.create_image(0, 0, anchor="nw")
imageActive = Image.open("library/aaa.jpeg")


root.mainloop()
