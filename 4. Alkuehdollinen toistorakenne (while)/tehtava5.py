ktunnus = "python"
salasana = "rules"
yritykset = 0
while True:
    tunnuskysely = input("Anna käyttäjätunnus: ")
    salasanakysely = input("Anna salasana: " )
    if tunnuskysely == ktunnus and salasanakysely == salasana:
        print("Tervetuloa")
        break
    elif yritykset >= 4:
        print("Pääsy evätty")
        break
    elif tunnuskysely != ktunnus or salasanakysely != salasana:
        print("Väärin")
        yritykset = yritykset + 1
    elif tunnuskysely != ktunnus and salasanakysely != salasana:
        print("Väärin")
        yritykset = yritykset + 1



