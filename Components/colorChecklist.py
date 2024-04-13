from dash import dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

def color_checklist(clid, cn):
    return dbc.Card(
        dmc.CheckboxGroup(
            orientation='horizontal',
            id=clid,
            children=[
                dmc.Checkbox(label='U',value='u',color='blue'),
                dmc.Checkbox(label='R',value='r',color='red'),
                dmc.Checkbox(label='W',value='w',color='yellow',),
                dmc.Checkbox(label='B',value='b',color="gray"),
                dmc.Checkbox(label='G',value='g',color='green'),
            ]
        ),className=cn)