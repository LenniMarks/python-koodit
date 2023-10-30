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
   
auto = Auto("ABC-123", 142,)
auto.kiihdytys(+30)
auto.kiihdytys(+70)
auto.kiihdytys(+50)
auto.kiihdytys(-200)
auto.kulje(1.5)

print (f"Auton rekisteritunnus on {auto.rekisteritunnus}, Auton huippunopeus on {auto.huippunopeus}, Auton tämän hetkinen nopeus on {auto.taman_hetkinen_nopeus} ja Auton kuljettu matka on {auto.kuljettu_matka}.")