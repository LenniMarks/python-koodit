import mysql.connector

def haeLentokentta(icao):
    sql = "SELECT ident, name, iso_region FROM airport"
    sql += " WHERE ident='" + icao + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentokentän nimi {rivi[1]} ja Sijainti kunta {rivi[2]}")
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )



icao = input("Syötä ICAO-Koodi: ")
haeLentokentta(icao)