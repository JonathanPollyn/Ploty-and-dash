import dash
import dash_core_components as dcc
import dash_html_components as html


# Creating the app object
app = dash.Dash()


app.layout = html.Div(children=[html.H1('Dash with Python'),
html.Div(children='Dash: A web Application framework for building Visualization'),

dcc.Graph(
    id='example-graph',
    figure = {
        'data': [
            {'x': [1,2,3], 'y': [4,1,2], 'type': 'bar', 'name': 'SF'},
            {'x': [1,2,3], 'y': [2,4,5], 'type': 'bar', 'name': 'Montreal'}
        ],
        'layout': {
            'title': 'Dash Data Visualization'
        }

    }
)


])

if __name__ == '__main__':
    app.run_server()
