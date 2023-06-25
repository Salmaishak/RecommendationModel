import geopy
import geopandas
import pandas as pd


def convert_to_coordinates(address):
    locator = geopy.Nominatim(user_agent="myGeocoder")
    location = locator.geocode(address)
    lat = location.latitude
    long = location.longitude
    return lat, long


print(convert_to_coordinates("Tropitel Sahl Hasheesh, egypt"))


def search_hotel(hotel_name):
    hotels = pd.read_csv('../Hotels/Allhotels.csv')
    for hotel in hotels:
        result = hotels.loc[hotels['name'] == hotel_name, ['Latitude', 'Longitude']]
        return result


print(search_hotel("Tropitel Sahl Hasheesh"))