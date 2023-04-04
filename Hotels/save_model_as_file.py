import pickle
from Hotels.Hotels_MF_ALS import *
import pandas as pd

#TEST CODE FOR HOTELS
csvHotelInfo = "Allhotels.csv"
csvRatingInfo = 'user_profiling.csv'

newUser = []

newUser.append(
               {
                   'user_id': 2709,
                   'hotel_id':3,
                   'rating': 5,
                   'flag': 'F',
                   'city':'Cairo'

               })
pd.DataFrame(newUser).to_csv('ay_haga.csv', index=False, mode='a', header=False)
#when entering a new user we do have to retrain the entire model
ratingsSpark,hotels = initial_files(csvHotelInfo, csvRatingInfo)
calculateSparsity(ratingsSpark)
train,test= dataSplit(ratingsSpark)
best_model =MF_ALS(train,test)

# recommendations(best_model,1,hotels,'Al-Fayyum')

#TEST CODE FOR RESTAURANTS

#TEST CODE FOR ATTRACTIONS
# Train your model
model = best_model

# Save your model
# import dill
# with open('model.pkl', 'wb') as f:
#     dill.dump(model, f)


from pyspark.ml.recommendation import ALS
from pyspark.sql import SparkSession

# create a SparkSession
spark = SparkSession.builder.appName("ALS Example").getOrCreate()

# load data and train ALS model
data = spark.read.load("data/sample_movielens_ratings.txt", format="csv", header=True, inferSchema=True)
als = ALS(rank=10, maxIter=5, seed=0)
model = als.fit(data)

# save the model as an ALS file
model.save("als_model")
