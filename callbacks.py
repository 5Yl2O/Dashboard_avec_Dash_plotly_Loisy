from dash import Input, Output
from app import app
from datetime import datetime as dt
from datetime import date, timedelta
from components.functions import df_pc
from components.functions import update_first_datatable, update_graph,df_pc,update_pie, df_ars, df_aerm
import plotly.express as px

#callback de mise à jour de la table de données à partir du sélécteur de date
@app.callback(Output('table', 'data'),
	[Input('my-date-picker-range-publishing', 'start_date'),
	 Input('my-date-picker-range-publishing', 'end_date')
     ])
def update_data_1(start_date, end_date):

	data_table = update_first_datatable(start_date, end_date,'defaut')
	return data_table

#callback de mise à jour des graphs(line et bar) à partir des cases à cocher
@app.callback(
   Output('publishing', 'figure'),
   [Input('radio-button-publishing', 'value')])
def update_publishing(value):
    start_date=(df_pc['dates'].max() - timedelta(28)).date()
    start_date= dt.strftime(start_date, '%Y-%m-%d')
    end_date=df_pc['dates'].max().date()
    end_date= dt.strftime(end_date, '%Y-%m-%d')
    if value=='all':
        start_date=df_pc['dates'].min().date()
        start_date= dt.strftime(start_date, '%Y-%m-%d')
        end_date=df_pc['dates'].max().date()
        end_date= dt.strftime(end_date, '%Y-%m-%d')
        fig=update_graph(start_date, end_date,'trafic')
        return fig
    elif value=='trois_mois':
        end_date_obj= dt.strptime(end_date, '%Y-%m-%d')
        start_date=end_date_obj.date()-timedelta(92)
        start_date=start_date.strftime("%Y-%m-%d")
        fig = update_graph(start_date, end_date,'trafic')
        return fig
    elif value=='six_mois':
        end_date_obj= dt.strptime(end_date, '%Y-%m-%d')
        start_date=end_date_obj.date()-timedelta(186)
        start_date=start_date.strftime("%Y-%m-%d")
        fig = update_graph(start_date, end_date,'trafic')
        return fig
    elif value=='un_an':
        end_date_obj= dt.strptime(end_date, '%Y-%m-%d')
        start_date=end_date_obj.date()-timedelta(365)
        start_date=start_date.strftime("%Y-%m-%d")
        fig = update_graph(start_date, end_date,'trafic')
        return fig
    else:
	    fig = update_graph(start_date, end_date,'trafic')
	    return fig



# callback de mise à jour du graph circulaire à partir des cases à cocher
@app.callback(
   Output('pieGraph', 'figure'),
   [Input('radio-button-publishing', 'value')])

def update_publishing(value):
    start_date=(df_pc['dates'].max() - timedelta(28)).date()
    start_date= dt.strftime(start_date, '%Y-%m-%d')
    end_date=df_pc['dates'].max().date()
    end_date= dt.strftime(end_date, '%Y-%m-%d')
    if value=='all':
        start_date=df_pc['dates'].min().date()
        start_date= dt.strftime(start_date, '%Y-%m-%d')
        end_date=df_pc['dates'].max().date()
        end_date= dt.strftime(end_date, '%Y-%m-%d')
        fig=update_pie(start_date, end_date,'trafic')
        return fig
    elif value=='trois_mois':
        end_date_obj= dt.strptime(end_date, '%Y-%m-%d')
        start_date=end_date_obj.date()-timedelta(92)
        start_date=start_date.strftime("%Y-%m-%d")
        fig = update_pie(start_date, end_date,'trafic')
        return fig
    elif value=='six_mois':
        end_date_obj= dt.strptime(end_date, '%Y-%m-%d')
        start_date=end_date_obj.date()-timedelta(186)
        start_date=start_date.strftime("%Y-%m-%d")
        fig = update_pie(start_date, end_date,'trafic')
        return fig
    elif value=='un_an':
        end_date_obj= dt.strptime(end_date, '%Y-%m-%d')
        start_date=end_date_obj.date()-timedelta(365)
        start_date=start_date.strftime("%Y-%m-%d")
        fig = update_pie(start_date, end_date,'trafic')
        return fig

    else:
	    fig = update_pie(start_date, end_date,'trafic')
	    return fig

# Connection du graph Plotly avec les composants Dash (dcc)
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_conc', component_property='figure')],
    [Input(component_id='select_param', component_property='value')]
)
def update_graph_qual(option_slctd):

    container = "Le code du paramètre selectionné est: {}".format(option_slctd)

    dff = df_ars.copy()
    dff = dff[dff["code_parametre"] == option_slctd]


    # Plotly Express
    #Création du graph

    fig_eau = px.line(dff,
                      x='date_prelevement',
                      y='resultat_numerique',
                      color='nom_uge',
                      markers=True
                      )

    return container, fig_eau
