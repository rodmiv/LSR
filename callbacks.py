from dash import Output, Input, dcc, html
import dash_bootstrap_components as dbc
import sqlite3
import requests
import json

### Locals ###
from Components.NavBar import sets_dict
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
        code = sets_dict[selected_set]

        set_cards(code)

        return dict(hidden = None)

