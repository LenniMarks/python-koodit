class Julkaisu:

    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.nimi}")

class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Lehti: Nimi {self.nimi}, Päätoimittaja {self.paatoimittaja}")

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Kirja: Nimi {self.nimi}, Kirjoittaja {self.kirjoittaja}, Sivumäärä {self.sivumaara}")


julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Roosa Liksom", 200))

for t in julkaisut:
    t.tulosta_tiedot()