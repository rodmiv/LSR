from dash import html
import datetime
import dash_bootstrap_components as dbc

footer = html.Div(
    children=[
        dbc.Col(children=[
            html.P(f"Rod's World {datetime.date.today().year}",
                   className='footer-text m-0' ),
            html.P('All images are property of Wizards of the Coast.',
                   className='footer-text m-0'),
            html.P('This app is powered by Scryfall',
                   className='footer-text m-0')
        ]),
        
    ],
    className='fixed-bottom text-center bg-dark p-2'
)