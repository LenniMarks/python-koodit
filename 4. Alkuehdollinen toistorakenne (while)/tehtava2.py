tuuma = int(input("Syötä tuuma: "))

while tuuma >= 0:
    sentit = tuuma * 2.54
    print(str(tuuma) + " Tuumaa on " + str(sentit) + " cm")
    tuuma = int(input("Syötä tuuma: "))
