import pandas as pd
from pymongo import MongoClient

# Load the transformed data
transformed_data = pd.read_csv("data.csv")

# MongoDB connection information
mongodb_url = "mongodb://localhost:27017/"
database_name = "TRACKS_DATABASE"
collection_name = "Spotify_collection"

# Connect to MongoDB
client = MongoClient(mongodb_url)
db = client[database_name]

# Convert DataFrame to dictionary format
data_dict = transformed_data.to_dict(orient='records')

# Insert data into MongoDB collection
collection = db[collection_name]
collection.insert_many(data_dict)

print("Data successfully loaded into MongoDB collection.")
