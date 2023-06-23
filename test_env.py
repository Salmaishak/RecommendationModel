from datetime import datetime

from Hotels.Hotels_MF_ALS import *
from Restaurants.Restaurants_MF_ALS import *
import pandas as pd
# #
#TEST CODE FOR HOTELS
# csvHotelInfo = "Hotels/Allhotels.csv"
# csvRatingInfo = 'Hotels/user_profiling.csv'
# #when entering a new user we do have to retrain the entire model
# ratingsSpark,hotels = initial_files(csvHotelInfo, csvRatingInfo)
# calculateSparsity(ratingsSpark)
# train,test= dataSplit(ratingsSpark)
# best_model =MF_ALS(train,test)
#
# recommendations(best_model,1,hotels,'Cairo')

# # #TEST CODE FOR RESTAURANTS
# csvRestInfo = "Restaurants/Cairo_Final_Clean_Updated.csv"
# csvRatingInfoRest= 'Restaurants/user_profiling_rest.csv'
# #when entering a new user we do have to retrain the entire model
# ratingsSparkRest,rest = initial_files_Rest(csvRestInfo, csvRatingInfoRest)
# calculateSparsityRest(ratingsSparkRest)
# trainR,testR= dataSplit_Rest(ratingsSparkRest)
# best_model =MF_ALS_Rest(trainR,testR)

###########################Plan Preparation#######################################

#get recommendations to
def getRecommendationForPlanRest (userID, City):
    csvRestInfo = "Restaurants/Cairo_Final_Clean_Updated.csv"
    timesCsv = "Restaurants/Allrestaurants3.csv"
    timesSpark = spark.read.csv(timesCsv, header=True)
    csvRatingInfoRest = 'Restaurants/user_profiling_rest.csv'
    # when entering a new user we do have to retrain the entire model
    ratingsSparkRest, rest = initial_files_Rest(csvRestInfo, csvRatingInfoRest)
    calculateSparsityRest(ratingsSparkRest)
    trainR, testR = dataSplit_Rest(ratingsSparkRest)
    best_model = MF_ALS_Rest(trainR, testR)

    df= recommendationsRestPlan(best_model, userID, rest, City,timesSpark)
    return df

restaurants_df= getRecommendationForPlanRest(1,'Cairo')

# restaurants_df.show()

# Import necessary libraries
import pandas as pd

# Load the dataframes
#
# attractions_df = pd.read_csv('attractions.csv')

# Convert time format from "09:00AM" to "9AM"
# Convert time format for each value in the 'open_time' column
from datetime import datetime
restaurants_df_pandas= restaurants_df.toPandas()
# Define a function to convert time format
def convert_time_format(time_str):
    time_obj = datetime.strptime(time_str, '%I:%M%p')
    return time_obj.strftime('%I%p')

# Apply the function to the 'open_time' column
restaurants_df_pandas['open_time'] = restaurants_df_pandas['open_time'].apply(convert_time_format).str.replace('^0', '', regex=True)

# Apply the function to the 'close_time' column
restaurants_df_pandas['close_time'] = restaurants_df_pandas['close_time'].apply(convert_time_format).str.replace('^0', '', regex=True)

# Display the updated dataframe
print(restaurants_df_pandas)
# attractions_df['opening_time'] = pd.to_datetime(attractions_df['opening_time']).dt.strftime('%-I%p')
# attractions_df['closing_time'] = pd.to_datetime(attractions_df['closing_time']).dt.strftime('%-I%p')

# Create a dictionary to store the data
data = {
    "restaurants": [],
    "attractions": []
}

# Extract information from restaurants dataframe and add to dictionary
for _, row in restaurants_df_pandas.iterrows():
    restaurant = {
        "name": row['name'],
        "location": (row['latitude'], row['longitude']),
        "open_time": row['open_time'],
        "close_time": row['close_time'],
        "city": row['city']
    }
    data['restaurants'].append(restaurant)
print (data)
# Extract information from attractions dataframe and add to dictionary
# for _, row in attractions_df.iterrows():
#     attraction = {
#         "name": row['name'],
#         "location": (row['latitude'], row['longitude']),
#         "opening_time": row['opening_time'],
#         "closing_time": row['closing_time'],
#         "city": row['city']
#     }
#     data['attractions'].append(attraction)
#CODE TO REPLACE NULL IN ALL RESTAURANTS

# timesCsv = "Restaurants/Allrestaurants.csv"
# timesSpark = spark.read.csv(timesCsv, header=True)
# timesSpark= timesSpark.na.fill({'open_time':'09:00AM'})
# timesSpark= timesSpark.na.fill({'close_time':'12:00AM'})
# pandas_df = timesSpark.toPandas()
# pandas_df.to_csv('Allrestaurants3.csv', index=False)