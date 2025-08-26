# %%
def extract():
    pass

# ------- ALL BELOW FUNCTIONS TO BE PLACED INSIDE extract() ----------

# ready_countries() function ------------------------------
def ready_countries():
    pass

""" Objective: Create the data structure that will hold the forthcoming API responses. Iterate through the countries found in the country table in the database to be then fed into the Get Charts() API call.
"""

import sqlite3
import pandas as pd


# %%
conn = sqlite3.connect('test.db')
cur = conn.cursor()

# %%
# retrieve country code list from database
countries_list = pd.read_sql_query("SELECT country_code FROM country",
                                   conn)



# get_chart_data() function -----------------------------------
def get_chart_data():
    pass

""" Objective: Using the country code list from the database, iterate over each country as arguments into the Get_Charts YTMusic API call, parse each response, and store the relevant metrics.
"""
# %%
# setup .env file for accessing API keys
import os
from dotenv import load_dotenv, dotenv_values
dotenv_path = "c:\\Users\\seize\\OneDrive\\Documents\\My Documents\\Programming\\GitHub\\music-charts-dashboard\\API keys.env"
load_dotenv(dotenv_path=dotenv_path)
google_client_id = os.getenv("GOOGLE_CLIENT_ID")
google_client_secret = os.getenv("GOOGLE_CLIENT_SECRET")


# TODO
# i) point Python to root folder directory, not /scripts/
# ii) turn hard-coded directories into relative directories
# iii) update Python
# %%
from ytmusicapi import YTMusic, OAuthCredentials

ytmusic = YTMusic('oauth.json', oauth_credentials=OAuthCredentials(client_id=google_client_id, client_secret=google_client_secret))
                  
# %%
# test search
search_results = ytmusic.search("Oasis Wonderwall")