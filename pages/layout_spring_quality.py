from dash import Dash, html, dcc, Input, Output
#import dash_bootstrap_components as dbc
import dash_leaflet as dl
#import plotly.express as px
#import pandas as pd
#import requests

layout_spring_quality = html.Div([

    html.H1("Qualité sanitaire de l'eau des sources de Loisy", style={'text-align': 'center'}),

# la liste des codes param est extraite du df_eau => df[['code_parametre','libelle_parametre']]




    dcc.Dropdown(id="select_param",
                 options=[
                     {"label": "Nitrates (en NO3)", "value": '1340'},
                     {"label": "Conductivité à 25°C", "value": '1303'},
                     {"label": "Chlore combiné", "value": '1755'},
                     {"label": "Chlore total", "value": '1399'}
                 ],
                 value='1399',
                 ),


    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_conc', figure={})

])
