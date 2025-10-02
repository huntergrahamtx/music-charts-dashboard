# %%
# FIND LAST COMPLETED SATURDAY
import pandas as pd

# Today's date
today = pd.Timestamp.today().normalize()

# Finds latest Saturday
last_completed_saturday = pd.tseries.offsets.Week(weekday=5).rollback(today)

# If today is Saturday, adjusts to use last Saturday's date
if ts.weekday() == 5:
    last_completed_saturday -= pd.Timedelta(days=7)

# Converts timestamp to string with YYYY-MM-DD time formatting
week_ending_date = last_completed_saturday.strftime("%Y-%m-%d")

# %%
# API DATA EXTRACTION

# Placeholder functions for future refactoring
def extract():
    pass

def ready_countries():
    pass

""" Objective: Create the data structure that will hold the forthcoming API responses. Iterate through the countries found in the country table in the database to be then fed into the Get Charts() API call.
"""

# %%
import sqlite3

conn = sqlite3.connect('db/charts_database.db')
cur = conn.cursor()

# Retrieve country code list from database.
countries_list = pd.read_sql_query(
    "SELECT country_code FROM country",
    conn
)
# Retrieves 'artist' table attribute names for coming dataframe
artist_columns = pd.read_sql_query(
    "PRAGMA table_info(artist)",
    conn
)

# Remove all other fields besides the names of the table attributes
artist_columns = artist_columns["name"]

# Creates empty dataframe for loop 
df_artists_temp = pd.DataFrame(columns=artist_columns)

# Adds `rank` column with ranks
df_artists_temp["artist_rank"] = range(1,11)

# Adds `week_ending` date
df_artists_temp["week_ending"] = week_ending_date

# %%
from ytmusicapi import YTMusic, OAuthCredentials
import jmespath
import time

# Placeholder functions for future refactoring
def get_chart_data():
    pass

""" Objective: Using the country code list from the database, iterate over each country as arguments into the Get_Charts YTMusic API call, parse each response, and store the relevant metrics.
"""

ytmusic = YTMusic()

# %%
# ARTIST DATA

# Create dictionary of DataFrames to store all artist data extracted
data_artists = {}

# YouTubeMusic API data extraction loop
for i in range(0, len(countries_list)):

    # Extracts country_code
    country_code = countries_list.iat[i, 0]
    
    # Copies DataFrame template to loop
    df_artists = df_artists_temp

    # Writes current country code to DataFrame
    df_artists["country_code"] = country_code
    
    # Retrieves YouTube Music charts response
    try:
        yt_charts_response = ytmusic.get_charts(countries_list.iat[i, 0])
        print(countries_list.iat[i, 0], "YouTube Music response was successful.")

    except: 
        print(print(countries_list.iat[i, 0], "YouTube Music response FAILED."))
        continue

    # Selects just artist names
    df_artists["artist_name"] = jmespath.search("artists[0:10].title", yt_charts_response)

    # Copy extracted data to artist dictionary
    data_artists[country_code] = df_artists.copy()

    # Print country executed to output
    print(countries_list.iat[i, 0], "YouTube Music chart successfuly extracted.")

    # Courtesy delay
    time.sleep(0.3)


# %%
# SPOTIFY

# Placeholder functions for future refactoring
def get_spotify_id():
    pass

import spotipy
import os
from dotenv import load_dotenv, dotenv_values
from spotipy.oauth2 import SpotifyClientCredentials

dotenv_path = ".env"
load_dotenv(dotenv_path=dotenv_path)

# Load and authorize Spotify credentials + `spotipy` package
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
)

sp = spotipy.Spotify(auth_manager = auth_manager)

# %%

# Extracts Spotify artist metrics and adds data to country DataFrame in dictionary
for country in data_artists.keys():

    # Creates empty data lists for loop
    artist_ids = []
    artist_popularity_scores = []
    artist_image_urls = []
    artist_spotify_urls = []

    for j in range(0,10):
        # Retrieves artist information from search
        try:
            sp_search_artist_response = sp.search(
                q=data_artists[country]["artist_name"].loc[j],
                limit=1,
                type="artist"
            )
            # Prints confirmation
            print(
                "Spotify artist data for YouTube Music country",
                country,
                ", artist number",
                 j + 1,
                 "successfully extracted."
            )
        
        except:
            print(country, "Spotify artist search request FAILED.")
            continue

        # Parses response for 'artist id' and appends to artist ID list
        sp_artist_id = jmespath.search(
            "artists.items[0].id",
            sp_search_artist_response
        )

        artist_ids.append(sp_artist_id)

        # Parses response for 'popularity' and appends to popularity score list
        sp_popularity_score = jmespath.search(
            "artists.items[0].popularity",
            sp_search_artist_response
        )

        artist_popularity_scores.append(sp_popularity_score)

        # Parses response for artist image URL and appends to artist image URL list
        sp_artist_image_url = jmespath.search(
            "artists.items[0].images[1].url",
            sp_search_artist_response
        )

        artist_image_urls.append(sp_artist_image_url)

        # Parses response for artist Spotify preview URL and appends to artist Spotify preview URL list
        sp_artist_spotify_url = jmespath.search(
            "artists.items[0].external_urls.spotify",
            sp_search_artist_response
        )

        artist_spotify_urls.append(sp_artist_spotify_url)

        # Courtesy delay
        time.sleep(0.3)

    # Appends data lists from above loop to the dataframe
    data_artists[country]["spotify_artist_id"] = artist_ids
    data_artists[country]["artist_popularity"] = artist_popularity_scores
    data_artists[country]["artist_image_url"] = artist_image_urls
    data_artists[country]["artist_preview_url"] = artist_spotify_urls



# %%
# Loads artist data into database
for country in data_artists.keys():
    data_artists[country].to_sql(
        'artist', 
        conn, 
        if_exists='append', 
        index=False
    ) 
# %%
# EXPORT CHART DATA FOR DASHBOARD
# Reads 'artist' table from database
artist_export_data = pd.read_sql(
    "SELECT * FROM artist",
    conn)

# Exports pulled artist data to .csv file
artist_export_data.to_csv(
    "data/artist_data.csv",
    index=False,
    encoding="utf-8-sig") # Corrects diacritics not being represented correctly