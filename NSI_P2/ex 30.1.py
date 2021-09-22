from turtle import*
c = int(input("nombre de cotés du polygones:"))
angle = 360/c
for i in range(c):
    forward(50)
    right(angle)
