class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.taman_hetkinen_nopeus = 0
        self.kuljettu_matka = 0
   
auto = Auto("ABC-123", "142 km/h")

print (f"Auton rekisteritunnus on {auto.rekisteritunnus}, Auton huippunopeus on {auto.huippunopeus}, Auton tämän hetkinen nopeus on {auto.taman_hetkinen_nopeus} ja Auton kuljettu matka on {auto.kuljettu_matka}.")