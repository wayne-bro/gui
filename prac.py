from tkinter import *


root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480") #가로 세로




def opening():
    with open("mynote.txt", "r", encoding="utf8") as memo_file:
        text.insert(END, memo_file.read()) 

    
def saving():
    with open("mynote.txt", "w", encoding="utf8") as memo_file:
        memo_file.write(text.get("1.0", END))
        text.delete("1.0", END)



#메뉴
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=opening)
menu_file.add_separator()
menu_file.add_command(label="저장", command=saving)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu_file.add_separator()
menu.add_cascade(label="파일(F)", menu=menu_file)


menu.add_cascade(label="편집(E)")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")


root.config(menu=menu)


#텍스트
text = Text(root, width=640, height=480)


#스크롤바
frame = Frame(root)
frame.pack(fill="both", expand=True)
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

text = Text(frame, yscrollcommand = scrollbar.set)
text.pack(side="left", fill="both", expand=True)





root.mainloop()