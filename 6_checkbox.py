from cgitb import text
from msilib.schema import CheckBox
from tkinter import *


root = Tk()
root.title("KIM's GUI")
root.geometry("640x480")

chkvar = IntVar() #chkvar에 int형으로 값을 저장
chkbox = Checkbutton(root, text="don't do this today anymore.", variable=chkvar)
#chkbox.select() 자동 선택 처리
#chkbox.deselect 선택 해제 처리
chkbox.pack()



def btncmd():
    print(chkvar.get()) #0은 체크 해제, 1은 체크

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()