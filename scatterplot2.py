import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
)]
layout = go.Layout(
    title = 'Random Data for Scatterplot', #Graph Title
    xaxis = dict(title = 'Random x-values'), #Labeling the x title
    yaxis = dict(title = 'Random -values'), #Labeling the y axis
    hovermode = 'closest' # handling multiple points of landing on the same vertical
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scaterplot2.html')