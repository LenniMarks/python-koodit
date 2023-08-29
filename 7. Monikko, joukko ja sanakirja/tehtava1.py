kuukausi = int(input("Anna kuukauden numero (1-12): "))

vuodenajat = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")

vuodenaika = vuodenajat[kuukausi-1]

print (f"{kuukausi} Kuukausi on Vuodenaika {vuodenaika}.")
