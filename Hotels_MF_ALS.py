from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.shell import spark
from pyspark.sql.functions import col, explode

def initial_files (csvHotelInfo, csvRatingInfo):
    hotels = spark.read.csv(csvHotelInfo, header=True)
    ratingsSpark = spark.read.option("header", True) \
        .csv(csvRatingInfo)
    ratingsSpark.select(col("userID").cast('integer').alias("userID"))
    ratingsSpark.show()
    print(ratingsSpark.head())
    return ratingsSpark
def calculateSparsity(rating):
    # Count the total number of ratings in the dataset
    numerator = rating.select("rating").count()

    # Count the number of distinct userIds and distinct hotelIds
    num_users = rating.select("userID").distinct().count()
    num_hotels = rating.select("ID").distinct().count()

    # Set the denominator equal to the number of users multiplied by the number of hotels
    denominator = num_users * num_hotels

    # Divide the numerator by the denominator
    sparsity = (1.0 - (numerator * 1.0) / denominator) * 100
    print("The ratings dataframe is ", "%.2f" % sparsity + "% empty.")

def dataSplit (rating):
    # Group data by userId, count ratings
    userId_ratings = rating.groupBy("userID").count().orderBy('count', ascending=False)
    userId_ratings.show()

    # Group data by userId, count ratings
    hotelId_ratings = rating.groupBy("ID").count().orderBy('count', ascending=False)
    hotelId_ratings.show()

    rat = rating.select(col("userID").cast("int").alias("userID"), col("ID").cast("int").alias("ID"),
                              col("rating").cast("int").alias("rating"))
    rat.printSchema()
    rat.dropna()
    # Create test and train set
    (train, test) = rat.randomSplit([0.8, 0.2])
    return train,test

def MF_ALS (train,test):

    # initial
    ranks = [4, 6, 8, 10, 12]
    min_error = 2
    best_rank = -1
    best_regularization = 0
    best_model = None
    for rank in ranks:
        als = ALS(maxIter=5, regParam=0.01, rank=rank, userCol="userID", itemCol="ID", ratingCol="rating",
                  coldStartStrategy="drop")
        model = als.fit(train)
        predictions = model.transform(test)
        evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
        rmse = evaluator.evaluate(predictions)
        if rmse < min_error:
            min_error = rmse
            best_rank = rank
            best_model = model
            print('\nThe best model has {} latent factors and '
                  'regularization = {}'.format(best_rank, best_regularization))
            print('RMSE={}'.format(min_error))
        return best_model
