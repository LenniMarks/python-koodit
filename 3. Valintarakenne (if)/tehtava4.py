vuosi = int(input("Anna vuosiluku: "))



if vuosi % 4 == 0:
    print(str(vuosi) + " on karkausvuosi")
elif vuosi % 100 == 0 and vuosi % 400 == 0:
    print(str(vuosi) + " on karkausvuosi")
else:
    print(str(vuosi) + " ei ole karkausvuosi")