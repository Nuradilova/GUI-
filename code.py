from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

root = Tk()
root.geometry('500x500')

#def openFile():
 #   filepath = filedialog.askopenfilename(initialdir='C:\\Users\\user\\python files', title='Open file', 
  #                                          filetypes=(('image files', "*.jpg"), ("all files", "*.*")) )
    
   # file = open(filepath, 'r')
    #print(file.read())
    #file.close()
class MyInterface():
 pass


button_quit = Button(root, text = "Quit Button", command = root.quit)
button_quit.grid(row=3, column=0)

button_1 = Button(root, text= "Button1")
button_2 = Button(root, text= "Button2")

button_1.grid(row=1, column=0)
button_2.grid(row=2, column=0)
#

my_img = ImageTk.PhotoImage(Image.open("icon.png"))
my_label = Label(image=my_img)
my_label.grid(row=4, column=0)



#button = Button(text = 'open', command = openFile)
#button.pack()
root.mainloop()




