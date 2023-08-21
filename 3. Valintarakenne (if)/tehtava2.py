hyttiluokka = input("Anna hyttiluokkasi: ")

lux = "LUX on parvekkeellinen hytti yläkannella."
a = "A on ikkunallinen hytti autokannen yläpuolella."
b = "B on ikkunaton hytti autokannen yläpuolella."
c = "C on ikkunaton hytti autokannen alapuolella."

if hyttiluokka == "LUX":
    print(lux)
elif hyttiluokka == "A":
    print(a)
elif hyttiluokka == "B":
    print(b)
elif hyttiluokka == "C":
    print(c)
else:
    print("Virheellinen hyttiluokka")