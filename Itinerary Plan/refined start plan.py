import math
import datetime
import re
import geopy
import geopandas

def convert_to_24h(time_str):
    # Convert the time string to a datetime object with the strptime() method
    time_obj = datetime.datetime.strptime(time_str, "%I%p")

    # Extract the hour from the datetime object and convert it to an integer
    hour_24h = int(time_obj.strftime("%H"))

    return hour_24h


data = {
    "restaurants": [
        {"name": "Koshary Abou Tarek", "location": (30.0444, 31.2357), "opening_time": "10AM", "closing_time": "12AM",
         "city": "cairo"},
        {"name": "Felfela", "location": (30.0479, 31.2336), "opening_time": "8AM", "closing_time": "12AM",
         "city": "cairo"},
        {"name": "Abou El Sid", "location": (30.0521, 31.3415), "opening_time": "12PM", "closing_time": "12AM",
         "city": "cairo"},
        {"name": "Taboula", "location": (30.0580, 31.3417), "opening_time": "12PM", "closing_time": "1AM",
         "city": "cairo"},
        {"name": "Osmanly", "location": (30.0500, 31.3473), "opening_time": "12PM", "closing_time": "12AM",
         "city": "cairo"},
        {"name": "Nile Pharaohs Cruising Restaurant", "location": (30.0745, 31.2408), "opening_time": "12PM",
         "closing_time": "11PM", "city": "cairo"},
        {"name": "Kadoura", "location": (30.0505, 31.2390), "opening_time": "1PM", "closing_time": "12AM",
         "city": "cairo"},
        {"name": "La Palmeraie", "location": (30.0128, 31.2062), "opening_time": "12PM", "closing_time": "12AM",
         "city": "cairo"},
        {"name": "Le Pacha 1901", "location": (30.0442, 31.2334), "opening_time": "12PM", "closing_time": "2AM",
         "city": "cairo"},
        {"name": "Andrea El Mariouteya", "location": (29.9782, 31.1685), "opening_time": "12PM", "closing_time": "1AM",
         "city": "cairo"}
    ],
    "attractions": [
        {"name": "Pyramids of Giza", "location": (29.9792, 31.1342), "opening_time": "8AM", "closing_time": "5PM",
         "city": "cairo"},
        {"name": "Egyptian Museum", "location": (30.0478, 31.2336), "opening_time": "9AM", "closing_time": "5PM",
         "city": "cairo"},
        {"name": "Khan el-Khalili", "location": (30.0450, 31.2625), "opening_time": "9AM", "closing_time": "11PM",
         "city": "cairo"},
        {"name": "Cairo Tower", "location": (30.0458, 31.2245), "opening_time": "9AM", "closing_time": "12AM",
         "city": "cairo"},
        {"name": "Al-Azhar Park", "location": (30.0463, 31.2599), "opening_time": "8AM", "closing_time": "11PM",
         "city": "cairo"},
        {"name": "Salah El-Din Citadel", "location": (30.0293, 31.2612), "opening_time": "9AM", "closing_time": "5PM",
         "city": "cairo"},
        {"name": "The Hanging Church", "location": (30.0100, 31.2300), "opening_time": "9AM", "closing_time": "4PM",
         "city": "cairo"},
        {"name": "Coptic Museum", "location": (30.0086, 31.2256), "opening_time": "9AM", "closing_time": "4PM",
         "city": "cairo"},
        {"name": "Sultan Hassan Mosque", "location": (30.0322, 31.2459), "opening_time": "9AM", "closing_time": "5PM",
         "city": "cairo"},
        {"name": "Muizz Street", "location": (30.0057, 31.2454), "opening_time": "24/7", "closing_time": "24/7",
         "city": "cairo"}
    ]
}

breakfast_start = 8
breakfast_end = 12

lunch_start = 12
lunch_end = 18

dinner_start = 18
dinner_end = 24

# Radius of earth in km
R = 6373.0


def recommendation(city, starting_point, days, start_time, end_time):
    itinerary = []
    visited = []
    breakfast_flag = False
    lunch_flag = False
    dinner_flag = False

    restaurants = [r for r in data["restaurants"] if r["city"] == city]
    attractions = [a for a in data["attractions"] if a["city"] == city]

    current_location = starting_point
    current_time = convert_to_24h(start_time)

    meal_intervals = [10, 12, 15, 17]  # meal intervals in hours
    meal_times = {"breakfast": 1, "lunch": 2, "dinner": 3}  # meal times in hours

    def get_closest_place(places, location, current_time, visited):
        closest_place = {}
        min_distance = math.inf
        for place in places:
            print(place["name"])
            # Calculate lat/long difference in radians
            lat1, lon1 = math.radians(place["location"][0]), math.radians(place["location"][1])
            lat2, lon2 = math.radians(location[0]), math.radians(location[1])

            dlat = lat2 - lat1
            dlon = lon2 - lon1

            # Calculate distance using Haversine formula
            a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = R * c
            print(distance)
            if distance < min_distance and place not in visited:
                closest_place = place
                print("-----------------------------")
                print(closest_place["name"])
                print(closest_place)
                min_distance = distance
        return closest_place

    print("locationnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn")
    locator = geopy.Nominatim(user_agent="myGeocoder")
    location = locator.geocode("Cairo Festival City,Cairo 11835 Egypt")

    print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))

    # reccommend restaurant for breakfast
    if breakfast_start <= current_time < breakfast_end and not breakfast_flag:
        print("djcndjx")
        closest = get_closest_place(restaurants, current_location, current_time, visited)
        open_time_number = re.findall(r'\d+', closest['opening_time'])
        # print(convert_to_24h(closest['opening_time']))
        # print("hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

        if (closest not in visited) and convert_to_24h(closest['opening_time']) <= current_time:
            visited.append(closest)
            print(open_time_number[0])
            print(current_time)
            print("hereeeeeeeeeeeee open timeeeeeeeeeeeeee------------------------------")
            itinerary.append(closest)
            current_time += 1
            current_location = closest["location"]
            breakfast_flag = True
            print(current_location)
    closest = get_closest_place(attractions, current_location, current_time, visited)

    if (closest not in visited) and convert_to_24h(closest['opening_time']) <= current_time:
        visited.append(closest)
        itinerary.append(closest)
        current_time += 2
        current_location = closest["location"]
    closest = get_closest_place(attractions, current_location, current_time, visited)

    if (closest not in visited) and convert_to_24h(closest['opening_time']) <= current_time:
        visited.append(closest)
        itinerary.append(closest)
        current_time += 2
        current_location = closest["location"]

    if lunch_start <= current_time < lunch_end and not lunch_flag:
        closest = get_closest_place(restaurants, current_location, current_time, visited)
        if closest not in visited and convert_to_24h(closest['opening_time']) <= current_time:
            current_time += 1
            visited.append(closest)
            itinerary.append(closest)
            current_location = closest["location"]
            lunch_flag = True
            print(current_location)
    closest = get_closest_place(attractions, current_location, current_time, visited)

    if (closest not in visited) and convert_to_24h(closest['opening_time']) <= current_time:
        visited.append(closest)
        itinerary.append(closest)
        current_time += 2
        current_location = closest["location"]
    closest = get_closest_place(attractions, current_location, current_time, visited)

    if (closest not in visited) and convert_to_24h(closest['opening_time']) <= current_time:
        visited.append(closest)
        itinerary.append(closest)
        current_time += 2
        current_location = closest["location"]

    if dinner_start <= current_time < dinner_end and not dinner_flag:
        closest = get_closest_place(restaurants, current_location, current_time, visited)
        if (closest not in visited) and convert_to_24h(closest['opening_time']) <= current_time:
            current_time += 1
            visited.append(closest)
            itinerary.append(closest)
            current_location = closest["location"]
            dinner_flag = True
            print(current_location)
    print(itinerary)


recommendation("cairo", (30.0444, 31.2357), 1, "9AM", "11PM")
