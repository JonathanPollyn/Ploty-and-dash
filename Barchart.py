import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('C:/Jonathan Works/Plotly Data/2018WinterOlympics.csv')
print(df.head())

data = [go.Bar(
    x = df['NOC'],
    y = df['Total']
)]

layout = go.Layout(
    title = '2018 Winter Olympic medals by Country'
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barhchart.html')
