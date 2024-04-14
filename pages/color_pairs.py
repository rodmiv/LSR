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
    dbc.Row(
        children=[
            dbc.Col(className='col-4'),
            dbc.Col(
                children=[
                    html.Img(src='./assets/images/unh-44-richard-garfield-ph-d.png', className='w-75 ')
                ]
                ,className='col-4'
            ),
            dbc.Col(
                children=[
                    html.Img(src='./assets/images/unh-134-city-of-ass.png', className='w-75 ')
                ]
                ,className='col-4'
            ),
        ],
        className='p-5 d-flex justify-content-center w-100 m-0'
    ),

],
    className='mb-5')