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

hissi = Hissi(alas_kerros=1, ylos_kerros=5)
hissi.siirry_kerrokseen(5)
