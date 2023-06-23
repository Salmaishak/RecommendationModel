import math
import datetime

# def convert_to_24h(time_str):
#     # Convert the time string to a datetime object with the strptime() method
#     time_obj = datetime.datetime.strptime(time_str, "%I%p")
#
#     # Extract the hour from the datetime object and convert it to an integer
#     hour_24h = int(time_obj.strftime("%H"))
#     return hour_24h
def compare_times(time1, time2):
    """
    Compares two times in the format of "HH:MM AM/PM" and returns a string indicating which one is greater.

    Args:
        time1 (str): The first time to compare.
        time2 (str): The second time to compare.

    Returns:
        str: A string indicating which time is greater.
    """
    # Convert the times to 24-hour format for comparison
    time1_24h = datetime.datetime.strptime(time1, "%I:%M %p").strftime("%H:%M")
    time2_24h = datetime.datetime.strptime(time2, "%I:%M %p").strftime("%H:%M")

    # Compare the times and return the result as a string
    if time1_24h > time2_24h or time1_24h == time2_24h:
        return True
    elif time1_24h < time2_24h:
        return False

data = {
    "restaurants": [
        {"name": "Koshary Abou Tarek", "location": (30.0444, 31.2357), "opening_time": "10AM", "closing_time": "12AM", "city": "cairo"},
        {"name": "Felfela", "location": (30.0479, 31.2336), "opening_time": "8AM", "closing_time": "12AM", "city": "cairo"},
        {"name": "Abou El Sid", "location": (30.0521, 31.3415), "opening_time": "12PM", "closing_time": "12AM", "city": "cairo"},
        {"name": "Taboula", "location": (30.0580, 31.3417), "opening_time": "12PM", "closing_time": "1AM", "city": "cairo"},
        {"name": "Osmanly", "location": (30.0500, 31.3473), "opening_time": "12PM", "closing_time": "12AM", "city": "cairo"},
        {"name": "Nile Pharaohs Cruising Restaurant", "location": (30.0745, 31.2408), "opening_time": "12PM", "closing_time": "11PM", "city": "cairo"},
        {"name": "Kadoura", "location": (30.0505, 31.2390), "opening_time": "1PM", "closing_time": "12AM", "city": "cairo"},
        {"name": "La Palmeraie", "location": (30.0128, 31.2062), "opening_time": "12PM", "closing_time": "12AM", "city": "cairo"},
        {"name": "Le Pacha 1901", "location": (30.0442, 31.2334), "opening_time": "12PM", "closing_time": "2AM", "city": "cairo"},
        {"name": "Andrea El Mariouteya", "location": (29.9782, 31.1685), "opening_time": "12PM", "closing_time": "1AM", "city": "cairo"}
    ],
    "attractions": [
        {"name": "Pyramids of Giza", "location": (29.9792, 31.1342), "opening_time": "8AM", "closing_time": "5PM", "city": "cairo"},
        {"name": "Egyptian Museum", "location": (30.0478, 31.2336), "opening_time": "9AM", "closing_time": "5PM", "city": "cairo"},
        {"name": "Khan el-Khalili", "location": (30.0450, 31.2625), "opening_time": "9AM", "closing_time": "11PM", "city": "cairo"},
        {"name": "Cairo Tower", "location": (30.0458, 31.2245), "opening_time": "9AM", "closing_time": "12AM", "city": "cairo"},
        {"name": "Al-Azhar Park", "location": (30.0463, 31.2599), "opening_time": "8AM", "closing_time": "11PM", "city": "cairo"},
        {"name": "Salah El-Din Citadel", "location": (30.0293, 31.2612), "opening_time": "9AM", "closing_time": "5PM", "city": "cairo"},
        {"name": "The Hanging Church", "location": (30.0100, 31.2300), "opening_time": "9AM", "closing_time": "4PM", "city": "cairo"},
        {"name": "Coptic Museum", "location": (30.0086, 31.2256), "opening_time": "9AM", "closing_time": "4PM", "city": "cairo"},
        {"name": "Sultan Hassan Mosque", "location": (30.0322, 31.2459), "opening_time": "9AM", "closing_time": "5PM", "city": "cairo"},
        {"name": "Muizz Street", "location": (30.0057, 31.2454), "opening_time": "24/7", "closing_time": "24/7", "city": "cairo"}
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


def plan(city, starting_point, days, start_time, end_time):

    itinerary = []
    visited = []
    breakfast_flag = False
    lunch_flag = False
    dinner_flag = False

    restaurants = [r for r in data["restaurants"] if r["city"] == city]
    attractions = [a for a in data["attractions"] if a["city"] == city]

    current_location = starting_point
    current_time = start_time

    def get_closest_place(places, location, current_time, visited):
        closest_place = None
        min_distance = math.inf
        for place in places:
            # Calculate lat/long difference in radians
            lat1, lon1 = math.radians(place["location"][0]), math.radians(place["location"][1])
            lat2, lon2 = math.radians(location[0]), math.radians(location[1])

            dlat = lat2 - lat1
            dlon = lon2 - lon1

            # Calculate distance using Haversine formula
            a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = R * c

            if distance < min_distance and place not in visited:
                closest_place = place
                min_distance = distance

        # Sort the list of places based on distance
        sorted_places = sorted(places, key=lambda place: get_distance(place["location"], location))
        print(sorted_places)
        # Remove already visited places
        sorted_places = [place for place in sorted_places if place not in visited]
        print(place)
        # Insert the closest place at the beginning of the list
        if closest_place is not None:
            sorted_places.insert(0, closest_place)

        return sorted_places

    def get_distance(location1, location2):
        # Calculate lat/long difference in radians
        lat1, lon1 = math.radians(location1[0]), math.radians(location1[1])
        lat2, lon2 = math.radians(location2[0]), math.radians(location2[1])

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Calculate distance using Haversine formula
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        print(distance)
        return distance

    for day in range(days):

        while current_time < end_time:
            if (not breakfast_flag and compare_times(current_time,breakfast_end) == False and compare_times(current_time,breakfast_start) == True):
                closest_places = get_closest_place(restaurants,starting_point,current_time,visited)
                print ("------------------------")
                for place in closest_places:
                    print("fdjvjvbj")
                    if((place["opening_time"]) <= current_time and convert_to_24h(place["closing_time"]) > current_time ):
                        print("*******************")
                        itinerary.append(place)
                        visited.append(place)
                        current_time += 1
                        breakfast_flag = True
                        print("enterdd")
                        print(place)
                        print(itinerary)
            elif (not lunch_flag and current_time < lunch_end and current_time >= lunch_start):
                closest_places = get_closest_place(restaurants,starting_point,current_time,visited)
                for place in closest_places:
                    if(convert_to_24h(place["opening_time"]) <= current_time and convert_to_24h(place["closing_time"]) > current_time ):
                        print("fjfnfnjd")
                        itinerary.append(place)
                        visited.append(place)
                        current_time += 1
                        lunch_flag = True
            elif (not dinner_flag and current_time < dinner_end and current_time >= dinner_start):
                closest_places = get_closest_place(restaurants, starting_point, current_time, visited)
                for place in closest_places:
                    if (convert_to_24h(place["opening_time"]) <= current_time and convert_to_24h( place["closing_time"]) > current_time):
                        itinerary.append(place)
                        visited.append(place)
                        current_time += 1
                        dinner_flag = True



            print(itinerary)
            break


plan("cairo", (30.0444, 31.2357), 1,"9AM","11PM")