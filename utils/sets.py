import requests
import json
import sqlite3
import numpy as np
import os
from parse import parse

def replace_and_eval_asterix(string):
    return eval(parse(text=string.replace('*','0')))

def sets_list():

    print('Running Initial set retrieve')
    #Create a request to Scryfall-API for sets data 
    res  = requests.get('https://api.scryfall.com/sets')
    response = json.loads(res.text)

    #Connect to Database and insert any set not in the mtgSets table
    connection = sqlite3.connect('./Data/LSRDB.db')
    cursor = connection.cursor()

    #check if doesnt mtgsets exists and creates it
    cursor.execute("CREATE TABLE IF NOT EXISTS mtgSets (scryfall_id TEXT, code TEXT, name TEXT, released_at DATE, set_type TEXT, card_count INTEGER, UNIQUE(scryfall_id))")
    
    # cursor.execute('SELECT scryfall_id FROM mtgSets')
    # fetched = cursor.fetchall()
    # ids = [x[0] for x in fetched]

    for set in response['data']:
        if set['set_type'] in ['expansion', 'draft_innovation', 'core']:
            cursor.execute(f'''
                                INSERT OR IGNORE INTO mtgSets VALUES (
                                    "{str(set["id"])}",
                                    "{set["code"]}",
                                    "{set["name"]}",
                                    "{set["released_at"]}",
                                    "{set["set_type"]}",
                                    {set["card_count"]}
                                    )
                            ''')
            
            ### Save Set Icon ###
            icon_path = f'./assets/images/sets_icons/{set["code"]}.svg'

            if os.path.exists(icon_path):
                continue
            else:
                icon_res = requests.get(set['icon_svg_uri'])
                with open(f'./assets/images/sets_icons/{set["code"]}.svg', 'w') as file:
                    file.write(icon_res.text)
    
    connection.commit()
    connection.close()

def set_cards(set_code):
    more_pages = False
    connection = sqlite3.connect('./Data/LSRDB.db')
    cursor = connection.cursor()

    res = requests.get(f'https://api.scryfall.com/cards/search?q=set%3D{set_code}')
    response = json.loads(res.text)
    data = response['data']

    if 'next_page' in list(response.keys()):
        more_pages = True
        next_page_uri = response['next_page']

    while more_pages:
        res_=requests.get(next_page_uri)
        response_ = json.loads(res_.text)
        data.extend(response_['data'])

        if 'next_page' in list(response_.keys()):
            more_pages = True
            next_page_uri = response_['next_page']
        else:
            more_pages = False
    
    cursor.execute(f'''
               CREATE TABLE IF NOT EXISTS {set_code} (
                    scryfall_id TEXT,
                    oracle_id TEXT,
                    name TEXT,
                    layout TEXT, 
                    image_uri_1 TEXT, 
                    image_uri_2 TEXT, 
                    mana_cost_1 TEXT, 
                    mana_cost_2 TEXT, 
                    cmc INTEGER,
                    type_line_1 TEXT,
                    type_line_2 TEXT,
                    oracle_text_1 TEXT,
                    oracle_text_2 TEXT,
                    power_1 INTEGER,
                    power_2 INTEGER,
                    toughness_1 INTEGER,
                    toughness_2 INTEGER,
                    colors_1 TEXT,
                    colors_2 TEXT,
                    color_identity TEXT,
                    keywords TEXT,
                    set_id TEXT,
                    set_name TEXT,
                    collector_number,
                    rarity TEXT,
                    booster BOOLEAN,
                    UNIQUE(scryfall_id,oracle_id)
               )
               ''')
    
    for card in data:
        if card['booster'] == True:

            # print(json.dumps(card, sort_keys=True, indent=4))
            # print("#"*100)

            pows = {}
            tous = {}

            if 'power' in list(card.keys()):
                pows['pow_1'] = eval(card['power'].replace('*','0'))
                pows['pow_2']  = 999
            elif 'card_faces' in list(card.keys()):        
                count = 1
                for face in card['card_faces']:
                    if 'power' in list(face.keys()):
                        pows[f'pow_{count}'] = eval(face['power'].replace('*','0'))
                    else:
                        pows[f'pow_{count}'] = 999
                    count+=1
            else:
                pows['pow_1'] = 999
                pows['pow_2'] = 999
            
            if 'toughness' in list(card.keys()):
                tous['tou_1'] = eval(card['toughness'].replace('*','0'))
                tous['tou_2']  = 999
            elif 'card_faces' in list(card.keys()):        
                count = 1
                for face in card['card_faces']:
                    if 'toughness' in list(face.keys()):
                        tous[f'tou_{count}'] = eval(face['toughness'].replace('*','0'))
                    else:
                        tous[f'tou_{count}'] = 999
                    count+=1
            else:
                tous['tou_1']  = 999
                tous['tou_2']  = 999

            try:
                card_text_1 = card['oracle_text'].replace('"','').replace("'",'')
                card_text_2 = "NA"
            except:
                card_text = [face['oracle_text'] for face in card['card_faces']]

                card_text_1 = card_text[0].replace('"','').replace("'",'')
                card_text_2 = card_text[1].replace('"','').replace("'",'')

            try:
                image_uri_1 = card['image_uris']['normal']
                image_uri_2 = "NA"
            except:
                image_uris = [face['image_uris']['normal'] for face in card['card_faces']]

                image_uri_1 = image_uris[0]
                image_uri_2 = image_uris[1]

            try:
                mana_cost_1 = card['mana_cost']
                mana_cost_2 = "NA"
            except:
                mana_costs = [face['mana_cost'] for face in card['card_faces']]

                mana_cost_1 = mana_costs[0]
                mana_cost_2 = mana_costs[1]

            try:        
                type_1 = card['type_line'].replace("'","")
                type_2 = "NA"
            except:
                types = [face['type_line'] for face in card['card_faces']]

                type_1 = types[0].replace("'","")
                type_2 = types[1].replace("'","")

            try:        
                colors_1 = card['colors']
                colors_2 = "NA"
            except:
                colorss = [face['colors'] for face in card['card_faces']]

                colors_1 = colorss[0]
                colors_2 = colorss[1]
                
            query = f'''
                                INSERT OR IGNORE INTO {set_code} VALUES (
                                    '{card['id']}',
                                    '{card['oracle_id']}',
                                    "{card['name'].replace('"','').replace("'",'')}",
                                    '{card['layout']}',
                                    '{image_uri_1}',
                                    '{image_uri_2}',
                                    '{mana_cost_1}',
                                    '{mana_cost_2}',
                                    {card['cmc']},
                                    '{type_1}',
                                    '{type_2}',
                                    '{card_text_1}',
                                    '{card_text_2}',
                                    {pows['pow_1']},
                                    {pows['pow_2']},
                                    {tous['tou_1']},
                                    {tous['tou_2']},
                                    "{colors_1}",
                                    "{colors_2}",
                                    "{card['color_identity']}",
                                    "{card['keywords']}",
                                    '{card['set_id']}',
                                    '{card['set_name']}',
                                    '{card['collector_number']}',
                                    '{card['rarity']}',
                                    '{card['booster']}'
                                    )
                            '''
            #print(query)
            cursor.execute(query)
    
    connection.commit()
    connection.close()