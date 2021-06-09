import dash
import dash_core_components as dcc
import dash_html_components as html
from Problem2 import prob2
from Problem3 import prob3

print(dcc.__version__) # 0.6.0 or above is required

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),

    dcc.Link('Navigate to Problem 2', href='/dash/problem2'),
    html.Br(),
    dcc.Link('Navigate to Problem 3', href='/dash/problem3'),

    # content will be rendered in this element
    html.Div(id='page-content')
])

@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    pathname = pathname.split('/')
    if pathname[2] == "problem2":
        return prob2()
    elif pathname[2] == "problem3":
        return prob3()
    return html.Div([
        html.H3("Don't have this dash leh")
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
