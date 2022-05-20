import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd

df = pd.read_csv('C:/Jonathan Works/Plotly_and_Dash/TestData.csv')
print(df.head())


#Creating Traces
traces = [go.Scatter(
    x = df.columns,
    y = df.loc[name],
    mode = 'markers',
    name = name
) for name in df.index]

layout = go.Layout(
    title = 'Milestone to product'
)

fig = go.Figure(data=traces, layout=layout)
pyo.plot(fig, filename='line2.html')