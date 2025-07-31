"""Objective: create the SQLite database and load test data into it."""

import sqlite3

# creates connection object that represents the database
conn = sqlite3.connect('charts.db')

# creates cursor object for sending queries to the database
cur = conn.cursor()
