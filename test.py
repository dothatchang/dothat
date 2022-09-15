from tkinter import *
window = Tk()
window.title("커피자동주문기")


e = Entry(window, width = 40 , bg = "white", fg= "black", bd  = 5)
e.grid(row = 0 , column = 0 , columnspan = 10)

buttons = [
    '아메리카노\n(핫)','카페라테\n(핫)','카푸치노\n(핫)',
    '아메리카노\n(아이스)','카페라테\n(아이스)','카푸치노\n(아이스)',
    '핫초코','주문','지움']

row = 1
col = 0

for char in buttons :

    def click(key = char):
        if key == '주문':
            result = eval(e.get())
            s = (result)
            e.delete(0, END)
            e.insert(0, s)
        elif key == '지움':
            e.delete(0, END)
        elif key == '아메리카노\n(핫)':
            result = "3000"
            s = (result)
            if len(e.get()) == 0:
                e.insert(END, s)
            else:
                e.insert(END, '+')
                e.insert(END, s)
        elif key == '핫초코':
            result = "3000"
            s = (result)
            if len(e.get()) == 0:
                e.insert(END, s)
            else:
                e.insert(END, '+')
                e.insert(END, s)
        else :
            result = "4000"
            s = (result)
            if len(e.get()) == 0:
                e.insert(END, s)
            else:
                e.insert(END, '+')
                e.insert(END, s)
        
    b = Button(window, text =char , width = 9,height = 2 , command = click)
    b.grid(row= row , column=col)
    col +=1
    if col > 2:
        row +=1
        col = 0
window.mainloop()