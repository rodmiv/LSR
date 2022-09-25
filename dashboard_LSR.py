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


pn.extension('tabulator', sizing_mode="stretch_width")

list_of_sets = os.listdir('C:/Users/rod_c/Documents/Python/LSR/Data') 
expansion = 'DMU'

stx_df = pd.read_json('C:/Users/rod_c/Documents/Python/Datos/' + expansion + '.json') #Se lee el archivo JSON de 
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

mtg_limited_app = Dash()

#Layout
dd_list = []
dd_list.append('all')
for i in df['rarity'].unique():
    dd_list.append(i)
    
    
rarity_checklist = dcc.Checklist(id='r_checklist',value='all',options=dd_list,
                                 labelStyle={'display': 'block'},style={"overflow":"auto"})

mtg_limited_app.layout = html.Div([
    
    html.Div(children=[html.H1('Limited Set Review')],style={'text-align': 'center'}),
    
    html.Div(children=[html.Div(children=[
            dcc.Graph(id='Power_Stats',style={'height':'40vh'}),
            dcc.Graph(id='Toughness_Stats',style={'height':'40vh'}),
            ],style={'width':'80vw','padding': 10, 'flex': 2}),
        
        html.Div(children=[
            html.H3(children='Rarity',style={}),
            rarity_checklist
            ],style={'padding': 10, 'flex': 1})
    ],style={'display': 'flex', 'flex-direction': 'row'})
    
], style={'display': 'flex', 'flex-direction': 'column'})

@mtg_limited_app.callback(
    Output(component_id='Power_Stats',component_property='figure'),
    Input(component_id='r_checklist', component_property='value')
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
    Input(component_id='r_checklist', component_property='value')
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

if __name__ == '__main__':
    mtg_limited_app.run_server(debug=False, use_reloader=False, port=8150)
