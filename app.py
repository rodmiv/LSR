import pandas as  pd
import json
import numpy as np
import plotly.express  as px
import os
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from pathlib import Path
from utils.utilities import next_free_port
from utils.sets import set_cards

### Locals ###
from appLayout import myLayout

### Initialize the APP ###
app = Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE])

### Layout ###
app.layout = myLayout

### Callbacks ###

### Options ###

### Run APP ###
user_port = next_free_port()
app.run(debug=True, port=user_port)