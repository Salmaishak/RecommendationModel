import pandas as pd



def intersection(lst1, lst2, total_num):
    lst3 = [value for value in lst1 if value in lst2]
    if (len(lst3) == 1):
        return 4
    elif (len(lst3) > 1):
        return 5
    elif (len(lst3) == 0):
        return 0

def user_profile_restaurant(cuisine_input, user_id):
    allRestaurants = pd.read_csv(r'E:\\1.Study Stuff\College\\4th year\GP\TravelRecommeder_Flask\Restaurants\Cairo_FInal_Clean_Updated.csv' ,encoding='latin-1')

    cuisine_types = {1: 'Mediterranean', 2: 'Egyptian', 3: 'Italian', 4:'Seafood', 5:'Middle Eastern',6:'European',
                 7:'American',8:'Vegetarian Friendly', 9:'Lebanese', 10:'Barbecue', 11:'Japanese',12:'Healthy',13:'Steakhouse',
                 14:'French', 15:'International'}

    preferred_cuisine_types = []
    user_input = ''
    total_num = len(cuisine_input)
    for i in cuisine_input:
        preferred_cuisine_types.append(cuisine_types[i])

    # while user_input != 0:
    #     user_input = int(input("Please choose numbers of your favorite cuisine_types (type '0' to exit): "))
    #     if user_input!=0:
    #         print(cuisine_types[user_input])
    #         preferred_cuisine_types.append(cuisine_types[user_input])
    #         total_num = total_num + 1



    # user_id = 1
    user_rating_df = []
    print(preferred_cuisine_types)
    for ind, row in allRestaurants.iterrows():


       if (pd.isna(row[7])):
            continue
       cuisine_types = row[7]
       row_cuisine_types = cuisine_types.split(",")

       interValue = intersection(row_cuisine_types, preferred_cuisine_types,total_num)
       if (interValue > 3):
           user_rating_df.append(
               {
                   'userID': user_id,
                   'restID': row[0],
                   'ratings': interValue,
                   'flag': 'F',
                   'city': row[2]

               }
           )

    print(pd.DataFrame(user_rating_df))
    pd.DataFrame(user_rating_df).to_csv('user_profiling_rest.csv', index = False, mode='a',header=False)
# user_profile()