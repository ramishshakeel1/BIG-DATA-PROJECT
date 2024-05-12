# Music Recommendation System

## Overview

This project implements a music recommendation system using Apache Spark's machine learning library (MLlib). The recommendation model is built using the Alternating Least Squares (ALS) algorithm, which is a collaborative filtering technique. The system predicts music recommendations based on user listening history, genres, and track popularity.

## Files

1. **Data Preparation Script**
    - **File Name:** data_preparation.py
    - **Description:** Python script for preparing music data by merging tracks data with additional information.
    - **Functionality:**
        - Loads the "tracks.csv" file containing track information.
        - Loads the "features.csv" file containing the features of the tracks.
        -Merges all the data into a new file "data.csv" file which has all the required information of the tracks.
        - Loads the "data.csv" file containing additional data.
        - Merges the "listens" column from the tracks data with the combined data based on track IDs.
        - Saves the final prepared data to a new CSV file.

2. **MongoDB Loader Script**
    - **File Name:** mongodb_loader.py
    - **Description:** Python script for loading prepared data into MongoDB.
    - **Functionality:**
        - Loads the transformed data from the CSV file.
        - Establishes a connection to the MongoDB database.
        - Converts the DataFrame to dictionary format.
        - Inserts the data into a specified MongoDB collection.

3. **Music Recommendation Model Script**
    - **File Name:** music_recommendation_model.py
    - **Description:** Python script implementing the music recommendation model using Apache Spark's MLlib.
    - **Functionality:**
        - Initializes a SparkSession for working with Spark DataFrame.
        - Loads data from MongoDB into a Spark DataFrame, including genres and listens information.
        - Prepares the data by selecting relevant features (genres and listens).
        - Trains the ALS recommendation model with specified hyperparameters.
        - Evaluates the model's performance using Root Mean Squared Error (RMSE) metric.
        - Stops the SparkSession after model training and evaluation.

## Requirements

- Python 3.x
- Apache Spark
- PySpark
- MongoDB Server
- pymongo
- Kafka

## Usage

1. Ensure that Apache Spark and MongoDB are installed and running on your local machine.
2. Run each script in the order to prepare the data, load it into MongoDB, and train the recommendation model.
3. Monitor the script's output for RMSE evaluation results.

## Contributors

- [Ramish Shakeel](21i-1363)
- [Abdul Rehman](21i-1780)

## Frontend for Spotify 

**Introduction:**
The frontend of the Spotify alternative aims to provide users with an intuitive and visually appealing interface for interacting with the music streaming service. It consists of HTML for structure, CSS for styling, and inline styling for quick adjustments. The frontend is designed to be responsive and accessible across different devices.

**HTML Structure:**
The HTML structure consists of multiple pages, including:
1. **Index Page (Home):** Provides an introduction to the Spotify alternative with a call-to-action to sign up or log in.
2. **Register Page:** Allows users to create a new account by providing their username, email, password, date of birth, gender, and accepting terms and conditions.
3. **Login Page:** Enables existing users to log in with their email and password.
4. **Dashboard Page:** Displays the user's dashboard after successful login, showcasing their playlists and providing options to create new playlists or view liked songs.

**CSS Styling:**
The CSS stylesheet (`style.css`) defines the visual appearance of the web pages. It includes styles for:
- Navbar: Styling for the navigation bar, including background color, text color, and alignment.
- Container: Styling for the main content container, including max-width, margin, and padding.
- Buttons: Styling for buttons, including background color, text color, padding, border-radius, and hover effects.
- Landing Section: Styling for the landing section, including background color, padding, and border-radius.
- Playlists: Styling for the playlists section, including grid layout, spacing, background color, padding, and box-shadow.

**Inline Styling:**
Some elements have inline styling for quick adjustments and to ensure proper alignment. Inline styling is primarily used for the navigation bar, search bar, and buttons to align them properly and adjust their appearance as needed.

**Functionality:**
- **Register/Login:** Users can sign up for a new account or log in with existing credentials.
- **Dashboard:** After logging in, users are directed to their dashboard where they can see their playlists. They can also create new playlists or view liked songs.
- **Search Bar:** The search bar allows users to search for songs, artists, or playlists within the Spotify alternative.

**Conclusion:**
The frontend of the Spotify alternative provides users with an intuitive and visually appealing interface for interacting with the music streaming service. It offers essential functionalities such as registration, login, dashboard display, and search functionality. The HTML structure, CSS styling, and inline styling work together to create a cohesive and engaging user experience. Further enhancements and features can be added based on user feedback and requirements.

