a = int(input())
print(a)
for x in [100, 50, 20, 10, 5, 2, 1]:
    print(f"{a//x} nota(s) de R$ {x},00")
    a = a % x
