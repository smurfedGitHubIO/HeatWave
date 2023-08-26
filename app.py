from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

df = pd.read_csv('./data.txt')

app = Dash(__name__)

features = ['Heat Wave Days Based on Daily Maximum Temperature',
            'Heat Wave Days Based on Daily Maximum Heat Index',
            'Heat Wave Days Based on Net Daily Heat Stress',
            'Population']

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(features, 'Heat Wave Days Based on Daily Maximum Temperature', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    return px.choropleth(df, geojson=counties, locations='County Code', color=value,
                           color_continuous_scale="Viridis",
                           scope="usa",
#                            labels={'unemp':'unemployment rate'}
                          )

if __name__ == '__main__':
    app.run(debug=True)
