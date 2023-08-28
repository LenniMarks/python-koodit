def laskin(kokonaisluvut):
    i = 0
    while i < len(kokonaisluvut):
        if kokonaisluvut[i] % 2 == 0:
            karsittulista.append(kokonaisluvut[i])
        i+=1
    return kokonaisluvut

karsittulista = []
kokonaisluvut = [4, 6, 2, 5, 2, 7, 8, 2]
print(laskin(kokonaisluvut))
print(karsittulista)