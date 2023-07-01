
# import joblib
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS, ALSModel
from pyspark.shell import spark
from pyspark.sql.functions import col, explode
import pickle
import matplotlib.pyplot as plt


def initial_files (csvHotelInfo, csvRatingInfo):
    hotels = spark.read.csv(csvHotelInfo, header=True)
    ratingsSpark = spark.read.option("header", True) \
        .csv(csvRatingInfo)
    # ratingsSpark.show()
    print(ratingsSpark.head())
    return ratingsSpark,hotels

def calculateSparsity(rating):
    # Count the total number of ratings in the dataset
    numerator = rating.select("ratings").count()

    # Count the number of distinct userIds and distinct hotelIds
    num_users = rating.select("user_id").distinct().count()
    num_hotels = rating.select("attraction_id").distinct().count()
    print(str(num_users) + ' users')
    print(str(num_hotels) + ' attra')
    # Set the denominator equal to the number of users multiplied by the number of hotels
    denominator = num_users * num_hotels

    # Divide the numerator by the denominator
    sparsity = (1.0 - (numerator * 1.0) / denominator) * 100
    print("The ratings dataframe is ", "%.2f" % sparsity + "% empty.")

def dataSplit (rating):
    # Group data by userId, count ratings
    # userId_ratings = rating.groupBy("userID").count().orderBy('count', ascending=False)
    # userId_ratings.show()

    # Group data by userId, count ratings
    # hotelId_ratings = rating.groupBy("ID").count().orderBy('count', ascending=False)
    # hotelId_ratings.show()

    rat = rating.select(col("user_id").cast("int").alias("user_id"), col("attraction_id").cast("int").alias("attraction_id"),
                              col("ratings").cast("int").alias("ratings"))
    # rat.printSchema()
    # Create test and train set
    (train, test) = rat.randomSplit([0.8, 0.2])
    return train,test

# we should save here
def MF_ALS (train,test):

    # initial
    ranks = [1,2,3,4,5,6,7,8,9,10]
    min_error = 10
    best_model = None
    ranksUsed=[]
    errors=[]
    for rank in range (1,21):
        als = ALS(maxIter=5, regParam=0.01,rank=rank, userCol="user_id", itemCol="attraction_id", ratingCol="ratings",
                  coldStartStrategy="drop")
        model = als.fit(train)
        predictions = model.transform(test)
        evaluator = RegressionEvaluator(metricName="rmse", labelCol="ratings", predictionCol="prediction")
        rmse = evaluator.evaluate(predictions)
        print('RMSE OUT={}'.format(rmse))
        errors.append(rmse)
        ranksUsed.append(rank)
        print ("Latent factor{}".format(rank))
        print('RMSE OUT={}'.format(rmse))
        if rmse < min_error:
            min_error = rmse
            best_rank = rank
            best_model = model
            print('RMSE IN= {}'.format(min_error))
            print('\nThe best model has {} latent factors'.format(best_rank))

    plt.plot(ranksUsed, errors)
    plt.xlabel("Rank in Model MF ALS")
    plt.ylabel("RMSE Error")
    plt.title("Relationship Between Rank and RMSE Error")
    plt.show()
    return best_model


def recommendations (model,userID,hotels,city):
    userRecs = model.recommendForAllUsers(500)
    nrecommendations = userRecs \
        .withColumn("rec_exp", explode('recommendations')) \
        .select('userID', col("rec_exp.hotelID"), col("rec_exp.rating"))

    nrecommendations.join(hotels, on='hotelID').select('userID','hotelID','name','ratings','longitude','latitude','city')\
        .filter(col('userID') == userID).filter(col('city')==city).orderBy(col('ratings').desc()).show()

    #Ordered by the highest rating
def recommendationsAttract (model,userID,hotels,city):
    userRecs = model.recommendForAllUsers(10)
    nrecommendations = userRecs \
        .withColumn("rec_exp", explode('recommendations')) \
        .select('user_id', col("rec_exp.attraction_id"), col("rec_exp.rating"))

    nrecommendations.join(hotels, on='attraction_id').select('attraction_id','attraction_name','ratings','longitude','latitude','city')\
        .filter(col('user_id') == userID).filter(col('city')==city).orderBy(col('ratings').desc()).show()

    #Ordered by the highest rating


################ TO-DO ##########################
# 2- extract it as an array for the api / or temp csv file
# 4- add a csv for user profiling
############################################################
# TEST CODE FOR HOTELS
csvHotelInfo = r"D:\GP\RecommendationModel\attractions_reccommendation\attractions.csv"
csvRatingInfo = r"D:\GP\RecommendationModel\attractions_reccommendation\user_profiling3010.csv"
#when entering a new user we do have to retrain the entire model
ratingsSpark,hotels = initial_files(csvHotelInfo, csvRatingInfo)
calculateSparsity(ratingsSpark)
train,test= dataSplit(ratingsSpark)
best_model =MF_ALS(train,test)

recommendationsAttract(best_model,1,hotels,'cairo')