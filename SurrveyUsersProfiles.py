import pandas as pd
from Restaurants.restaurants_user_profiling import *
from Hotels.initial_user_profiling import *
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


user_amenities_dict = get_user_amenities()



for key in user_amenities_dict:
        arr = user_amenities_dict[key]
        user_profile(arr, key)
print (user_amenities_dict)