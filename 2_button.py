from tkinter import *


root = Tk()
root.title("KIM's GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=5, text="버튼4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="C:/Users/user/Desktop/작업/행정 업무/프로그래밍/gui/button.png")
btn6 = Button(root, image=photo)
btn6.pack()


def btncmd():
    print("button click!")

btn7 = Button(root, text="button7", command=btncmd)
btn7.pack()

root.mainloop()