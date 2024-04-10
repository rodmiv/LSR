import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

dash.register_page(__name__,path='/')

layout = html.Div(children=[
    
    dbc.Row(children=[
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H1('Welcome!'),
                        html.P(
                            '''
                                Welcome to the limited set reviewer tool. The following is my attempt at creating an automation of some basic analytics and statistics of MTG sets for limited play purposes.
                            ''',
                        ),
                    ]
                ),
                className='w-75 m-auto',
            ),
            class_name='col-6'
        ),
        dbc.Col(
            html.Img(src='./images/card.png', alt='cards')
            ,class_name='col-6'
        ),
    ],className='w-100 p-5')
],className='text-center')