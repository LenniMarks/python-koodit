import random
arpakuutiot = int(input("Syötä arpakuutioiden määrä: "))
lista = []
i = 0
summa = int(0)
while arpakuutiot > i:
    lista.append(0)
    i += 1

for x in lista:
    x = random.randint(1,6)
    summa = summa + x
    print(summa)


