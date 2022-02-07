from cgitb import text
from tkinter import *


root = Tk()
root.title("KIM's GUI")
root.geometry("640x480")

label1 = Label(root, text="hello")
label1.pack()

photo = PhotoImage(file="C:/Users/user/Desktop/작업/행정 업무/프로그래밍/gui/button.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="see ya!")
    global photo2
    photo2 = PhotoImage(file="C:/Users/user/Desktop/작업/행정 업무/프로그래밍/gui/button2.png")
    label2.config(image=photo2)

btn = Button(root, text="click", command=change)
btn.pack()


root.mainloop()