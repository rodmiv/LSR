# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as  pd
import json
import numpy as np
import seaborn as sns
import statistics
import panel as pn
import matplotlib.pyplot as plt
import plotly.express  as px
import os
from dash import Dash, html, dcc, Input, Output
from pathlib import Path
from utils.utilities import next_free_port

parent_path =str(Path(__file__).parent.absolute())

# list_of_sets = []
list_of_sets = os.listdir(parent_path + '/Data') 

expansion = 'BRO'

stx_df = pd.read_json(parent_path + '/Data/' + expansion + '.json') #Se lee el archivo JSON de 
a_jason=json.dumps(stx_df['data']['cards'])
a_jason2=json.loads(a_jason)
df=pd.DataFrame.from_dict(a_jason2, orient="columns")
df = df[(df['isPromo'].isna())&(df['promoTypes'].isna())&(~df['boosterTypes'].isna())]

df['power'].replace(to_replace='*',value='1',inplace = True)
df['power'].replace(to_replace='*+1',value='1',inplace = True)
df['power'].replace(to_replace='1+*',value='1',inplace = True)
df['toughness'].replace(to_replace='*',value='1',inplace = True)
df['toughness'].replace(to_replace='*+1',value='1',inplace = True)
df['toughness'].replace(to_replace='1+*',value='1',inplace = True)
df['power']=df['power'].astype(float)
df['toughness']=df['toughness'].astype(float)

mtg_limited_app = Dash(__name__)

#Layout
dd_list = []
dd_list.append('all')
for i in df['rarity'].unique():
    dd_list.append(i)
    
print(dd_list)
rarity_checklist = dcc.Checklist(id='r_checklist',options=dd_list,
                                 labelStyle={'display': 'block'},style={"overflow":"auto"})

mtg_limited_app.layout = html.Div(children=[
    
    html.Div(children=[
        html.H1('Limited Set Review'),
        html.Div(children=[
            html.H3('Select Expansion', style={'height':'1vh','margin':'5px'}),
            dcc.Dropdown(id='sets_dd', options=list_of_sets, style={'display':'inline-block', 'height':'5vh',
                                                                'margin-top':'1vh', 'width':'27vw', 'text-align':'center'})
        ],style={'position':'absolute','top':'0','left':'0', 'width':'27vw', 'margin':'0', 'padding-left':'10px'})
        
    ],style={'text-align': 'center'}),
    
    html.Div(children=[html.Div(children=[
            dcc.Graph(id='Power_Stats',style={'height':'40vh'}),
            dcc.Graph(id='Toughness_Stats',style={'height':'40vh'}),
            ],style={'width':'80vw','padding': 10, 'flex': 2}),
        
        html.Div(children=[
            html.H3(children='Rarity',style={}),
            rarity_checklist
            ],style={'padding': 10, 'flex': 1})
    ],style={'display': 'flex', 'flex-direction': 'row'}),
    dcc.Store(id='json_storage')
    
], style={'display': 'flex', 'flex-direction': 'column'})

@mtg_limited_app.callback(
    outputs=dict(d=Output('json_storage','data')),
    inputs=dict(sel=Input('sets_dd','value')),
    prevent_initial_call=True
)

def data_load(sel):
    
    return

@mtg_limited_app.callback(
    Output(component_id='Power_Stats',component_property='figure'),
    Input(component_id='r_checklist', component_property='value'),
    prevent_initial_call=True
)

def update_graph(selected_rarity):
    if 'all' in selected_rarity:
        filtered_df = df.copy()
    else:
        filtered_df = df[df['rarity'].isin(selected_rarity)] 
        
    grouped = filtered_df[['power','rarity']].groupby(by=['power'],dropna=True,as_index=False).count()
    grouped.rename(columns={'rarity':'frequencia'},inplace=True)
    
    line_fig = px.bar(grouped,x='power',y='frequencia',title='Cumulative Power Frequency')
    
    return line_fig

@mtg_limited_app.callback(
    Output(component_id='Toughness_Stats',component_property='figure'),
    Input(component_id='r_checklist', component_property='value'),
    prevent_initial_call=True
)

def update_graph2(selected_rarity):
    if 'all' in selected_rarity:
        filtered_df = df.copy()
    else:
        filtered_df = df[df['rarity'].isin(selected_rarity)] 
        
    grouped = filtered_df[['toughness','rarity']].groupby(by=['toughness'],dropna=True,as_index=False).count()
    grouped.rename(columns={'rarity':'frequencia'},inplace=True)
    
    line_fig = px.bar(grouped,x='toughness',y='frequencia',title='Cumulative toughness Frequency')
    
    return line_fig


mtg_limited_app.scripts.config.serve_locally = True
mtg_limited_app.css.config.serve_locally = True

user_port = next_free_port()
mtg_limited_app.run(debug=True, port= user_port)
