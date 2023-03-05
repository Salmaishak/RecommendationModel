from Hotels_MF_ALS import *
from pyspark.ml.recommendation import ALS, ALSModel

csvHotelInfo = "Allhotels.csv"
csvRatingInfo = 'user_profiling30.csv'
ratingsSpark,hotels = initial_files(csvHotelInfo, csvRatingInfo)
calculateSparsity(ratingsSpark)
train,test= dataSplit(ratingsSpark)
best_model =MF_ALS(train,test)
recommendations(best_model,1,hotels,'Giza')