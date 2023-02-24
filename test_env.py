from Hotels_MF_ALS import *

csvHotelInfo = "Allhotels.csv"
csvRatingInfo = 'trialdata.csv'
ratingsSpark = initial_files(csvHotelInfo, csvRatingInfo)
calculateSparsity(ratingsSpark)
train,test= dataSplit(ratingsSpark)
MF_ALS(train,test)