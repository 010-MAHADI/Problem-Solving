user = input().split()
a = int(user[0])
b = int(user[1])
c = int(user[2])
d = int(user[3])

sum1 = c + d
sum2 = a + b

if b > c and d > a and sum1 > sum2 and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")

else:
    print("Valores nao aceitos")
