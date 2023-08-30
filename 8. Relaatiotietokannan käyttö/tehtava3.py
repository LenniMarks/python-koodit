from geopy.geocoders import Nominatim
from geopy import distance

icao1 = input("Anna ensimmäisen lentokentän ICAO-Koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-Koodi: ")

geolocator = Nominatim(user_agent="find_location")
sijainti1 = geolocator.geocode(icao1)

geolocator = Nominatim(user_agent="find_location")
sijainti2 = geolocator.geocode(icao2)

koordinaatti1 = sijainti1.latitude, sijainti1.longitude
koordinaatti2 = sijainti2.latitude, sijainti2.longitude

kilometrit = distance.distance(koordinaatti1, koordinaatti2).km

print("Lentokenttien välinen pituus on " + str(kilometrit) + " km")
