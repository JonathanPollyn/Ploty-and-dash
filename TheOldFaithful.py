#Importing required libraries
from turtle import title
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go


#Initiate the dash object
app = dash.Dash()

# Importing the data into a dataFrame
oldfaithful_df = pd.read_csv('C:/JonathanWorks/Plotly Data/OldFaithful.csv')
#print(oldfaithful_df)

# Creating the dash layout
app.layout = html.Div([
    dcc.Graph(
        id='the_old_faithful',
    figure = {
        'data':[
            go.Scatter(
                x = oldfaithful_df['X'],
                y = oldfaithful_df['Y'],
                mode = 'markers'
)
        ],
        'layout': go.Layout(
            title='The old Faithful Eruption intervals v Duration',
            xaxis= {'title': 'Duration of the eruption'},
            yaxis = {'title': 'Interval to the next eruption'},
            hovermode='closest'
        )
    }

    )
    

])






#Adding the server
if __name__ == '__main__':
    app.run_server()