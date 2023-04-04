from Restaurants_MF_ALS import *


def recommend_restaraurnat(user_id, city):
    csvRestaurantInfo = "Cairo_Final_Clean_Updated.csv"
    csvRatingInfo = 'user_profiling_rest.csv'
    ratingsSpark, restaurants = initial_files_Rest(csvRestaurantInfo, csvRatingInfo)
    calculateSparsityRest(ratingsSpark)
    train, test = dataSplit_Rest(ratingsSpark)

    best_model = MF_ALS_Rest(train, test)
    print("-----------------")
    print(best_model)
    return recommendationsRest(best_model,user_id,restaurants, city)



print(recommend_restaraurnat(1,"Cairo"))
