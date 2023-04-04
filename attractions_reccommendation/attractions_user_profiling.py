import pandas as pd



def intersection(category, lst1):
   if category in lst1:
       return True
   else:
       return False


def user_profile(user_id):
    attractions = pd.read_csv('G:\\Fourth Year\\GP\\RecommendationModel\\attractions_reccommendation\\attractions.csv', encoding ='latin1')

    categories = {1: 'Museum', 2: 'Park', 3: 'Historical landmark', 4:'Beach', 5:'Garden',6:'Art Gallery',
                 7:'Palace',8:'Mosque', 9:'Church', 10:'Shopping mall'}

    preferred_categories = []
    for i in range(5):
        print("choose 5 numbers of your favorite attraction categories: ")
        num = int(input("Enter the number of requested attraction: "))
        # print(categories[num])
        preferred_categories.append(categories[num])


    user_rating_df = []
    # print(preferred_categories)
    for ind, row in attractions.iterrows():
       # print("Row: ")
       # print(row)
       category = row[4]
       # print(category)
       if(intersection(category, preferred_categories) == True):
           rating = int(5)
       else:
           rating = int(1)
       user_rating_df.append(
          {
              'user_id': user_id,
              'attraction_id': row[0],
              'rating': rating,
              'flag': 'F'
          }
       )

    print(pd.DataFrame(user_rating_df))
    pd.DataFrame(user_rating_df).to_csv('user_profiling_attractions.csv', index = False)

user_profile(1)

