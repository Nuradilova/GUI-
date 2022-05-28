from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from cProfile import label
from cgitb import text
from turtle import bgcolor, color
from setuptools import Command
from PIL import ImageFont
from PIL import ImageDraw

root = Tk()
root.geometry('700x700')

imag= PhotoImage(file = 'C:\\Users\\user\\python files\\ala.png')
root.iconphoto(False, imag)

t=Text(root, height=5, width=4)
l=Label(root,text = '#Select a file to use other commands', background='#D2E6FF', borderwidth=3)
l.config(font=('Courier', 10))
l.grid(row=1, column=1)

def openFile():
   global filepath
   filepath = filedialog.askopenfilename(initialdir='C:\\Users\\user\\python files', title='Open file')
   photo = Image.open(filepath)
   
def grey():
    my_pic= Image.open(filepath)
    bw_image = my_pic.convert('L')
    bw_image.show() 
    bw_image.save('image.png')

def resized():
    my_pic= Image.open(filepath) 
    resized = my_pic.resize((int(my_box1.get()),int(my_box.get())), Image.Resampling.LANCZOS)  
    new_pic = ImageTk.PhotoImage(resized)
    
    label1 = Label(image=new_pic)
    label1.image = new_pic
    label1.grid(row=20, column=2)


def get_width():
    try:
        int(my_box1.get())
        answer1.config(text="Available value!")
    except ValueError:
        print("Width can be only Number")

def get_width():
    try:
        int(my_box1.get())
        answer1.config(text="Available value!", bg='#A9CDD5')
    except ValueError:
        print("Width can be only Number")


def get_height():
    try:
        int(my_box.get())
        answer2.config(text="Available value!", bg='#A9CDD5')
    except ValueError:
        print("Height can be only Number")


def add_watermark():
    im = Image.open(filepath)
    w, h = im.size
    color = 'black'
    draw = ImageDraw.Draw(im)
    text = "AlaToo"
    font = ImageFont.truetype('arial', (w+h)//22)
    textwidth, textheight = draw.textsize(text, font)
    # calculate the x,y coordinates of the text
    margin = 20
    x = w - textwidth - margin
    y = h - textheight - margin
    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font, fill='#FA05B0', stroke_fill='purple', bgcolor = 'grey')
    im.show()
    im.save('with_watermark.png')

button_quit = Button(root, text = "Quit Button", command = root.quit)
button_quit.grid(row=3, column=0)

button_1 = Button(root, text= "Button1", command= black_white())
button_2 = Button(root, text= "Button2")

button_1.grid(row=1, column=0)
button_2.grid(row=2, column=0)
#

my_img = ImageTk.PhotoImage(Image.open("icon.png"))
my_label = Label(image=my_img)
my_label.grid(row=4, column=0)



button = Button(text = 'open', command = openFile)
button.grid(row=5, column=0)
root.mainloop()




