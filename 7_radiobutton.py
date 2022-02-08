from cgitb import text
from msilib.schema import CheckBox
from tkinter import *


root = Tk()
root.title("KIM's GUI")
root.geometry("640x480")

Label(root, text="select Food").pack() # Label은 그냥 글자가 나오도록 하는 언어

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="hamburger", value=1, variable=burger_var)
btn_burger1.select() #기본으로 선택되어 있게 설정
btn_burger2 = Radiobutton(root, text="cheese burger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="chicken burger", value=3, variable=burger_var)
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="select Drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="coke", value="coke", variable=drink_var)
btn_drink2 = Radiobutton(root, text="sprite", value="sprite", variable=drink_var)
btn_drink3 = Radiobutton(root, text="juice", value="juice", variable=drink_var)
btn_drink1.select()
btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd():
    print(burger_var.get()) #햄버거중 선택된 값
    print(drink_var.get()) #햄버거중 선택된 값

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()