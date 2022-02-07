from cgitb import text
from tkinter import *


root = Tk()
root.title("KIM's GUI")
root.geometry("640x480")

text = Text(root, width="30", height="5")  # Text는 여러줄 입력
text.pack()
text.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)  #Entry는 한줄 입력용
e.pack()
e.insert(0, "한줄만 입력")


def value():
    #내용 출력
    print(text.get("1.0", END)) #처음부터 끝까지 입력 내용을 다 가져오라는 의미, 1은 첫번째 라인 , 0은 0번째 column 위치
    print(e.get())

    #내용 삭제
    text.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="click", command=value)
btn.pack()


root.mainloop()