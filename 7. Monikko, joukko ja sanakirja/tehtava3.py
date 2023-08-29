lentokentat = {"EFHK":"Helsinki-Vantaa",
               "OUL":"Oulu",
               "EGLL":"Lontoo-Heathrow"}


while True:
    kysely1 = input("Syötä uusi lentoasema(x), Hae lentoasemaa(y), Lopeta(p): ")
    if kysely1 == "x" or kysely1 == "X":
        icao1 = input("Syötä lentoaseman ICAO-Koodi: ")
        nimi = input("Syötä lentoaseman nimi: ")
        lentokentat[icao1] = nimi
    elif kysely1 == "y" or kysely1 == "Y":
        icao2 = input("Syötä lentoaseman ICAO-Koodi: ")
        if icao2 in lentokentat:
            print(f"{lentokentat[icao2]}")
        else:
            print("Väärä ICAO-Koodi")
    elif kysely1 == "p" or kysely1 == "P":
        break