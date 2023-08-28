import random

def heitto(maksimiluku):
    noppaluku = random.randint(1,maksimiluku)
    return noppaluku

maksimiluku = int(input("Anna maksimisilmäluku: "))

while True:
    luku = heitto(maksimiluku)
    print(luku)
    if luku == maksimiluku:
        break