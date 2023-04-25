import pandas as pd
import numpy as np


def nulitos(df):
    nul_col = df.isna().sum()
    print(nul_col[nul_col>0])


def modificar_nombre(nombre):
    if nombre.upper() in 'USA':
        return nombre
    elif 'UAE' in  nombre.upper():
        return 'UAE'
    elif nombre.endswith('?'):
        return nombre.title()[:-1]
    elif nombre is 'N/A':
        return 'N/A'
    elif '&' in nombre:
        nombre = nombre.replace('&', '/')
        return nombre
    else:
        return nombre.title()
    


def completar_valores(row):
    if pd.isnull(row['Area']):
        row['Area'] = row['Location']
    if pd.isnull(row['Area']) and pd.isnull(row['Location']):
        row['Area'] = 'unknown'
    if pd.isnull(row['Location']):
        row['Location'] = 'unknown'
    return row


dict_activ = {"Board surfing" : ".*(surf).*|.*(boogie board).*|.*(body board).*",
              "Kayaking & similar" : ".*(kayak).*|.*(canoe).*|.*(rowing).*",
              "Diving" : ".*(diving).*",
              "Paddle boarding" : ".*(paddle).*",
              "Sailing" : ".*(boat).*|.*(sail).*|.*(ship).*|.*(overboard).*",
              "Snorkeling" : ".*(snorkel).*",
              "Swimming" : ".*(bathing).*|.*(swimming).*|.*(float).*",
              "Spear-fishing" : ".*(spearfishing).*",
              "Fishing" : "[\w\s]+?(fishing).*|^(fishing).*",
              "Wading" : ".*wad.*|.*(walking).*|.*(standing).*|.*(treading).*"
}