import pandas as pd
import random


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return len(lst3)


def user_profile(userID):
    allhotels = pd.read_csv('../Allhotels.csv', encoding='latin-1')

    amenities = {1: 'Restaurant', 2: 'Air conditioning', 3: 'Laundry service', 4:'Room service', 5:'Airport transportation',6:'Non-smoking rooms',
                 7:'24-hour front desk',8:'Bar / lounge', 9:'Family rooms', 10:'Safe', 11:'Wifi',12:'Pool',13:'Dry cleaning',
                 14:'Concierge', 15:'Children Activities (Kid / Family Friendly)'}

    preferred_amenities =[]
    randomChoice= random.sample(range(1, 15), 5)
    for i in randomChoice:
        print("choose 5 numbers of your favorite amenities")
        num = i
        print(amenities[num])
        preferred_amenities.append(amenities[num])

    user_id = userID
    user_rating_df = []
    print(preferred_amenities)
    for ind, row in allhotels.iterrows():
       if (pd.isna(row[4])):
            continue
       amenities = row[4]
       row_amenities = amenities.split(",")
       #print(row_amenities)
       interValue =intersection(row_amenities, preferred_amenities)
       if (interValue>0):
           user_rating_df.append(
               {
                   'user_id': user_id,
                   'hotel_id': row[0],
                   'rating': interValue,
                   'flag': 'F',
                   'city':row[7]

               }
           )
    return user_rating_df

def intoCSV(user_rating_df):
    #print(pd.DataFrame(user_rating_df))
    pd.DataFrame(user_rating_df).to_csv('user_profiling307.csv', index = False, mode='a', header=False)
