import pandas as pd



def intersection(lst1, lst2, total_num):
    lst3 = [value for value in lst1 if value in lst2]
    return ((len(lst3)/ total_num) * 5)

def user_profile(amentitiesInput, user_id):
    allhotels = pd.read_csv('D:\GP\RecommendationModel\Hotels\Allhotels.csv' ,encoding='latin-1')

    amenities = {1: 'Restaurant', 2: 'Air conditioning', 3: 'Laundry service', 4:'Room service', 5:'Airport transportation',6:'Non-smoking rooms',
                 7:'24-hour front desk',8:'Bar / lounge', 9:'Family rooms', 10:'Safe', 11:'Wifi',12:'Pool',13:'Dry cleaning',
                 14:'Concierge', 15:'Children Activities (Kid / Family Friendly)'}

    preferred_amenities = []
    total_num = len(amentitiesInput)
    for i in amentitiesInput:
        preferred_amenities.append(amenities[i])



    # user_id = 1
    user_rating_df = []
    print(preferred_amenities)
    for ind, row in allhotels.iterrows():


       if (pd.isna(row[4])):
            continue
       amenities = row[4]
       row_amenities = amenities.split(",")
       #print(row_amenities)
       interValue = intersection(row_amenities, preferred_amenities,total_num)
       if (interValue > 3):
           user_rating_df.append(
               {
                   'userID': user_id,
                   'hotelID': row[0],
                   'ratings': interValue,
                   'flag': 'F',
                   'city': row[7]

               }
           )

    print(pd.DataFrame(user_rating_df))
    pd.DataFrame(user_rating_df).to_csv('user_profiling.csv', index = False, mode='a', header=False)

# user_profile()