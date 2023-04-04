import pandas as pd
import random


def intersection(lst1, lst2, total_num):
    lst3 = [value for value in lst1 if value in lst2]
    if (len(lst3) == 1):
        return 4
    elif (len(lst3) > 1):
        return 5
    elif (len(lst3) == 0):
        return 0


def user_profile_rest(userID):
    allRestaurants = pd.read_csv('Cairo_Final_Clean_Updated.csv', encoding='latin-1')

    cuisine_types = {1: 'Mediterranean', 2: 'Egyptian', 3: 'Italian', 4: 'Seafood', 5: 'Middle Eastern', 6: 'European',
                     7: 'American', 8: 'Vegetarian Friendly', 9: 'Lebanese', 10: 'Barbecue', 11: 'Japanese',
                     12: 'Healthy', 13: 'Steakhouse',
                     14: 'French', 15: 'International'}
    preferred_cuisine_types = []
    total_num = 0
    randomChoice= random.sample(range(1, 15), 5)
    for i in randomChoice:
        print("choose 5 numbers of your favorite amenities")
        num = i
        print(cuisine_types[num])
        preferred_cuisine_types.append(cuisine_types[num])
        total_num = total_num + 1

    user_id = userID

    user_rating_df = []
    print(preferred_cuisine_types)
    for ind, row in allRestaurants.iterrows():
       if (pd.isna(row[7])):
            continue
       cuisine_types = row[7]
       row_amenities = cuisine_types.split(",")
       #print(row_amenities)
       interValue =intersection(row_amenities, preferred_cuisine_types,total_num)
       if (interValue>0):
           print("append one row")
           user_rating_df.append(
               {
                    'userID': user_id,
                    'restID': row[0],
                    'ratings': interValue,
                    'flag': 'F',
                    'city': row[2]

               }
           )
    return user_rating_df

def intoCSV(user_rating_df):
    #print(pd.DataFrame(user_rating_df))
    pd.DataFrame(user_rating_df).to_csv('user_profiling_rest.csv', index = False, mode='a', header=False)