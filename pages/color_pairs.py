import dash
import dash_bootstrap_components as dbc
from dash import html

dash.register_page(
    __name__,
    path='/colorpairs',
    name='Color Pairs'
)

layout = html.Div(children=[
    html.H1('Color Pairs',className='text-center'),
    
])