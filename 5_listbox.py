from cgitb import text
from tkinter import *


root = Tk()
root.title("KIM's GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()



def btncmd():
    pass



btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()