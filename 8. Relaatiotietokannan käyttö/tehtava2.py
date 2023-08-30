import mysql.connector
from collections import defaultdict
lentokentat = defaultdict(int)

def haeTyypit(maakoodi):
    sql = "SELECT type FROM airport"
    sql += " WHERE iso_country ='" + maakoodi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            lentokentat[rivi[0]] += 1
        for i in lentokentat:
            print(i + " = " + str(lentokentat[i]))
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )

maakoodi = input("Syötä maakoodi: ")
haeTyypit(maakoodi)
