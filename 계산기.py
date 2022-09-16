from tkinter import *
import math
window = Tk()
window.title("계산기 만들기")

e = Entry(window, width = 40 , bg = "black", fg= "white", bd  = 5)
e.grid(row = 0 , column = 0 , columnspan = 5)

buttons = [
    '0','1','2','sin','+','%',
    '3','4','5','cos','-','//',
    '6','7','8','tan','*','**',
    '9','.','=','log','/','C']

row = 1
col = 0

for char in buttons :

    def click(key = char):
        if key == '=' :
            result = eval(e.get())
            s = (result)
            e.delete(0, END)
            e.insert(0, s)
        elif key == 'C':
            e.delete(0, END)
        elif key == 'sin':
            result = math.sin(float(e.get()))
            s = str(result)
            e.delete(0,END)
            e.insert(0,s)
        elif key == 'cos':
            result = math.cos(float(e.get()))
            s = str (result)
            e.delete(0,END)
            e.insert(0,s)
        elif key == 'tan':
            result = math.tan (float(e.get()))
            s = str (result)
            e.delete(0,END)
            e.insert(0,s)
        elif key == 'log':
            result = math.log(float(e.get()))
            s = str(result)
            e.delete(0,END)
            e.insert(0,s)
        else : 
            e.insert(END, key)
            
    b = Button(window, text =char , width = 7, height = 3 , command = click)
    b.grid(row= row , column=col)
    col += 1
    if col > 5:
        row +=1
        col = 0
window.mainloop()
