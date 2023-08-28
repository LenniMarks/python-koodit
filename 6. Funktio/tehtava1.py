import random

def heitto():
    noppaluku = random.randint(1,6)
    return noppaluku

while True:
    luku = heitto()
    print(luku)
    if luku == 6:
        break

