from tkinter import *


root = Tk()
root.title("KIM's GUI")
root.geometry("640x480")


Label(root, text="Select a menu").pack(side="top")
Button(root, text="order").pack(side="bottom")


#  메뉴 프레임
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="ham").pack()
Button(frame_burger, text="cheese").pack()
Button(frame_burger, text="chicken").pack()


#음료 프레임
frame_drink = LabelFrame(root, text="beverage")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="coke").pack()
Button(frame_drink, text="sprite").pack()
Button(frame_drink, text="juice").pack()

root.mainloop()