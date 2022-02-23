import dash
import dash_bootstrap_components as dbc
from dash import html

LOGO = "https://loisy54.fr/wp-content/uploads/2020/11/Blason_Loisy_54.svg"

navbar = dbc.Navbar(
    dbc.Container(
    [
        html.A(
            # Alignement vertical de l'image et de l'acceuil
            dbc.Row(
                [   #logo
                    dbc.Col(html.Img(src=LOGO, height="40px")),
                    #Navlink Acceuil
                    dbc.Col(dbc.NavLink("Acceuil", href="/acceuil")),
                    #Navlink dashbord
                    dbc.Col(dbc.NavLink("OLD_Dashbsoard_Exemple", href="/dashboard")),
                    #Navlink Qualité Sanitaire
                    dbc.Col(dbc.NavLink("Qualité Sources", href="/springs_quality")),
                    #Navlink Qualité Sanitaire
                    dbc.Col(dbc.NavLink("Localisation Sources", href="/spring_localisation")),
                ],
                align="center",
                #className="g-0",

            ),
        ),

        dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
    ],
    fluid=True
    )
    #color="dark",
    #dark=True,
)
