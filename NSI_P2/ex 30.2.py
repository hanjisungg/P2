from turtle import*
n = int(input("nombre de branches de l'étoile:"))
angle = 360/n
for i in range(n):
    forward(50)
    goto(0, 0)
    right(angle)
