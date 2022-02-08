import tkinter.messagebox as msgbox
from tkinter import *


root = Tk()
root.title("KIM's GUI")
root.geometry("640x480")

# messagebox는 alert와 기능 비슷

#기차 예매 시스템이라고 가정
def info():
    msgbox.showinfo("notice", "The reservation is complete.")

def warn():
    msgbox.showwarning("warning", "You're fully booked!")

def error():
    msgbox.showerror("error", "Unknown Error!")


def okcancel():
    msgbox.askokcancel("ok/cancel", "For kids only. Wanna return?")

def retrycancel():
    msgbox.askretrycancel("retry/cancel", "Unknown error. Wanna retry?")

def yesno():
    msgbox.askyesno("yes/no", "Wanna cancel?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="Not saved. Wanna quit after saving?")
    # 네 : 저장 후 종료
    #아니오 : 저장하지 않고 종료
    #취소 : 프로그램 종료 취소(현재 화면에서 계속 작업)
    print(response) #True, False, None -> 예 1, 아니오 0, 그외
    if response == 1:
        print("Yes")
    elif response == 0:
        print("no")
    else:
        print("None")



Button(root, command=info, text="push").pack()
Button(root, command=warn, text="warning").pack()
Button(root, command=error, text="error").pack()
Button(root, command=okcancel, text="confirm").pack()
Button(root, command=retrycancel, text="retry").pack()
Button(root, command=yesno, text="yes / no").pack()
Button(root, command=yesnocancel, text="yes / no / cancel").pack()



root.mainloop()