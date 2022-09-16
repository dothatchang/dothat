import turtle as t

for i in range(4):
    t.circle(100,180)
    t.rt(90)
    
t.pu()
t.goto(-100,0)
t.pd()
t.fillcolor('yellow')
t.begin_fill()
t.circle(100)
t.end_fill()
f.ht()