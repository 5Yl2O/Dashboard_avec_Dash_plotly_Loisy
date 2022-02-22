import random
from dash import Dash, html, dcc
import dash_leaflet as dl
import plotly.express as px
import pandas as pd
from dash.dependencies import Output, Input
import dash_leaflet.express as dlx

from dash_extensions.javascript import assign

#importation excel
df = pd.read_excel(r'../nitrate_jupyter.xlsx')
s = pd.DataFrame([['Source 1',4 ]], columns = ["Source","Nitrates"])
df = df.append(s, ignore_index = True)

print(df)

# sources de Loisy
Sources = [dict(name="Source 1", lat=48.864163, lon=6.109882),
          dict(name="Source 2", lat=48.86481, lon=6.108976),
          dict(name="Source 3", lat=48.86407, lon=6.107531),
          dict(name="Source 4", lat=48.863809, lon=6.107276),
          dict(name="Source 5", lat=48.863482, lon=6.106427),
          dict(name="Source 6", lat=48.865616, lon=6.107503),
          dict(name="Source 7", lat=48.865392, lon=6.111298)]
# Generate geojson with a marker for each city and name as tooltip.
geojson = dlx.dicts_to_geojson([{**c, **dict(tooltip=c['name'])} for c in Sources])
#fig = px.bar(df, x='Date', y = 'Source1')
#fig.show()
#print(df)
app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1("Analyse graphique de la teneur en Nitrate"),
        html.Div(
            dcc.Dropdown(id='source_option',options=[{'label':x,'value':x} for x in sorted(df.Source.unique())],
                 value='Source 1', #mutli=True
                         )),
            dcc.Graph(id='my-graph', figure = {}), #px.bar(df, x='Date', y ='Nitrates')


        html.Div(children='Une carte'),
            dl.Map(children=[
            dl.TileLayer(),
            dl.GeoJSON(data=geojson, #options=dict(filter=geojson_filter),
            id="geojson")
        ], style={'width': '100%', 'height': '50vh', 'margin': "auto", "display": "block"}, id="map"),
]),

        html.Div([
            html.H1("Analysepourcarte"),
            html.Div(
                dcc.Dropdown(id='date_option',options=[{'label':x,'value':x} for x in sorted(df.Date.unique())],
                 value='26-03-2015'
                 )),
                dcc.Graph(id = 'wesh', figure = {}),


                ]),
            ])

@app.callback(
     [Output(component_id='my-graph', component_property='figure'),
      Output(component_id = 'wesh', component_property = 'figure')],
    [Input(component_id='source_option', component_property='value'),
      Input(component_id='date_option', component_property='value')]
)

# @app.callback(
#     Output(component_id = 'wesh', component_property = 'figure'),
#     Input(component_id='date_option', component_property='value'),
# )

def interactive_graphing(value_source, value_date):
    print(value_source) #pour voir la source choisie dans la fenêtre
    dff = df[df.Source==value_source] #copie
    fig = px.bar(dff, x = 'Date', y = 'Nitrates')
    dfff = df[df.Date == value_date]
    figg = px.bar(dfff, x='Source', y='Nitrates')
    return fig, figg


# def graphique(value_date) :
#     dfff = df[df.Date == value_date]
#     figg = px.bar(dfff, x='Source', y='Nitrates')
#     return figg

#interactive graphing with Dash

if __name__ == '__main__':
    app.run_server(debug=True)


