from turtle import*
n = int(input("n:"))
r = 0
g = 0
b = 0
color(r, g, b)
width(10)
y = 0
for i in range(n):
    forward(50)
    y = y-10
    up()
    goto(0, y)
    r = r+1/n
    g = g+1/n
    b = b+1/n
    color(r, g, b)
    down()