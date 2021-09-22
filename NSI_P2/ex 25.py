s = int(input("somme initiale:"))
t = int(input("taux d'interets annuels:"))
n = int(input("nombre d'annees:"))
for i in range(n):
    s = s*t/100
print(s) 
              
