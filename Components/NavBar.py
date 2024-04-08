import dash_bootstrap_components as dbc
from dash import html

### NAVBAR ###
navbar = dbc.Navbar(
    html.Div(
        dbc.NavbarBrand("Limited Set Review V0.1", className="ms-0 brand")
    ),
    color='primary',
    dark=True
)