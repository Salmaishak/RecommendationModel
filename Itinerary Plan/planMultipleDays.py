import math
import datetime


# def convert_to_24h(time_str):
#     # Convert the time string to a datetime object with the strptime() method
#     time_obj = datetime.datetime.strptime(time_str, "%I%p")
#
#     # Extract the hour from the datetime object and convert it to an integer
#     hour_24h = int(time_obj.strftime("%H"))
#     return hour_24h
import re
from datetime import datetime

from datetime import datetime
from datetime import datetime

from datetime import datetime


def is_open(open_time, close_time, check_time):
    """Check if check_time is between open_time and close_time"""
    # Convert times to 24 hour format
    open_time = datetime.strptime(open_time, "%I%p").strftime("%H")
    close_time = datetime.strptime(close_time, "%I%p").strftime("%H")
    check_time = datetime.strptime(check_time, "%I%p").strftime("%H")

    if open_time < close_time:
        # Open time is before close time in the same day
        return open_time <= check_time <= close_time
    else:
        # Open time is after close time, so open spans midnight
        return check_time >= open_time or check_time <= close_time

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
    time1_24h = datetime.strptime(time1, "%I%p").strftime("%H")
    time2_24h = datetime.strptime(time2, "%I%p").strftime("%H")

    # Compare the times and return the result as a string
    if time1_24h > time2_24h or time1_24h == time2_24h:
        return True
    elif time1_24h < time2_24h :
        return False

def convert_to_24hr(time_str,hr=0):
    # Parse the time string into a datetime object
    time_obj = datetime.strptime(time_str, '%I%p')

    # Add 2 hours to the time
    new_time_obj = time_obj + timedelta(hours=hr)

    # Convert the datetime object back to a string
    new_time_str = new_time_obj.strftime('%#I%p')

    return new_time_str

from datetime import datetime

from datetime import datetime

from datetime import datetime, timedelta


from datetime import datetime, timedelta

def is_time_after(time1, time2):
    # Convert the time strings to datetime objects
    dt_format = '%I%p'
    dt1 = datetime.strptime(time1, dt_format)
    dt2 = datetime.strptime(time2, dt_format)

    # If the second time is before the first time, and it's not midnight,
    # add 12 hours to the second time to handle cases like 11PM and 1AM
    if dt2 < dt1 and dt2.time() != datetime.strptime('12AM', '%I%p').time():
        dt2 += timedelta(hours=12)

    # If the first time is midnight and the second time is before or equal to midnight,
    # add 24 hours to the first time to handle cases like 12AM and 1AM
    if dt1.time() == datetime.strptime('12AM', '%I%p').time() and dt2.time() <= datetime.strptime('12AM', '%I%p').time():
        dt1 += timedelta(hours=24)

    # If the second time is midnight and the first time is before or equal to midnight,
    # subtract 24 hours from the second time to handle cases like 11PM and 12AM
    if dt2.time() == datetime.strptime('12AM', '%I%p').time() and dt1.time() <= datetime.strptime('12AM', '%I%p').time():
        dt2 -= timedelta(hours=24)

    # Check if the second time is after the first time
    return dt2 > dt1

is_time_after('9PM', '1AM')

is_time_after('8PM', '9PM')
is_time_after('11PM', '1AM')
is_time_after('1AM', '11PM')
is_time_after('11PM', '12AM')
is_time_after('12AM', '1AM')
is_time_after('12AM', '11PM')

# False
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
        {"name": "Muizz Street", "location": (30.0057, 31.2454), "opening_time": "9AM", "closing_time": "10PM",
         "city": "cairo"}
    ]
}

breakfast_start = "8AM"
breakfast_end = "12AM"

lunch_start = "12AM"
lunch_end = "6PM"

dinner_start = "6PM"
dinner_end = "11PM"

# Radius of earth in km
R = 6373.0

visited_res = []
visited__attr = []


def plan(city, starting_point, days, start_time, end_time, visited_res, visited__attr):
    breakfast_flag = False
    lunch_flag = False
    dinner_flag = False

    itinerary = []

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
        # Remove already visited places
        sorted_places = [place for place in sorted_places if place not in visited]
        # Insert the closest place at the beginning of the list
        #if closest_place is not None:
            #sorted_places.insert(0, closest_place)

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
        return distance

    for day in range(days):
        while not compare_times(current_time, end_time):
            if (breakfast_flag == False and is_open(breakfast_start,breakfast_end,current_time)):
                closest_places = get_closest_place(restaurants, starting_point, current_time, visited_res)
                for place in closest_places:
                    if (is_open(place["opening_time"],place["closing_time"],current_time)and place not in visited_res):
                        itinerary.append(place)
                        visited_res.append(place)
                        starting_point = place["location"]
                        current_time = convert_to_24hr(current_time,1)
                        breakfast_flag = True
                        if (compare_times(current_time,end_time) == True):
                            return itinerary
                        break
            elif ( lunch_flag == False and is_open(lunch_start,lunch_end,current_time)):

                closest_places = get_closest_place(restaurants, starting_point, current_time, visited_res)
                for place in closest_places:
                    if (is_open(place["opening_time"],place["closing_time"],current_time)and place not in visited_res):
                        itinerary.append(place)
                        visited_res.append(place)
                        starting_point = place["location"]
                        current_time = convert_to_24hr(current_time, 1)
                        lunch_flag = True
                        if (compare_times(current_time,end_time) == True):
                            return itinerary
                        break
            elif ( dinner_flag == False and is_open(dinner_start,dinner_end,current_time)):
                closest_places = get_closest_place(restaurants, starting_point, current_time, visited_res)
                for place in closest_places:
                    if (is_open(place["opening_time"],place["closing_time"],current_time)and place not in visited_res):
                        itinerary.append(place)
                        visited_res.append(place)
                        starting_point = place["location"]
                        current_time = convert_to_24hr(current_time, 1)
                        dinner_flag = True
                        if (compare_times(current_time, end_time) == True):
                            return itinerary
                        break
            closest_places = get_closest_place(attractions, starting_point, current_time, visited__attr)
            for place in closest_places:
                if (is_open(place["opening_time"], place["closing_time"], current_time)and place not in visited__attr):
                    itinerary.append(place)
                    visited__attr.append(place)
                    starting_point = place["location"]
                    current_time = convert_to_24hr(current_time, 2)
                    if (compare_times(current_time, end_time) == True):
                        return itinerary
                    break

            closest_places = get_closest_place(attractions, starting_point, current_time, visited__attr)
            for place in closest_places:
                if (is_open(place["opening_time"], place["closing_time"], current_time) and place not in visited__attr):
                    itinerary.append(place)
                    visited__attr.append(place)
                    starting_point = place["location"]
                    current_time = convert_to_24hr(current_time, 2)
                    if (compare_times(current_time, end_time) == True):
                        return itinerary
                    break


    return itinerary


i = 0
def planmultipledays(days,city,location,no,start_time,end_time,visited_res,visited__attr):
    i = 0
    while i < days:
        itiner2 = plan(city,location,no, start_time,end_time,visited_res,visited__attr)
        print(itiner2)
        i= i +1

planmultipledays(2,"cairo", (30.0444, 31.2357), 1, "8AM", "4PM", visited_res, visited__attr)

