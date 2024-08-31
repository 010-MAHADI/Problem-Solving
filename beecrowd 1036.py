import math
user = input().split()

a = float(user[0])
b = float(user[1])
c = float(user[2])

root = b*b - 4*a*c

if a ==0 or root < 0 :
    print("Impossivel calcular")
else:
    x1 = (-b + math.sqrt(root)) / (2*a)
    x2 = (-b - math.sqrt(root)) / (2*a)

    print(f"R1 = {x1:.5f}\nR2 = {x2:.5f}")