import phonenumbers
import folium
from mynumber import  number

from  phonenumbers import geocoder

sanNum = phonenumbers.parse(number)
Key="fa69e25c94d74663b60190ca73aec526"

yorlocation = geocoder.description_for_number(sanNum,"en")

print(yorlocation)

# get service provider
from phonenumbers import carrier

service_prov= phonenumbers.parse(number)
print(carrier.name_for_number(service_prov,"en"))

#lat long in the map

from opencage.geocoder import OpenCageGeocode

geocoder=OpenCageGeocode(Key)

query=str(yorlocation)
res=geocoder.geocode(query)

print(res)

lat=res[0]['geometry']['lat']
lng=res[0]['geometry']['lng']

print(lat,lng)



myMap=folium.Map(location=[lat,lng],zoom_start=9)

folium.Marker([lat,lng],popup=yorlocation).add_to(myMap)

myMap.save("my Location.html")
