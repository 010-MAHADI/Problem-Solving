
user = float(input())

if 0 <= user <= 25:
    print("Intervalo [0,25]")

elif 25 < user <= 50:
    print("Intervalo (25,50]")

elif 50 < user <= 75:
    print("(50,75]")

elif 75 < user <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
