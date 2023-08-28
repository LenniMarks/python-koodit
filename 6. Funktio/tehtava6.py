import math

def laskin(pizza, hinta):
    pinta_ala = math.pi * pizza
    return pinta_ala // hinta

pizza1 = int(input("Anna halkaisija ensimmäiselle pizzalle: "))
hinta1 = int(input("Anna hinta ensimmäiselle pizzalle: "))
pizza2 = int(input("Anna halkaisija toiselle pizzalle: "))
hinta2 = int(input("Anna hinta toiselle pizzalle: "))

print("Ensimmäisen pizzan yksikköhinta " + str(laskin(pizza1, hinta1)))
print("Toisen pizzan yksikköhinta " + str(laskin(pizza2, hinta2)))

