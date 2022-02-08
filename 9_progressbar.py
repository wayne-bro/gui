from cgitb import text
import tkinter.ttk as ttk
import time
from tkinter import *


root = Tk()
root.title("KIM's GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate") # indeterminate는 작업이 언제 끝날지 모르는 상황에 사용
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") 
# progressbar.start(10)  # 10ms 마다 움직임
# progressbar.pack()



# def btncmd():
#     progressbar.stop() #작동 중지

p_var2 = DoubleVar() #실수, 정수 표현
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2) 
progressbar2.pack()


def btncmd():
     for i in range(1, 101):
         time.sleep(0.01) #0.01초 대기

         p_var2.set(i) #progressbar의 값 설정
         progressbar2.update() #ui 업데이트
         print(p_var2.get())




btn = Button(root, text="click", command=btncmd)
btn.pack()


root.mainloop()