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
    #삭제
    # listbox.delete(0)   -> 맨 앞부터 삭제

    # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인
    #print("첫번째 부터 세번째 까지 :", listbox.get(0,2))

    #선택된 항목 확인(위치로 반환)
    print("선택된 항목 :", listbox.curselection())

btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()