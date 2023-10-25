import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.taman_hetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytys(self, nopeus):
        self.taman_hetkinen_nopeus = self.taman_hetkinen_nopeus + nopeus
        if self.taman_hetkinen_nopeus > self.huippunopeus:
            self.taman_hetkinen_nopeus = self.taman_hetkinen_nopeus = self.huippunopeus
        if self.taman_hetkinen_nopeus < 0:
            self.taman_hetkinen_nopeus = 0
        return

    def kulje(self, aika):
        matka = self.taman_hetkinen_nopeus * aika
        self.kuljettu_matka += matka

lista = []
for i in range(1, 11):
    rekisteritunnus = "ABC-" + str(i)
    huippunopeus = random.randint(100, 200)
    auto = Auto(rekisteritunnus, huippunopeus)
    lista.append(auto)

kilpailun_jatkuu = True

while kilpailun_jatkuu:
    for auto in lista:
        nopeus = random.randint(-10, 15)
        auto.kiihdytys(nopeus)
        auto.kulje(1)

    for auto in lista:
        if auto.kuljettu_matka >= 10000:
            kilpailun_jatkuu = False
            break

print("{:<10} {:<15} {:<15} {:<15} {:<15}".format("Rekisteri", "Huippunopeus (km/h)", "Nopeus (km/h)", "Kuljettu matka (km)", "Kulunut aika (h)"))
for auto in lista:
    print("{:<10} {:<19} {:<15} {:<19} {:<15}".format(auto.rekisteritunnus, auto.huippunopeus, auto.taman_hetkinen_nopeus, auto.kuljettu_matka, auto.kuljettu_matka / auto.taman_hetkinen_nopeus))

