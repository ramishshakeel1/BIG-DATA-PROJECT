import pandas as pd

# Load the "tracks.csv" file and extract the "listens" column
tracks_file = "tracks.csv"
tracks_data = pd.read_csv(tracks_file, dtype=str)  # Specify data type as string for all columns
listens_column = tracks_data["listens"]

# Load the "final_combined_data.csv" file
final_combined_file = "final_combined_data.csv"
final_combined_data = pd.read_csv(final_combined_file)

# Merge the "listens" column with the "final_combined_data.csv" file based on "track_id"
final_data = pd.merge(final_combined_data, tracks_data[["track_id", "listens"]], on="track_id", how="left")

# Save the final data to a new CSV file
final_data.to_csv("data.csv", index=False)

print("Final data saved to final.csv")

