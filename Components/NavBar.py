import dash_bootstrap_components as dbc
from dash import html, dcc
import sqlite3
import dash

### Set Options ###
connection = sqlite3.connect('./Data/LSRDB.db')
cursor = connection.cursor()
cursor.execute('SELECT name ,code  FROM mtgSets')
fetched = cursor.fetchall()
sets_dict = dict(fetched)
sets = [x[0] for x in fetched]


### NAVBAR ###

navbar = 