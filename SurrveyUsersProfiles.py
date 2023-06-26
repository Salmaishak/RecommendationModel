import pandas as pd
from Restaurants.restaurants_user_profiling import *
from Hotels.initial_user_profiling import *
from attractions_reccommendation.profiling_new_user import *
amenities_dict = {
    'Restaurant': 1,
    'Air conditioning': 2,
    'Laundry service': 3,
    'Room service': 4,
    'Airport transportation': 5,
    'Non-smoking rooms': 6,
    '24-hour front desk': 7,
    'Bar / lounge': 8,
    'Family rooms': 9,
    'Safe': 10,
    'Wifi': 11,
    'Pool': 12,
    'Dry cleaning': 13,
    'Concierge': 14,
    'Children Activities (Kid / Family Friendly)': 15
}

def get_user_amenities():
    # Load Excel sheet into a Pandas dataframe
    df = pd.read_csv('Personalized Travel Recommender.csv')

    # Create an empty dictionary to store the arrays of matching amenities for each user ID
    user_amenities = {}

    # Loop through each row in the dataframe
    for index, row in df.iterrows():
        # Extract the user ID and amenities for the current row
        user_id = row['userID']
        amenities = row['amenities']

        # Split the amenities string into a list of individual amenities
        amenities_list = amenities.split(';')
        print (amenities)

        matching_keys = []

        # Loop through the amenities in the list
        for amenity in amenities_list:
            # Check if the amenity is in the dictionary
            if amenity in amenities_dict:
                # If it is, add the corresponding value (amenity number) to the matching keys list
                matching_keys.append(amenities_dict[amenity])

        # Add the list of matching keys to the user_amenities dictionary
        user_amenities[user_id] = matching_keys

    # Return the dictionary of user amenities
    return user_amenities


# user_amenities_dict = get_user_amenities()
#
#
#
# for key in user_amenities_dict:
#         arr = user_amenities_dict[key]
#         user_profile(arr, key)
# print (user_amenities_dict)

cuisine_types_dict = { 'Mediterranean':1,  'Egyptian':2, 'Italian':3, 'Seafood':4,'Middle Eastern':5,'European':6 ,
                 'American':7,'Vegetarian Friendly':8, 'Lebanese':9, 'Barbecue':10, 'Japanese':11,'Healthy':12,'Steakhouse':13,
                 'French':14,'International':15}

def get_user_cuisine_Types():
    # Load Excel sheet into a Pandas dataframe
    df = pd.read_csv('Personalized Travel Recommender.csv')

    # Create an empty dictionary to store the arrays of matching amenities for each user ID
    user_cusinie_types = {}

    # Loop through each row in the dataframe
    for index, row in df.iterrows():
        # Extract the user ID and amenities for the current row
        user_id = row['userID']
        cusinie_types = row['cuisine types']

        # Split the amenities string into a list of individual amenities
        cusinie_types_list = cusinie_types.split(';')
        print (cusinie_types)

        matching_keys = []

        # Loop through the amenities in the list
        for type in cusinie_types_list:
            # Check if the amenity is in the dictionary
            if type in cuisine_types_dict:
                # If it is, add the corresponding value (amenity number) to the matching keys list
                matching_keys.append(cuisine_types_dict[type])

        # Add the list of matching keys to the user_amenities dictionary
        user_cusinie_types[user_id] = matching_keys

    # Return the dictionary of user amenities
    return user_cusinie_types
#
# user_cusinie_types_dict = get_user_cuisine_Types()
#
#
#
# for key in user_cusinie_types_dict:
#         arr = user_cusinie_types_dict[key]
#         user_profile_restaurant(arr, key)
# print (user_cusinie_types_dict)

attraction_types_dict = {'Museum': 1, 'Park': 2, 'Historical landmark': 3, 'Beach': 4, 'Garden': 5, 'Art Gallery': 6,
                    'Palace': 7, 'Mosque': 8, 'Church': 9, 'Shopping mall': 10, 'Temple': 11, 'Bazar': 12,
                    'island': 13, 'Zoo': 14, 'Library': 15}
def get_user_attraction_types():
    # Load Excel sheet into a Pandas dataframe
    df = pd.read_csv('Personalized Travel Recommender.csv')

    # Create an empty dictionary to store the arrays of matching amenities for each user ID
    user_attraction_types = {}

    # Loop through each row in the dataframe
    for index, row in df.iterrows():
        # Extract the user ID and amenities for the current row
        user_id = row['userID']
        attraction_types = row['attraction types']

        # Split the amenities string into a list of individual amenities
        attraction_types_list = attraction_types.split(';')
        print (attraction_types)

        matching_keys = []

        # Loop through the amenities in the list
        for type in attraction_types_list:
            # Check if the amenity is in the dictionary
            if type in attraction_types_dict:
                # If it is, add the corresponding value (amenity number) to the matching keys list
                matching_keys.append(attraction_types_dict[type])

        # Add the list of matching keys to the user_amenities dictionary
        user_attraction_types[user_id] = matching_keys

    # Return the dictionary of user amenities
    return user_attraction_types

user_attraction_dict = get_user_attraction_types()



for key in user_attraction_dict:
        arr = user_attraction_dict[key]
        profiling_new_user (key, arr)
print (user_attraction_dict)