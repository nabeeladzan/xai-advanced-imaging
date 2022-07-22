from msilib.schema import File
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from filters import *
from tkinter import filedialog as fd

root = Tk()
root.minsize(1280, 720)


def about():
    messagebox.showinfo(
        'XAI', "Xai's Awesome Images")


def update_image(img, op):
    global img2
    if op == "og":
        img.save("display.jpeg")
        resized = Image.open("display.jpeg").resize(img_size, Image.LANCZOS)
        img2 = ImageTk.PhotoImage(resized)
    if op == "gr":
        grayscale(img.resize(img_size, Image.LANCZOS))
        resized = Image.open("display.jpeg").resize(img_size, Image.LANCZOS)
        img2 = ImageTk.PhotoImage(resized)
    if op == "fm":
        filmic(img.resize(img_size, Image.LANCZOS))
        resized = Image.open("display.jpeg").resize(img_size, Image.LANCZOS)
        img2 = ImageTk.PhotoImage(resized)
    if op == "ds":
        desat(img.resize(img_size, Image.LANCZOS))
        resized = Image.open("display.jpeg").resize(img_size, Image.LANCZOS)
        img2 = ImageTk.PhotoImage(resized)
    canvas.itemconfig(image_container, image=img2)


def load_image():
    global img1
    global img_path
    global img_size
    filepath = fd.askopenfilename()
    img1 = Image.open(filepath)
    width, height = img1.size
    if height > width:
        if height/2 < 750:
            img_size = (int(width/2), int(height/2))
        elif height/4 < 750:
            img_size = (int(width/4), int(height/4))
        else:
            img_size = (int(width/8), int(height/8))
    else:
        if width/2 < 750:
            img_size = (int(width/2), int(height/2))
        elif width/4 < 750:
            img_size = (int(width/4), int(height/4))
        else:
            img_size = (int(width/8), int(height/8))

    img_path = filepath
    update_image(Image.open(filepath), "og")


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

# Create a canvas and add the image into it
canvas = Canvas(root, width=500, height=750)
canvas.pack(expand=True)
# Create a button to update the canvas image
og = ttk.Button(root, text="Original",
                command=lambda: update_image(Image.open(img_path), "og"))
og.pack()
gr = ttk.Button(root, text="Grayscale",
                command=lambda: update_image(Image.open(img_path), "gr"))
gr.pack()

fm = ttk.Button(root, text="Filmic",
                command=lambda: update_image(Image.open(img_path), "fm"))
fm.pack()

ds = ttk.Button(root, text="Desaturate",
                command=lambda: update_image(Image.open(img_path), "ds"))
ds.pack()

img_size = (500, 750)
img_path = ""
if img_path != "":
    img_file = open(img_path)
# Open an Image in a Variable
resized = Image.open("empty.png").resize(img_size, Image.LANCZOS)
img1 = ImageTk.PhotoImage(resized)
img2 = ImageTk.PhotoImage(Image.open("display.jpeg"))
# Add image to the canvas
image_container = canvas.create_image(0, 0, anchor="nw", image=img1)

root.mainloop()
