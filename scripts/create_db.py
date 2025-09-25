"""Objective: create the SQLite database and load test data into it."""

# %%
import sqlite3
import pandas as pd


# TEST DATABASE CREATION  -------------------------------------------------------------------

# %%
# creates connection object that represents the database
conn = sqlite3.connect('db/test.db')

# creates cursor object for sending queries to the database
cur = conn.cursor()

# %%
# import test data tables
df_artist = pd.read_csv("data/test_artist.csv")
df_country = pd.read_csv("data/test_country.csv")
df_track = pd.read_csv("data/test_track.csv")
df_time = pd.read_csv("data/time_table.csv")

#%%
# insert test data as tables into database
df_artist.to_sql(
    'artist', 
    conn, 
    if_exists = 'replace', 
    index = False
)

df_country.to_sql(
    'country', 
    conn, 
    if_exists = 'replace', 
    index = False
)

df_track.to_sql(
    'track', 
    conn, 
    if_exists = 'replace', 
    index = False
)

df_time.to_sql(
    'time', 
    conn, 
    if_exists = 'replace', 
    index = False
)

# %%
# test queries
testqueries = [
    "SELECT * FROM artist LIMIT 1;",
    "SELECT * FROM country LIMIT 1;",
    "SELECT * FROM track LIMIT 1;",
    "SELECT * FROM time LIMIT 1;"
]


# %%
pd.read_sql_query(
    "SELECT * FROM country LIMIT 10",
    conn
) # success

# %%
pd.read_sql_query(
    "SELECT spotify_artist_id FROM artist WHERE artist_name = 'Sabrina Carpenter'",
    conn
) # success