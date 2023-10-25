import random

class Auto:
    def __init__(self, nimi, nopeus, kulutus):
        self.nimi = nimi
        self.nopeus = nopeus
        self.kulutus = kulutus
        self.matka = 0

    def kulje(self, tunti):
        self.matka += self.nopeus * tunti

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.uniform(-10, 10)
            auto.nopeus += nopeuden_muutos
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{'Nimi':<15}{'Nopeus (km/h)':<15}{'Kulutus (l/h)':<15}{'Matka (km)':<15}")
        for auto in self.autot:
            print(f"{auto.nimi:<15}{auto.nopeus:<15.2f}{auto.kulutus:<15.2f}{auto.matka:<15.2f}")

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.matka >= self.pituus:
                return True
        return False

autot = [Auto("Auto1", 100, 10),
             Auto("Auto2", 120, 8),
             Auto("Auto3", 90, 12),
             Auto("Auto4", 110, 9),
             Auto("Auto5", 105, 11),
             Auto("Auto6", 115, 9.5),
             Auto("Auto7", 95, 13),
             Auto("Auto8", 125, 8.5),
             Auto("Auto9", 98, 11.5),
             Auto("Auto10", 130, 8.0)]

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

print(f"Kilpailu: {kilpailu.nimi}")
print("Kilpailu alkaa!")
    
tunnit = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        print(f"Aika kulunut: {tunnit} tuntia")
        kilpailu.tulosta_tilanne()
    
print("Kilpailu päättyi!")
kilpailu.tulosta_tilanne()