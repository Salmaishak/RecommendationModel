from Restaurants_MF_ALS import *


def recommend_restaraurnat(user_id, city):
    csvRestaurantInfo = "Allrestaurants2.csv"
    csvRatingInfo = 'user_profiling_rest.csv'
    ratingsSpark, restaurants = initial_files_Rest(csvRestaurantInfo, csvRatingInfo)
    calculateSparsityRest(ratingsSpark)
    timesCsv = r"D:\GP\RecommendationModel\Restaurants\Allrestaurants3.csv"
    train, test = dataSplit_Rest(ratingsSpark)
    timesSpark = spark.read.csv(timesCsv, header=True)
    best_model = MF_ALS_Rest(train, test)
    print("-----------------")
    print(best_model)
    return recommendationsRestPlan(best_model,user_id,restaurants, city,timesSpark)



print(recommend_restaraurnat(1,"Cairo"))
