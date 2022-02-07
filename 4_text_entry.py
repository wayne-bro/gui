from cgitb import text
from tkinter import *


root = Tk()
root.title("KIM's GUI")
root.geometry("640x480")

text = Text(root, width="30", height="5")
text.pack()

root.mainloop()