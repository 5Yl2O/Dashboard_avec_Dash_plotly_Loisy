from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_leaflet as dl
import geopandas as gpd



Sources = [dict(name="Source 1", lat=48.864163, lon=6.109882),
          dict(name="Source 2", lat=48.86481, lon=6.108976),
          dict(name="Source 3", lat=48.86407, lon=6.107531),
          dict(name="Source 4", lat=48.863809, lon=6.107276),
          dict(name="Source 5", lat=48.863482, lon=6.106427),
          dict(name="Source 6", lat=48.865616, lon=6.107503),
          dict(name="Source 7", lat=48.865392, lon=6.111298)]
# Generate geojson with a marker for each city and name as tooltip.
gpd_sources = gpd.fr.dicts_to_geojson([{**c, **dict(tooltip=c['name'])} for c in Sources])


# ------------------------------------------------------------------------------
page_title=html.Div(html.H1("Localisation des sources de Loisy",style={'text-align': 'center'}))


# App layout
layout_spring_localisation = html.Div(
    dbc.Container([
        dbc.Row(
            dbc.Col(
                page_title,
                md=11,
            ),

        ),


        dbc.Row(
            dbc.Col(
                dl.Map(
                    dl.TileLayer(), style={'height': '50vh'}
                ),
                md=11,
            ),
        justify="center",
        ),
        dbc.Row(
            [
                html.Br(),
                html.Div('Réalisé par XX Votre nom ici !! XX'),
                html.Br(),
            ],
            justify='center'
        ),

    ],
    className="pad-row"
    )
)
