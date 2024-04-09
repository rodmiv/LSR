import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from pathlib import Path
from utils.utilities import next_free_port
from utils.sets import set_cards

### Locals ###
# from callbacks import get_callbacks

### Initialize the APP ###
app = Dash(__name__, external_stylesheets=[dbc.themes.SANDSTONE], use_pages=True)

### Layout ###
app.layout = html.Div(
                className="document",
                children=[
                    dbc.Navbar(
                        children=[
                            dbc.Row(children=[
                                dbc.Col(children=[
                                    html.Div(
                                        dbc.NavbarBrand("Limited Set Review V0.1", className="brand")
                                    ),
                                ],class_name='col-4', width={'offset': 2}),
                                dbc.Col(children=[
                                    #  dcc.Dropdown(options=sets,placeholder='Select a Set',className='set-selector',id='set_selection')
                                    dbc.DropdownMenu(
                                        label='Menu',
                                        children=[
                                            dbc.DropdownMenuItem(f'{page['name']}',href=page['relative_path'])
                                            for page in dash.page_registry.values()
                                        ]
                                    , size='lg')
                                ],class_name='col-4'),
                            ],class_name='w-100 mx-auto gx-5 text-center'),        
                        ],    
                        color='primary',
                        dark=True
                    ),
                    
                    html.Div(
                        dash.page_container,
                        className='m-5'
                    ),
                ]
            )

### Callbacks ###

# get_callbacks(app)

### Options ###

### Run APP ###
user_port = next_free_port()
app.run(debug=True, port=user_port)