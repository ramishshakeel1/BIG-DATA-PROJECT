from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("MusicRecommendationModel") \
    .getOrCreate()

# Load data from MongoDB into Spark DataFrame
# Replace 'your_database_name' and 'your_collection_name' with actual database and collection names
data = spark.read.format("com.mongodb.spark.sql.DefaultSource") \
    .option("uri", "mongodb://localhost:27017/TRACKS_DATABASE.Spotify_collection") \
    .load()

# Prepare data by selecting relevant features (genres and listens)
prepared_data = data.select("genres", "listens")

# Train ALS recommendation model
als = ALS(rank=10, maxIter=10, regParam=0.01, userCol="user_id", itemCol="track_id", ratingCol="listens")
model = als.fit(prepared_data)

# Evaluate the model
predictions = model.transform(prepared_data)
evaluator = RegressionEvaluator(metricName="rmse", labelCol="listens", predictionCol="prediction")
rmse = evaluator.evaluate(predictions)
print("Root Mean Squared Error (RMSE) =", rmse)

# Stop SparkSession
spark.stop()

