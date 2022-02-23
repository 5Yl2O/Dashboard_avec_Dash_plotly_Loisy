import dash
import dash_bootstrap_components as dbc
from dash import html

LOGO = "https://loisy54.fr/wp-content/uploads/2020/11/Blason_Loisy_54.svg"

navbar = dbc.Navbar(
    [
        html.A(
            # Alignement vertical de l'image et de l'acceuil
            dbc.Row(
                [   #logo
                    dbc.Col(html.Img(src=LOGO, height="40px")),
                    #Navlink Acceuil
                    dbc.NavLink("Acceuil", href="/acceuil"),
                    #Navlink dashbord
                    dbc.NavLink("Dashbsoard", href="/dashboard"),
                    #Navlink Qualité Sanitaire
                    dbc.NavLink("Qualité Sources", href="/springs_quality")
                ],
                align="center",
                #no_gutters=True,
            ),
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
    ],
    #color="dark",
    #dark=True,
)
