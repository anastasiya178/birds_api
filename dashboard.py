import plotly.express as px
from dash import Dash, dcc, html

from transformations.transformations import species_count, county_top_5
from transformations.group_by_month import obs_reported_by_month


app = Dash(__name__)

# top 3 observation dates
fig = px.bar(obs_reported_by_month, x='Month', y='Count', color_discrete_sequence=['#b05815'])
fig.update_layout(width=700, height=500, bargap=0.05)

fig2 = px.bar(species_count, x='sciName', y='Count', color_discrete_sequence=['#0a4a2a'])
fig2.update_layout(width=700, height=500, bargap=0.05)

fig3 = px.bar(county_top_5, x='County', y='Count', color_discrete_sequence=['#472d04'])
fig2.update_layout(width=700, height=500, bargap=0.05)

app.layout = html.Div(children=[
    # All elements from the top of the page
    html.Div(
        children=[
            html.Div(
                children=[
                    html.Span(children="🦤", className="header-emoji"),
                    html.H1(
                        children='Birds Observation in Pennsylvania',
                        className="header-title",
                    ),
                    html.Span(
                        children=(
                            "Analyze the observation of birds in 2025 in Pennsylvania"
                        ),
                        className="header-description",
                    ),
                ],
                className="header"
            ),
            html.Div([
                html.Span(
                    children="Observations reported by month",
                    className="graph_name"
        ),
                dcc.Graph(
                    id='graph1',
                    figure=fig
                ),
            ],
            className="div_graph"
            ),

            html.Div([
                html.Span(
                    children="Top species observed",
                    className="graph_name"
                ),
                dcc.Graph(
                    id='graph2',
                    figure=fig2
                ),
            ],
            className="div_graph"
            ),
            html.Div([
                html.Span(
                    children="Top countries observed",
                    className="graph_name"
                ),
                dcc.Graph(
                    id='graph3',
                    figure=fig3
                ),
            ],
            className="div_graph"
            ),
        ],
    )
]
)

if __name__ == '__main__':
    app.run(debug=True)

    # run and open http://127.0.0.1:57540/

# for reference
# columns = ['speciesCode', 'comName', 'sciName', 'locId', 'locName', 'obsDt',
#        'howMany', 'lat', 'lng', 'obsValid', 'obsReviewed', 'locationPrivate',
#        'subId', 'exoticCategory']
