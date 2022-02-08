from cProfile import label
from cgitb import text
import tkinter.ttk as ttk
import time
from tkinter import *


root = Tk()
root.title("KIM's GUI")
root.geometry("640x480")

menu = Menu(root)

def creat_new_file():
    pass

#File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=creat_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File")
menu_file.add_separator()
menu_file.add_command(label="Quit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

#Edit 메뉴
menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label="Un Do")
menu_edit.add_command(label="Re Do")
menu_edit.add_separator()
menu_edit.add_command(label="Cut")
menu.add_cascade(label="Edit", menu=menu_edit)

# radio 버튼을 통해 선택
menu_lan = Menu(menu, tearoff=0)
menu_lan.add_radiobutton(label="Korean")
menu_lan.add_radiobutton(label="English")
menu_lan.add_radiobutton(label="French")
menu.add_cascade(label="Language", menu=menu_lan)

# checkbutton 활용
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="show minimap")
menu.add_cascade(label="View", menu=menu_view)


root.config(menu=menu)  #윈도우 창에 메뉴 등록
root.mainloop()