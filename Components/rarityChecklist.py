from dash import dcc
import dash_bootstrap_components as dbc

def rarity_checklist(clid,cn):
    return dbc.Card(
        dcc.Checklist(
            ['Common','Uncommon','Rare','Mythic'],
            id=f'{clid}',
            inline=True,
            inputStyle={"margin-right": "5px","margin-left": "10px"},
            
        ),
        className=cn
    )

    