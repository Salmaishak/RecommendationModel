from Hotels.Hotels_MF_ALS import *
from Restaurants.Restaurants_MF_ALS import *
import pandas as pd
#
# #TEST CODE FOR HOTELS
# csvHotelInfo = "Hotels/Allhotels.csv"
# csvRatingInfo = 'Hotels/user_profiling.csv'
# #when entering a new user we do have to retrain the entire model
# ratingsSpark,hotels = initial_files(csvHotelInfo, csvRatingInfo)
# calculateSparsity(ratingsSpark)
# train,test= dataSplit(ratingsSpark)
# best_model =MF_ALS(train,test)
#
# recommendations(best_model,1,hotels,'Al-Fayyum')

#TEST CODE FOR RESTAURANTS
csvRestInfo = "Restaurants/Cairo_Final_Clean_Updated.csv"
csvRatingInfoRest= 'Restaurants/user_profiling_rest.csv'
#when entering a new user we do have to retrain the entire model
ratingsSparkRest,rest = initial_files_Rest(csvRestInfo, csvRatingInfoRest)
calculateSparsityRest(ratingsSparkRest)
trainR,testR= dataSplit_Rest(ratingsSparkRest)
best_model =MF_ALS_Rest(trainR,testR)

recommendationsRest(best_model,1,rest,'Cairo')
#TEST CODE FOR ATTRACTIONS