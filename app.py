from flask import Flask, render_template_string, render_template
import pandas as pd
from urllib.request import urlopen
import json
import plotly.express as px
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

app = Flask(__name__)

us_state_abbreviations = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}
us_state_latitudes = {
    "AL": 32.806671,
    "AK": 61.370716,
    "AZ": 33.729759,
    "AR": 34.969704,
    "CA": 36.116203,
    "CO": 39.059811,
    "CT": 41.597782,
    "DE": 39.318523,
    "FL": 27.766279,
    "GA": 33.040619,
    "HI": 21.094318,
    "ID": 44.240459,
    "IL": 40.349457,
    "IN": 39.849426,
    "IA": 42.011539,
    "KS": 38.526600,
    "KY": 37.668140,
    "LA": 31.169546,
    "ME": 44.693947,
    "MD": 39.063946,
    "MA": 42.230171,
    "MI": 43.326618,
    "MN": 45.694454,
    "MS": 32.741646,
    "MO": 38.456085,
    "MT": 46.921925,
    "NE": 41.125370,
    "NV": 38.313515,
    "NH": 43.452492,
    "NJ": 40.298904,
    "NM": 34.840515,
    "NY": 42.165726,
    "NC": 35.630066,
    "ND": 47.528912,
    "OH": 40.388783,
    "OK": 35.565342,
    "OR": 44.572021,
    "PA": 40.590752,
    "RI": 41.680893,
    "SC": 33.856892,
    "SD": 44.299782,
    "TN": 35.747845,
    "TX": 31.054487,
    "UT": 40.150032,
    "VT": 44.045876,
    "VA": 37.769337,
    "WA": 47.400902,
    "WV": 38.491226,
    "WI": 44.268543,
    "WY": 42.755966
}
us_state_longitudes = {
    "AL": -86.791130,
    "AK": -152.404419,
    "AZ": -111.431221,
    "AR": -92.373123,
    "CA": -119.681564,
    "CO": -105.311104,
    "CT": -72.755371,
    "DE": -75.507141,
    "FL": -81.686783,
    "GA": -83.643074,
    "HI": -157.498337,
    "ID": -114.478828,
    "IL": -88.986137,
    "IN": -86.258278,
    "IA": -93.210526,
    "KS": -96.726486,
    "KY": -84.670067,
    "LA": -91.867805,
    "ME": -69.381927,
    "MD": -76.802101,
    "MA": -71.530106,
    "MI": -84.536095,
    "MN": -93.900192,
    "MS": -89.678696,
    "MO": -92.288368,
    "MT": -110.454353,
    "NE": -98.268082,
    "NV": -117.055374,
    "NH": -71.563896,
    "NJ": -74.521011,
    "NM": -106.248482,
    "NY": -74.948051,
    "NC": -79.806419,
    "ND": -99.784012,
    "OH": -82.764915,
    "OK": -96.928917,
    "OR": -122.070938,
    "PA": -77.209755,
    "RI": -71.511780,
    "SC": -80.945007,
    "SD": -99.438828,
    "TN": -86.692345,
    "TX": -97.563461,
    "UT": -111.862434,
    "VT": -72.710686,
    "VA": -78.169968,
    "WA": -121.490494,
    "WV": -80.954384,
    "WI": -89.616508,
    "WY": -107.302490
}

@app.route("/")
def home():
    dft = pd.read_csv('data.txt', sep='\t', dtype={"County Code": str})
    fig = px.choropleth(dft, geojson=counties, locations='County Code', color='Heat Wave Days Based on Daily Maximum Temperature',
                            color_continuous_scale="Viridis",
                            scope="usa",
                            )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    div = fig.to_html(full_html=False)
    # return render_template_string('''
        # <html>
        # <head>
        #     <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        # </head>
        # <body>
        #     {{div_placeholder|safe}}
        # </body>
        # </html>
    # ''', div_placeholder=div)
    return render_template('page.html', divplaceholder=div)

if __name__ == "__main__":
    app.run(debug=True)