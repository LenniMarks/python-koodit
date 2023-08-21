kuhan_pituus = int(input("Anna kuhan pituus: "))

alimitta = 37
puuttuva_pituus = alimitta - kuhan_pituus
if kuhan_pituus < alimitta:
    print("Laske kuha takaisin järveen. Alimmasta sallitusta pyyntimitasta puuttuu " + str(puuttuva_pituus) + "cm")
else:
    print("Kuhan pituus on sallittu")