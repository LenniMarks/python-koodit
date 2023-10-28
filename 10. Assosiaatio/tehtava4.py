import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeus):
        uusi_nopeus = self.nopeus + nopeus
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        matka = self.nopeus * tuntimaara
        self.kuljettu_matka += matka

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"{self.nimi} - Kilpailun tilanne:")
        print("{:<10} {:<15} {:<15} {:<15}".format("Rekisteri", "Huippunopeus (km/h)", "Nopeus (km/h)", "Kuljettu matka (km)"))
        for auto in self.autot:
            print("{:<10} {:<15} {:<15} {:<15}".format(auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.kuljettu_matka))

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

autot = []
for i in range(1, 11):
    autot.append(Auto("ABC", i))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 1
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()
    tunti += 1

kilpailu.tulosta_tilanne()
