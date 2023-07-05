import pandas as pd
import random


def intersection(lst1, lst2):
    if lst1 in lst2:
        return True
    else:
        return False


def user_profile(userID):
    attractions = pd.read_csv('attractions.csv', encoding='latin-1')

    attraction_types = {1: 'Museum', 2: 'Park', 3: 'Historical landmark', 4: 'Beach', 5: 'Garden', 6: 'Art Gallery',
                        7: 'Palace', 8: 'Mosque', 9: 'Church', 10: 'Shopping mall', 11: 'Temple', 12: 'Bazar',
                        13: 'island', 14: 'Zoo', 15: 'Library'}

    preferred_types = []
    randomChoice = random.sample(range(1, 15), 5)
    for i in randomChoice:
        print("choose 5 numbers of your favorite attraction types")
        num = i
        print(attraction_types[num])
        preferred_types.append(attraction_types[num])

    user_id = userID
    user_rating_df = []
    print(preferred_types)

    for ind, col in attractions.iterrows():
        if pd.isna(col[4]):
            continue
        attraction_types = col[4]
        # row_attractions = attraction_types.split(",")
        # print(row_attractions)

        if intersection(attraction_types, preferred_types):
            rating = col[2]
        else:
            rating = int(1)
        if rating > 1:
            user_rating_df.append(
                {
                    'user_id': user_id,
                    'attraction_id': col[0],
                    'rating': rating,
                    'flag': 'F',
                    'city': col[8]

                }
            )
    return user_rating_df


def intoCSV(user_rating_df):
    # print(pd.DataFrame(user_rating_df))
    pd.DataFrame(user_rating_df).to_csv('user_profiling100.csv', index=False, mode='a', header=False)


df = []
for x in range(1, 101):
    df = user_profile(x)
    # print(x)
    intoCSV(df)
