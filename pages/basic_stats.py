import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from Components.rarityChecklist import rarity_checklist
from Components.colorChecklist import color_checklist

dash.register_page(
    __name__,
    path='/bstats',
    name='Basic Statistics'
)

layout = html.Div(
    children=[
        ### Set Basic Data and data types ###
        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        html.H1("No Set Selected",className='text-center', id='set_name'),
                        html.Br(),
                        html.Table([
                            html.Tr([html.Td('Set Code:'), html.Td('NSS', id='set_code')]),
                            html.Tr([html.Td('Card Count:'), html.Td('NSS', id='set_ccount')]),
                            html.Tr([html.Td('Creature Count:'), html.Td('NSS', id='creature_Count')]),
                            html.Tr([html.Td('Sorcery Count:'), html.Td('NSS', id='sorcery_count')]),
                            html.Tr([html.Td('Instant Count:'), html.Td('NSS', id='instant_count')]),
                            html.Tr([html.Td('Enchantment Count:'), html.Td('NSS', id='ench_count')]),
                            html.Tr([html.Td('Land Count:'), html.Td('NSS', id='land_count')]),
                            html.Tr([html.Td('Other Count:'), html.Td('NSS', id='other_count')]),
                        ]),
                    ]
                ,className='my-auto col-6'),
                dbc.Col(
                    children=[
                        dcc.Graph(id='types_hist')
                    ],
                    className='col-6'
                ),
                color_checklist(clid='general_color',cn='check-list text-center')
            ],
            className='p-5 d-flex justify-content-center w-100 m-0'
        ),

        ### Power vs Toughness ###
        html.H1('Power Vs Toughness',className='text-center'),
        dbc.Row(
            children=[
                
                dbc.Col(
                    children=[
                        dcc.Graph(id='power_plot'),
                        rarity_checklist('power_rarity',cn='check-list mx-auto'),
                        color_checklist('power_color',cn='check-list mx-auto'),
                    ],
                    className='col-6 text-center'
                ),
                dbc.Col(
                    children=[
                        dcc.Graph(id='toughness_plot'),
                        rarity_checklist('toughness_rarity',cn='check-list mx-auto'),
                        color_checklist('toughness_color',cn='check-list mx-auto'),
                    ],
                    className='col-6 text-center'
                ),
            ],
            className='p-5 d-flex justify-content-center w-100 m-0'
        ),

        ### Just heatmap for now ###

        dbc.Row(
            children=[
                dbc.Col(
                    children=[
                        dcc.Graph(id='heatmap_plot'),
                        rarity_checklist('heatmap_rarity',cn='check-list mx-auto'),
                        color_checklist('heatmap_color',cn='check-list mx-auto'),
                    ],
                    className='col-6 text-center'
                )
            ],
            className='p-5 d-flex justify-content-center w-100 m-0'
        ),
    ],
    className='mb-5'
)