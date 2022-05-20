from turtle import color
from matplotlib.pyplot import title
import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('C:/Jonathan Works/Plotly Data/2018WinterOlympics.csv')
print(df.head())

trace1 = go.Bar(
    x = df['NOC'],
    y = df['Gold'],
    name = 'Gold',
    marker=dict(color='#FFD700')
)

trace2 = go.Bar(
    x = df['NOC'],
    y = df['Silver'],
    name = 'Silver',
    marker=dict(color='#9EA0A1')
)

trace3 = go.Bar(
    x = df['NOC'],
    y = df['Bronze'],
    name = 'Bronze',
    marker=dict(color='#CD7F32')
)

data = [trace1, trace2, trace3]

layout = go.Layout(
    title = '2018 Winter Olympics and Mendals',
    barmode = 'stack'
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barhchart2.html')
