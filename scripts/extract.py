# %%

def extract():
    pass


# ready_countries() function
# --------------------------
def ready_countries():
    pass

""" Objective: Create the data structure that will hold the forthcoming API responses. Iterate through the countries found in the country table in the database to be then fed into the Get Charts() API call.
"""

import sqlite3
import pandas as pd

# %%
conn = sqlite3.connect('db/test.db')
cur = conn.cursor()

# %%
# Retrieve country code list from database.
countries_list = pd.read_sql_query(
    "SELECT country_code FROM country",
    conn
)


# %%

# YOUTUBE MUSIC
# get_chart_data() function
# -------------------------
def get_chart_data():
    pass

""" Objective: Using the country code list from the database, iterate over each country as arguments into the Get_Charts YTMusic API call, parse each response, and store the relevant metrics.
"""

# %%
from ytmusicapi import YTMusic, OAuthCredentials
import jmespath       

ytmusic = YTMusic()

# %%
# --- Top 10 Artists ---

# Retrieves YouTube Music charts
yt_charts_response = ytmusic.get_charts(countries_list.iat[0, 0]) # 'US' for USA #SUCCESS


# %%
yt_top_artists = jmespath.search("artists[0:10].title", yt_charts_response) #SUCCESS

# %%
# Convert artists list to dataframe

yt_top_artists = pd.DataFrame(
    yt_top_artists,
    columns = ['artist_name']
) #SUCCESS

# %%
# Adds rank column with ranks
yt_top_artists["artist_rank"] = range(1,11) #SUCCESS


# %%
# Adds country code column
yt_top_artists["country_code"] = countries_list.iat[0, 0]



# %%
# SPOTIFY

# get_spotify_id function
# -----------------------

def get_spotify_id():

    pass

import spotipy
import os
from dotenv import load_dotenv, dotenv_values
from spotipy.oauth2 import SpotifyClientCredentials

dotenv_path = ".env"
load_dotenv(dotenv_path=dotenv_path)

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# %%
auth_manager = SpotifyClientCredentials(
    client_id = SPOTIFY_CLIENT_ID,
    client_secret = SPOTIFY_CLIENT_SECRET
)
sp = spotipy.Spotify(auth_manager = auth_manager)

# %%

""" for loop
1) search artist i from 'yt_top_artists'
2) retrieve 'name', 'id', 'popularity' and 'images[1].url' from top hit (assumes top hit is correct)
3) append these attributes to dataframe
4) repeat 
"""
# Duplicates and creates dataframe with top artists to add Spotify data
top_artists = yt_top_artists


# Retrieve and append all artist metrics to dataframe
artist_ids = []
artist_popularity_scores = []
artist_image_urls = []
artist_spotify_urls = []

for i in range(0,10):
    # Retrieves artist information from search
    sp_search_artist_response = sp.search(
        q = top_artists.iat[i, 0],
        limit = 1,
        type = "artist"
    ) 

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

# Appends data lists from above to the dataframe
top_artists["spotify_artist_id"] = artist_ids
top_artists["spotify_popularity"] = artist_popularity_scores
top_artists["spotify_image_url"] = artist_image_urls
top_artists["spotify_artist_preview_url"] = artist_spotify_urls

#TODO build loop encompassing above loop for each country
#TODO build load process into loop
