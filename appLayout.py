### Imports ###
from dash import html
import dash_bootstrap_components as dbc

### Locals ###
from Components.NavBar import navbar
### Layout ###

myLayout = html.Div(
    className="document",
    children=[
        navbar,
        html.Div(
            children=[

            ],
        className="page-body"),
        
    ]
)