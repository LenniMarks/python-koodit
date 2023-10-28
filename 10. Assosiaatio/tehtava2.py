class Hissi:
    def __init__(self, alas_kerros, ylos_kerros):
        self.kerros = alas_kerros
        self.alas_kerros = alas_kerros
        self.ylos_kerros = ylos_kerros
    
    def kerros_ylos(self):
        if self.kerros < self.ylos_kerros:
            self.kerros += 1
        print(f'Hissi on nyt {self.kerros} kerroksessa')

    def kerros_alas(self):
        if self.kerros > self.alas_kerros:
            self.kerros -= 1
        print(f'Hissi on nyt {self.kerros} kerroksessa')
    
    def siirry_kerrokseen(self, kerros):
        if kerros > self.kerros:
            while self.kerros < kerros:
                self.kerros_ylos()
        elif kerros < self.kerros:
            while self.kerros > kerros:
                self.kerros_alas()
        else:
            print(f'Hissi on jo {kerros} kerroksessa')

class Talo:
    def __init__(self, alas_kerros, ylos_kerros, hissit):
        self.alin_kerros = alas_kerros
        self.ylin_kerros = ylos_kerros
        self.hissit = [Hissi(alas_kerros, ylos_kerros) for i in range(hissit)]

    def aja_hissiä(self, hissin_numero, kerros):
        if 0 <= hissin_numero < len(self.hissit):
            hissi = self.hissit[hissin_numero]
            hissi.siirry_kerrokseen(kerros)
        else:
            print(f'Hissiä numero {hissin_numero} ei ole talossa.')

hissi = Hissi(alas_kerros=1, ylos_kerros=5)
hissi.siirry_kerrokseen(5)

talo = Talo(alas_kerros=1, ylos_kerros=10, hissit=2)

talo.aja_hissiä(0, 5)
talo.aja_hissiä(1, 8)
