from Hotels_MF_ALS import *

csvHotelInfo = "Allhotels.csv"
csvRatingInfo = 'user_profiling3.csv'
ratingsSpark,hotels = initial_files(csvHotelInfo, csvRatingInfo)
calculateSparsity(ratingsSpark)
train,test= dataSplit(ratingsSpark)
best_model =MF_ALS(train,test)
recommendations(best_model,1,'Giza',hotels)