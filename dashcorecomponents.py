# Import the required packages
from cProfile import label
import dash
import dash_core_components as dcc
import dash_html_components as html


# Initiating the dash app
app = dash.Dash()
app.layout = html.Div([
    # Dropdown
html.Label('Dash Dropdown'),
dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
),
html.Label('Multi-Select Droopdown'),
dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'lable': 'Montreal', 'value': 'MTL'},
        {'lable': 'San Francisco', 'value': 'SF'}
    ],
    value=['MTL','SF'],
    multi=True
),
# Slider
html.Label('Slider'),
html.P(
    dcc.Slider(
        min=-5,
        max=10,
        step=0.5,
        marks={i: i for i in range(-5,11)},
        value=-3
    )
),
# Radio item
html.Label('Radio Item'),
dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'lable': 'Montreal', 'value': 'MTL'},
        {'lable': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
)


], style={'width': '50%'}
)






if __name__ == '__main__':
    app.run_server()