class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = 0

    def kulje(self, aika):
        matka = self.nopeus * aika
        self.kuljettu_matka += matka

    def tulosta_tiedot(self):
        print(self.rekisteritunnus)
class Sähköauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti, nopeus):
        self.nopeus = nopeus
        super().__init__(rekisteritunnus, huippunopeus, nopeus)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Auton matkamittarilukema on {self.kuljettu_matka}")

class Polttomoottoriauto(Auto):

    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko, nopeus):
        self.nopeus = nopeus
        super().__init__(rekisteritunnus, huippunopeus, nopeus)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Auton matkamittarilukema on {self.kuljettu_matka}")
   
autot = []
autot.append(Sähköauto("ABC-15", 180, 52.5, 125))
autot.append(Polttomoottoriauto("ACD-123",165, 32.3, 155))

for t in autot:
    t.kulje(3)
    t.tulosta_tiedot()