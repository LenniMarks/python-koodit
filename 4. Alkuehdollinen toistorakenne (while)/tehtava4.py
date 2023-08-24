import random
luku = (random.randint(1, 10))

while True:
    kayttajan_luku = int(input("Anna luku: "))
    if kayttajan_luku == luku:
        print("Oikein")
        break
    elif kayttajan_luku < luku:
        print("Liian pieni arvaus")
    elif kayttajan_luku > luku:
        print("Liian suuri arvaus")