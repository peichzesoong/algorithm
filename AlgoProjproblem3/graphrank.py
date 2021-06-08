import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import mcdm


# # plot graph for most to least recommended ranking based on distance and sentiment
def plot_graph_rank(mcdm_dict):
    mcdm_sort = dict(sorted(mcdm_dict.items(), key=lambda x: x[1], reverse=True))

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    mcdm_graph = go.Bar(name='Most Recommended to the Least Recommended Courier Company', x=list(mcdm_sort.keys()),
                        y=list(mcdm_sort.values()))

    app.layout = html.Div(children=[
        html.Div([
            html.Div()
        ]),

        html.Div([
            html.H1(children='Most Recommended Courier Company'),

            html.Div(children='''
                   Bar chart of most recommended courier company based on multi criteria decision making with distance and ranking by using Dash.
                '''),

            dcc.Graph(
                id='graph1',
                figure={
                    'data': [mcdm_graph],
                    'layout':
                        go.Layout(title='Most Recommended to the Least Recommended Courier Company',
                                  barmode='group')
                })
        ]),

        html.Div([
            html.H1(children='Conclusion'),
            html.H5(children='''
                              Algorithmic conclusion for best courier company.
                          '''),
            html.Div(children=[str(mcdm.best_courier(mcdm_dict))])
        ])

    ])

    app.run_server(debug=True)
