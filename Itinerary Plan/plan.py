import math

#Section for getting the recommendation and turing it into a usable array for the itinerary
import pandas as pd


def format_open_hours(df):
    result = []

    for index, row in df[['name', 'location', 'open_time', 'close_time']].iterrows():
        # convert open and close times to 24-hour format
        open_hour = int(row['open_time'].split(':')[0])
        close_hour = int(row['close_time'].split(':')[0])

        if 'PM' in row['close_time'] and close_hour < 12:
            close_hour += 12

        if 'AM' in row['open_time'] and open_hour == 12:
            open_hour = 0

        if 'PM' in row['open_time'] and open_hour < 12:
            open_hour += 12

        # format open and close times as string
        open_str = f"{open_hour}{row['open_time'][-2:]}"
        close_str = f"{close_hour}{row['close_time'][-2:]}"

        # create dictionary with name, location, and open hours
        result_dict = {
            "name": row['name'],
            "location": row['location'],
            "open_hours": f"{open_str}-{close_str}"
        }

        result.append(result_dict)

    return result




data = {
    "Cairo": {
        "restaurants": [
            {"name": "Koshary Abou Tarek", "location": (30.0444, 31.2357), "open_hours": "10AM-12AM"},
            {"name": "Felfela", "location": (30.0479, 31.2336), "open_hours": "8AM-12AM"},
            {"name": "Abou El Sid", "location": (30.0521, 31.3415), "open_hours": "12PM-12AM"},
            {"name": "Taboula", "location": (30.0580, 31.3417), "open_hours": "12PM-1AM"},
            {"name": "Osmanly", "location": (30.0500, 31.3473), "open_hours": "12PM-12AM"},
            {"name": "Nile Pharaohs Cruising Restaurant", "location": (30.0745, 31.2408), "open_hours": "12PM-11PM"},
            {"name": "Kadoura", "location": (30.0505, 31.2390), "open_hours": "1PM-12AM"},
            {"name": "La Palmeraie", "location": (30.0128, 31.2062), "open_hours": "12PM-12AM"},
            {"name": "Le Pacha 1901", "location": (30.0442, 31.2334), "open_hours": "12PM-2AM"},
            {"name": "Andrea El Mariouteya", "location": (29.9782, 31.1685), "open_hours": "12PM-1AM"}
        ],
        "attractions": [
            {"name": "Pyramids of Giza", "location": (29.9792, 31.1342), "open_hours": "8AM-5PM"},
            {"name": "Egyptian Museum", "location": (30.0478, 31.2336), "open_hours": "9AM-5PM"},
            {"name": "Khan el-Khalili", "location": (30.0450, 31.2625), "open_hours": "9AM-11PM"},
            {"name": "Cairo Tower", "location": (30.0458, 31.2245), "open_hours": "9AM-12AM"},
            {"name": "Al-Azhar Park", "location": (30.0463, 31.2599), "open_hours": "8AM-11PM"},
            {"name": "Salah El-Din Citadel", "location": (30.0293, 31.2612), "open_hours": "9AM-5PM"},
            {"name": "The Hanging Church", "location": (30.0100, 31.2300), "open_hours": "9AM-4PM"},
            {"name": "Coptic Museum", "location": (30.0086, 31.2256), "open_hours": "9AM-4PM"},
            {"name": "Sultan Hassan Mosque", "location": (30.0322, 31.2459), "open_hours": "9AM-5PM"},
            {"name": "Muizz Street", "location": (30.0057, 31.2454), "open_hours": "24/7"}
        ]
    },
    "Alexandria": {
        "restaurants": [
            {"name": "Fish Market", "location": (31.2144, 29.8859), "open_hours": "12PM-12AM"},
            {"name": "Abou Abdallah", "location": (31.2153, 29.9335), "open_hours": "10AM-12AM"}
        ],
        "attractions": [
            {"name": "Montaza Palace", "location": (31.2847, 30.0131), "open_hours": "9AM-4PM"},
            {"name": "Alexandria Library", "location": (31.2089, 29.9097), "open_hours": "10AM-7PM"}
        ]
    }
}


def recommendation(city, starting_point, days):
    if city not in data:
        raise ValueError(f"{city} is not a valid city.")
    restaurants = data[city]["restaurants"]
    attractions = data[city]["attractions"]

    start_time = 9  # start time in hours
    meal_intervals = [10, 12, 15, 17]  # meal intervals in hours
    meal_times = {"breakfast": 1, "lunch": 2, "dinner": 3}  # meal times in hours

    def get_closest_place(places, location):
        closest_place = None
        min_distance = math.inf
        for place in places:
            distance = math.sqrt((place["location"][0] - location[0]) ** 2 + (place["location"][1] - location[1]) ** 2)
            if distance < min_distance:
                closest_place = place
                min_distance = distance
        return closest_place

    def recommend_place(places, location, meal_flag, visited):
        if meal_flag and meal_times["breakfast"] not in meal_flag:
            for place in places:
                if place["open_hours"] <= "10AM" and place["name"] not in visited:
                    closest_place = get_closest_place(places, location)
                    print(f"Recommended place for breakfast: {closest_place['name']}")
                    visited.append(closest_place['name'])
                    meal_flag.append(meal_times["breakfast"])
                    return closest_place
        elif meal_flag and meal_times["lunch"] not in meal_flag:
            for place in places:
                if place["open_hours"] <= "12PM" and place["name"] not in visited:
                    closest_place = get_closest_place(places, location)
                    print(f"Recommended place for lunch: {closest_place['name']}")
                    visited.append(closest_place['name'])
                    meal_flag.append(meal_times["lunch"])
                    return closest_place
        elif meal_flag and meal_times["dinner"] not in meal_flag:
            for place in places:
                if place["open_hours"] <= "7PM" and place["name"] not in visited:
                    closest_place = get_closest_place(places, location)
                    print(f"Recommended place for dinner: {closest_place['name']}")
                    visited.append(closest_place['name'])
                    meal_flag.append(meal_times["dinner"])
                    return closest_place
        else:
            unvisited_places = [place for place in places if place["name"] not in visited]
            if unvisited_places:
                closest_place = get_closest_place(unvisited_places, location)
                print(f"Recommended place: {closest_place['name']}")
                visited.append(closest_place['name'])
                return closest_place
            else:
                print("All places have been visited.")
                return None

    if days == 1:
        print("Recommended hotels near the starting point:")
        closest_hotel = get_closest_place([{"name": "Hotel 1", "location": starting_point}], starting_point)
        print(closest_hotel["name"])
        location = starting_point
        meal_flag = []
        visited = []
        for time in range(start_time, 20):
            if time in meal_intervals:
                recommend_place(restaurants, location, meal_flag, visited)
                location = recommend_place(attractions, location, meal_flag, visited)["location"]
            elif time == 19:
                recommend_place(restaurants, location, meal_flag, visited)
                print("Time to go back to the hotel.")
            else:
                recommend_place(attractions, location, meal_flag, visited)
                location = recommend_place(restaurants, location, meal_flag, visited)["location"]
    else:
        print("Recommended hotels near the last visited place:")
        closest_hotel = get_closest_place([{"name": "Hotel 1", "location": starting_point}], starting_point)
        print(closest_hotel["name"])
        location = starting_point
        meal_flag = []
        visited = []
        for day in range(1, days + 1):
            print(f"Day {day}:")
            for time in range(start_time, 20):
                if time in meal_intervals:
                    recommend_place(restaurants, location, meal_flag, visited)
                    location = recommend_place(attractions, location, meal_flag, visited)["location"]
                elif time == 19:
                    recommend_place(restaurants, location, meal_flag, visited)
                    print("Time to go back to the hotel.")
                else:
                    recommend_place(attractions, location, meal_flag, visited)
                    location = recommend_place(restaurants, location, meal_flag, visited)["location"]
            print("Time to go back to the hotel.")
            print()
            location = get_closest_place(attractions, location)["location"]
            meal_flag = []
            visited = []


# recommendation("Cairo", (30.0444, 31.2357), 1)