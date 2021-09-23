from turtle import*

x = 0
y = 0
w = 0
for i in range(20):
    goto(x, y)
    y = y-10
    w = w+1
    width(w)
x = -50
y = 0
w = 0
up()
goto(x, y)
down()
width(1)
for i in range(20):
    goto(x, y)
    y = y-10
    x = x-10
    w = w+1
    width(w)
x = +50
y = 0
w = 0
up()
goto(x, y)
down()
width(1)
for i in range(20):
    goto(x, y)
    y = y-10
    x = x+10
    w = w+1
    width(w)
    
    
    
    
    
    
    