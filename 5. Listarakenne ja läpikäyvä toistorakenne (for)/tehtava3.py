luku = int(input("Anna luku: "))

todenmukaisuus = True
if luku < 2:
    todenmukaisuus = False
if luku > 2:
    for i in range(2, luku):
        if luku % i == 0:
            todenmukaisuus = False
            break
        else:
            todenmukaisuus = True

if todenmukaisuus:
    print(str(luku) + " On alkuluku")
else:
    print(str(luku) + " Ei ole alkuluku")

