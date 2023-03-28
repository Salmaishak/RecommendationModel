from Hotels.Hotels_MF_ALS import *
import pandas as pd

#TEST CODE FOR HOTELS
csvHotelInfo = "Allhotels.csv"
csvRatingInfo = 'user_profiling30.csv'

newUser = []

newUser.append(
               {
                   'user_id': 2709,
                   'hotel_id':3,
                   'rating': 5,
                   'flag': 'F',
                   'city':'Cairo'

               })
pd.DataFrame(newUser).to_csv('Hotels/user_profile_Data/user_profiling30.csv', index=False, mode='a', header=False)
#when entering a new user we do have to retrain the entire model
ratingsSpark,hotels = initial_files(csvHotelInfo, csvRatingInfo)
calculateSparsity(ratingsSpark)
train,test= dataSplit(ratingsSpark)
best_model =MF_ALS(train,test)

recommendations(best_model,2709,hotels,'Giza')

#TEST CODE FOR RESTAURANTS

#TEST CODE FOR ATTRACTIONS 