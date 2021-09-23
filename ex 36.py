from turtle import*

n = int(input("n:"))
right(180)
speed(100)
a = 0
b = 1
for i in range(n):
    c = a+b
    a = b
    b = c
    circle(a, 90)
    
