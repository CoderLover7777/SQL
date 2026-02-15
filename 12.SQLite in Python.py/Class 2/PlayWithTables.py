import sqlite3
database = 'database.sqlite'
conn = sqlite3.connect(database)
print('Opened data successfully')
import pandas as pd
tables = pd.read_sql("""SELECT * 
                     FROM sqlite_master
                     WHERE type='table';""", conn)
tables
teams = pd.read_sql("""SELECT * 
                    FROM Team,""", conn)
teams
matches =pd.read_sql("""SELECT *
                    FROM Match;""", conn)
matches
MI_wins = pd.read_sql("""SELECT * 
                      FROM Match
                      WHERE Match_winner == 7;""", conn)
MI_wins
MI_S8_S9 = pd.read_sql("""SELECT *
                       FROM Match
                      WHERE)