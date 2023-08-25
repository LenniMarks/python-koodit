lista = []
while True:
    luku = input("Anna luku: ")
    if luku == "":
        break
    lista.append(luku)

for i in range(0, len(lista)):
    lista[i] = int(lista[i])

lista.sort(reverse=True)

print(lista[0:5])