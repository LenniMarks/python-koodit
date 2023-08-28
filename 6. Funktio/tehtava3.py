def muunnin(gallona):
    lasku = gallona * 3.785
    return lasku

while True:
    gallona = int(input("Anna gallona lukumäärä: "))
    if gallona >= 0:
        litra = muunnin(gallona)
        print(str(litra) + " Litraa")
    else:
        break