from turtle import*
n = int(input("n:"))
m = int(input("m:"))
x = 0
y = 0
for i in range(n):
    forward(100)
    up()
    y = y-10
    goto(x, y)
    down()
up()
goto(0, 0)
down()
right(90)
y = 0
x = 100/m 
for i in range(m+1):
    forward(n*10-10)
    up()
    goto(x, y)
    x = x+100/m
    down()
    
    
    
    
