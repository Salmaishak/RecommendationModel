from Hotels_MF_ALS import *

csvHotelInfo = "Allhotels.csv"
csvRatingInfo = 'trialdata.csv'
ratingsSpark,hotels = initial_files(csvHotelInfo, csvRatingInfo)
calculateSparsity(ratingsSpark)
train,test= dataSplit(ratingsSpark)
best_model =MF_ALS(train,test)
recommendations(best_model,660,hotels)