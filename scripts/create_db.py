def create_db():
    pass

"""Objective: create the SQLite database and load data into it."""

# %%
import sqlite3
import pandas as pd


# %%
# Creates connection object that represents the database
conn = sqlite3.connect('db/charts_database.db')

# Creates cursor object for sending queries to the database
cur = conn.cursor()

create_artist_table = """
CREATE TABLE IF NOT EXISTS artist (
    spotify_artist_id   TEXT NOT NULL,
    week_ending         TEXT NOT NULL,
    country_code        TEXT NOT NULL,
    artist_name         TEXT,
    artist_rank      INTEGER,
    artist_popularity   INTEGER,
    artist_image_url    TEXT,
    artist_preview_url  TEXT,
    PRIMARY KEY (spotify_artist_id, week_ending, country_code)
);
"""
conn.execute(create_artist_table)
conn.commit()

# %%
# Imports static data tables
df_country = pd.read_csv("data/country_table.csv") 
df_time = pd.read_csv("data/time_table.csv")

#%%
# Inserts test data as tables into database
df_country.to_sql(
    'country', 
    conn, 
    if_exists='replace', 
    index=False
)

df_time.to_sql(
    'time', 
    conn, 
    if_exists='replace', 
    index=False
)
