import requests
import os
from dotenv import load_dotenv
load_dotenv()
apikey = os.getenv("apikey")

paikkakunta = input("Anna paikkakunta: ")

koordinaatti_pyynto = "http://api.openweathermap.org/geo/1.0/direct?q=" + paikkakunta + "&limit=1" + "&appid=" + apikey
vastaus = requests.get(koordinaatti_pyynto).json()
longitude = vastaus[0]["lon"]
latitude = vastaus[0]["lat"]

saa_pyynto = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(latitude) + "&lon=" + str(longitude) + "&appid=" + apikey
vastaus2 = requests.get(saa_pyynto).json()
lampotila = str(round(vastaus2["main"]["temp"] - 273.15, 2))
print(f"Pääosin: {vastaus2['weather'][0]['main']} Tarkemmin: {vastaus2['weather'][0]['description']} Lämpötila: {lampotila} astetta")



