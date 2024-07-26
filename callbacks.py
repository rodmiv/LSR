from dash import Output, Input, dcc, html
import dash_bootstrap_components as dbc
import sqlite3
from dash.exceptions import PreventUpdate
import json
import pandas as pd

### Locals ###
from utils.sets import set_cards, sets_list
from utils.utilities import type_selection

## Needed Before Callbacks ###
sets_list()

### Set Options ###
connection = sqlite3.connect('./Data/LSRDB.db')
cursor = connection.cursor()
cursor.execute('SELECT name ,code  FROM mtgSets')
fetched = cursor.fetchall()
sets_dict = dict(fetched)
sets = [
    {
        'label': html.Span(
            children=[
                html.Img(src=f'./assets/images/sets_icons/{sets_dict[x[0]]}.svg', height=20,width=20),
                html.Span(f'{x[0]}', style={'font-size': 15, 'padding-left': 10})
            ], style={'align-items': 'center', 'justify-content': 'center'}
        ),
        "value": x[0],
    }
    for x in fetched
]



def get_callbacks(app):

    @app.callback(
        output = dict(
            hidden = Output('hidden-div','children'),
            set_code = Output('set_code','children'),
            set_count = Output('set_count','children'),
            crea_count = Output('creature_count','children'),
            sorcery_count = Output('sorcery_count','children'),
            instant_count = Output('instant_count','children'),
            ench_count = Output('ench_count','children'),
            art_count = Output('artifacts_count','children'),
            land_count = Output('land_count','children'),
            pw_count = Output('planesw','children'),
            other_count = Output('other_count','children'),
        ),
        inputs = dict(
            selected_set = Input('set_selection','value')
        ),
        prevent_initial_call = True
    )

    def selected_set_process(selected_set):

        print(f"Processing {selected_set}")

        if selected_set==None:
            raise PreventUpdate
        else:
            code = sets_dict[selected_set]

            set_cards(code)

            cx = sqlite3.connect('./Data/LSRDB.db')
            set_df = pd.read_sql_query(f"SELECT * FROM {code}",cx)
            set_df['basic_type'] = set_df['type_line_1'].apply(type_selection)
            creatures_df = set_df[set_df['basic_type']=='creature']
            sorcery_df = set_df[set_df['basic_type']=='sorcery']
            instant_df = set_df[set_df['basic_type']=='instant']
            ench_df = set_df[set_df['basic_type']=='enchantment']
            art_df = set_df[set_df['basic_type']=='artifact']
            land_df = set_df[set_df['basic_type']=='land']
            pw_df = set_df[set_df['basic_type']=='planeswalker']
            other_df = set_df[set_df['basic_type']=='other']
            return dict(
                hidden = None,
                set_code = code.upper(),
                set_count = set_df.shape[0],
                crea_count = creatures_df.shape[0],
                sorcery_count = sorcery_df.shape[0],
                instant_count = instant_df.shape[0],
                ench_count = ench_df.shape[0],
                art_count = art_df.shape[0],
                land_count = land_df.shape[0],
                pw_count = pw_df.shape[0],
                other_count = other_df.shape[0],
                )

