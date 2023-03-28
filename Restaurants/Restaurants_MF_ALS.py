import joblib
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS, ALSModel
from pyspark.shell import spark
from pyspark.sql.functions import col, explode
import pickle


def initial_files_Rest (csvRestaurantsInfo, csvRatingInfo):
    restaurants = spark.read.csv(csvRestaurantsInfo, header=True)
    ratingsSpark = spark.read.option("header", True) \
        .csv(csvRatingInfo)
    # ratingsSpark.show()
    print(ratingsSpark.head())
    return ratingsSpark,restaurants

def calculateSparsityRest(rating):
    # Count the total number of ratings in the dataset
    numerator = rating.select("ratings").count()

    # Count the number of distinct userIds and distinct hotelIds
    num_users = rating.select("userID").distinct().count()
    num_hotels = rating.select("restID").distinct().count()
    print(str(num_users) + ' users')
    print(str(num_hotels) + ' restaurants')
    # Set the denominator equal to the number of users multiplied by the number of hotels
    denominator = num_users * num_hotels

    # Divide the numerator by the denominator
    sparsity = (1.0 - (numerator * 1.0) / denominator) * 100
    print("The ratings dataframe is ", "%.2f" % sparsity + "% empty.")

def dataSplit_Rest(rating):
    # Group data by userId, count ratings
    # userId_ratings = rating.groupBy("userID").count().orderBy('count', ascending=False)
    # userId_ratings.show()

    # Group data by userId, count ratings
    # hotelId_ratings = rating.groupBy("ID").count().orderBy('count', ascending=False)
    # hotelId_ratings.show()

    rat = rating.select(col("userID").cast("int").alias("userID"), col("restID").cast("int").alias("restID"),
                              col("ratings").cast("int").alias("ratings"))
    # rat.printSchema()
    # Create test and train set
    (train, test) = rat.randomSplit([0.8, 0.2])
    return train,test

def MF_ALS_Rest (train,test):

    # initial
    ranks = [6,7,8,9,10,1,2,3,4,5]
    min_error = 0.5
    best_model = None

    for rank in ranks:
        als = ALS(maxIter=5, regParam=0.01,rank=rank, userCol="userID", itemCol="restID", ratingCol="ratings",
                  coldStartStrategy="drop")
        model = als.fit(train)
        predictions = model.transform(test)
        evaluator = RegressionEvaluator(metricName="rmse", labelCol="ratings", predictionCol="prediction")
        rmse = evaluator.evaluate(predictions)
        print('RMSE OUT={}'.format(rmse))

        if rmse < min_error:
            min_error = rmse
            best_rank = rank
            best_model = model
            print('RMSE IN= {}'.format(min_error))
            print('\nThe best model has {} latent factors'.format(best_rank))
            return best_model


def recommendationsRest (model,userID,rest,city):
    userRecs = model.recommendForAllUsers(500)
    nrecommendations = userRecs \
        .withColumn("rec_exp", explode('recommendations')) \
        .select('userID', col("rec_exp.restID"), col("rec_exp.rating"))

    nrecommendations.join(rest, on='restID').select('userID','restID','name','ratings','longitude','latitude','city')\
        .filter(col('userID') == userID).filter(col('city')==city).orderBy(col('ratings').desc()).show()

    #Ordered by the highest rating


################ TO-DO ##########################
# 2- extract it as an array for the api / or temp csv file
# 4- add a csv for user profiling
############################################################
