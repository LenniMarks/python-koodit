class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.kerros = alin_kerros
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

    def siirry_kerrokseen(self, kohde_kerros):
        if kohde_kerros < self.alin_kerros:
            kohde_kerros = self.alin_kerros
        elif kohde_kerros > self.ylin_kerros:
            kohde_kerros = self.ylin_kerros

        while self.kerros < kohde_kerros:
            self.kerros_ylös()
        while self.kerros > kohde_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.kerros < self.ylin_kerros:
            self.kerros += 1
        self.ilmoita_kerros()

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
        self.ilmoita_kerros()

    def ilmoita_kerros(self):
        print(f"Hissi on kerroksessa {self.kerros}")

hissi = Hissi(1, 10)
hissi.siirry_kerrokseen(7)
hissi.siirry_kerrokseen(1)