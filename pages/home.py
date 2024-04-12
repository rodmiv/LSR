import dash
import dash_bootstrap_components as dbc
from dash import html, dcc

dash.register_page(__name__,path='/')
app = dash.get_app()

layout = html.Div(children=[
    
    ### Intro Segment
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
                        className='text-justify'),
                    ],
                className=''),
                className='h-100 text-left',
            ),
            className='p-5',
            width={'size':5}
        ),
        dbc.Col(
            html.Img(src='assets/images/cards.png', alt='cards',className='w-100')
            ,
            width={'size':5}
        ),
    ],className='bg-light p-5 d-flex justify-content-center w-100 m-0'),

    ### Basic Stats Segment
    dbc.Row(
        children=[
            dbc.Col(
                children=[
                    html.Img(alt='Basic Stats')
                ],
                class_name='',
                width={'size':5},
            ),
            dbc.Col(
                children=[
                    dbc.Card(
                        dbc.CardBody(
                            children=[
                                html.H1('Basic Stats'),
                                html.P(
                                    '''
                                        Explore sets general stats like number of cards, counts by type, etc.
                                        Additionally, explore where the sets creature stats (p/t) distribute and more. 
                                    '''
                                ),
                            ],
                        ),
                        className='h-100 text-left bg-light',
                    ),
                ],
                className='',
                width={'size':5},
            ),
        ],
        class_name='p-5 d-flex justify-content-center w-100 m-0',
    ),
    ### Color Pair Segment

    dbc.Row(
        children=[
            dbc.Col(
                children=[
                    dbc.Card(
                        dbc.CardBody(
                            children=[
                                html.H1('Color Pairs'),
                                html.P(
                                    '''
                                        Get a sense of the sets 
                                        themes and mechanics through the color pairs in the set.
                                        Look at uncommon sign posts, keyword, mechanics and some llm results run through the sets (coming later). 
                                    '''
                                ),
                            ],
                        ),
                        className='h-100 text-left',
                    ),
                ],
                className='',
                width={'size':5},
            ),
            dbc.Col(
                children=[
                    html.Img(alt='Basic Stats')
                ],
                class_name='',
                width={'size':5},
            ),
        ],
        class_name='p-5 d-flex justify-content-center w-100 m-0 bg-light',
    ),
], className='mb-5')