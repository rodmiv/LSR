import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(__name__,path='/')

layout = html.Div(children=[
    html.H1('Welcome')
])