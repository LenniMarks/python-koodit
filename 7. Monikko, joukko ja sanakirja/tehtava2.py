
nimet = set()

while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    elif nimi in nimet:
        print("Aiemmin syötetty nimi")
    elif nimi not in nimet:
        nimet.add(nimi)
        print("Uusi nimi")

for i in nimet:
    print(i)