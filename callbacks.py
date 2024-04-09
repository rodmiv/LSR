from dash import Output, Input, dcc, html
import dash_bootstrap_components as dbc
import sqlite3
from dash.exceptions import PreventUpdate
import json

### Set Options ###
connection = sqlite3.connect('./Data/LSRDB.db')
cursor = connection.cursor()
cursor.execute('SELECT name ,code  FROM mtgSets')
fetched = cursor.fetchall()
sets_dict = dict(fetched)
sets = [x[0] for x in fetched]

### Locals ###
from utils.sets import set_cards

def get_callbacks(app):

    @app.callback(
        output = dict(
            hidden = Output('hidden-div','children')
        ),
        inputs = dict(
            selected_set = Input('set_selection','value')
        ),
        prevent_initial_call = True
    )

    def selected_set_process(selected_set):

        if selected_set==None:
            raise PreventUpdate
        else:
            code = sets_dict[selected_set]

            set_cards(code)

            return dict(hidden = None)

