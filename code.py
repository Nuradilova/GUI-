from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.geometry('500x500')

def openFile():
   filepath = filedialog.askopenfilename(initialdir='C:\\Users\\user\\python files', title='Open file', 
                                          filetypes=(('image files', "*.jpg"), ("all files", "*.*")) )
    
   file = open(filepath, 'r')
   print(file.read())
   file.close()
   
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




