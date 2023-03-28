import pandas as pd



def intersection(lst1, lst2, total_num):
    lst3 = [value for value in lst1 if value in lst2]
    return ((len(lst3)/ total_num) * 5)

def user_profile():
    allhotels = pd.read_csv('Allhotels.csv')

    amenities = {1: 'Restaurant', 2: 'Air conditioning', 3: 'Laundry service', 4:'Room service', 5:'Airport transportation',6:'Non-smoking rooms',
                 7:'24-hour front desk',8:'Bar / lounge', 9:'Family rooms', 10:'Safe', 11:'Wifi',12:'Pool',13:'Dry cleaning',
                 14:'Concierge', 15:'Children Activities (Kid / Family Friendly)'}

    preferred_amenities = []
    user_input = ''
    total_num = 0
    while user_input != '0':
        num = int(input("Please choose numbers of your favorite amenities (type '0' to exit): "))
        print(amenities[num])
        preferred_amenities.append(amenities[num])
        total_num = total_num + 1



    user_id = 1
    user_rating_df = []
    print(preferred_amenities)
    for ind, row in allhotels.iterrows():


       if (pd.isna(row[4])):

            user_rating_df.append(
                {
                    'user_id' : user_id,
                    'hotel_id' : row[0],
                    'rating' : int(0),
                    'flag': 'F'

                }
            )
            continue

       amenities = row[4]
       row_amenities = amenities.split(",")
       #print(row_amenities)
       user_rating_df.append(
           {
               'user_id': user_id,
               'hotel_id': row[0],
               'rating': intersection(row_amenities, preferred_amenities),
               'flag': 'F'

           }
       )

    print(pd.DataFrame(user_rating_df))
    pd.DataFrame(user_rating_df).to_csv('user_profiling.csv', index = False)

user_profile()