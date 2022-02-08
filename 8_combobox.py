from cgitb import text
from msilib.schema import CheckBox
import tkinter.ttk as ttk
from tkinter import *


root = Tk()
root.title("KIM's GUI")
root.geometry("640x480")


values = [str(i) + "일" for i in range(1, 32)] # 1~31까지의 숫자

combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("월급날") #최초 목록 제목 설정

combobox2 = ttk.Combobox(root, height=10, values=values, state="readonly") #값을 직접 입력하지 못함
combobox2.current(0) # 0번째 인덱스 값 선택
combobox2.pack()


def btncmd():
    print(combobox.get())
    print(combobox2.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()