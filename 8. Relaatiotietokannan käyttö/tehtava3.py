from geopy import distance
import mysql.connector

def haku(icao1):
    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident='" + icao1 + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos[0]

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='1234',
         autocommit=True
         )

icao1 = input("Anna ensimmäisen lentokentän ICAO-Koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-Koodi: ")

sijainti1 = haku(icao1)
sijainti2 = haku(icao2)

matka = round(distance.distance(sijainti1, sijainti2).km)

print(f"Lentokenttien välinen matka on {matka} km")