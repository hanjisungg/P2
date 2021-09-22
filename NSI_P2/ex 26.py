n = int(input("nombre de notes?"))
s = 0
total = 0
for i in range(n):
    note = int(input("note:"))
    c = int(input("coefficient:"))
    s = s+note*c
    total = total+c
moyenne = s/total
print(moyenne)
