# Import the required packages
from turtle import width
import dash
import dash_html_components as html


# Initiating the dash app
app = dash.Dash()


# Creating the app layout
app.layout = html.Div([
    'This information will be the outermost DIV',
    html.Div(
        'This will be the inner most DIV',
        style={
            'color': 'blue',
            'border': '2px blue solid',
            'borderRadius': 5,
            'padding': 10,
            'width': 220
        }
    ),
    html.Div(
        'This is another inner Div',
        style={
            'color': 'greem',
            'border': '2px green solid',
            'borderRadius': 5,
            'padding': 10,
            'width': 220
        }
    ),

],
        style={
            'color': 'red',
            'border': '2px red dotted',
            'margin': 10,
            'width': 500,
            'height': 200
        }
)

if __name__ == '__main__':
    app.run_server()
