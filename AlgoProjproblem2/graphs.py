import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import senti_conclusion


# plotting both graphs (word count & stop word) and (positive, negative, neutral words)
def plotGraphs(courier_company, total_words_arr, total_stop_words_arr, total_positive_words_arr,
               total_negative_words_arr, total_neutral_words_arr, positive_sentiment,
               negative_sentiment, neutral_sentiment):
    positive_sentiment = dict(sorted(positive_sentiment.items(), key=lambda x: x[1], reverse=True))
    negative_sentiment = dict(sorted(negative_sentiment.items(), key=lambda x: x[1], reverse=True))
    neutral_sentiment = dict(sorted(neutral_sentiment.items(), key=lambda x: x[1], reverse=True))

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    wordcount = go.Bar(name='Word Count', x=courier_company, y=total_words_arr)
    stopword = go.Bar(name='Stop Words', x=courier_company, y=total_stop_words_arr)
    positiveword = go.Bar(name='Positive Words', x=courier_company, y=total_positive_words_arr)
    negativeword = go.Bar(name='Negative Words', x=courier_company, y=total_negative_words_arr)
    neutralword = go.Bar(name='Neutral Words', x=courier_company, y=total_neutral_words_arr)
    positivesentiment = go.Bar(name='Positive Sentiment', x=list(positive_sentiment.keys()),
                               y=list(positive_sentiment.values()))
    negativesentiment = go.Bar(name='Negative Sentiment', x=list(positive_sentiment.keys()),
                               y=list(negative_sentiment.values()))
    neutralsentiment = go.Bar(name='Neutral Sentiment', x=list(positive_sentiment.keys()),
                              y=list(neutral_sentiment.values()))

    app.layout = html.Div(children=[
        html.Div([
            html.Div()
        ]),

        html.Div([
            html.H1(children='Word Count and Stop Word'),

            html.Div(children='''
                    Grouped Bar Chart of Word Count and Stop Word by using Dash.
                '''),

            dcc.Graph(
                id='graph1',
                figure={
                    'data': [wordcount, stopword],
                    'layout':
                        go.Layout(title='Total Word Count and Stop Word by Courier Company',
                                  barmode='group')
                })
        ]),

        html.Div([
            html.H1(children='Positive, Negative and Neutral Words Count'),

            html.Div(children='''
                       Graph of Positive, Negative and Neutral words count by using Dash.
                   '''),

            dcc.Graph(
                id='graph2',
                figure={
                    'data': [positiveword, negativeword, neutralword],
                    'layout':
                        go.Layout(
                            title='Total Positive, Negative and Neutral Words by Courier Company',
                            barmode='group')
                })
        ]),

        html.Div([
            html.H1(children='Sentiment Ranking'),

            html.Div(children='''
                          Graph of Sentiment Ranking using ratio of positive words and negative words.
                      '''),

            dcc.Graph(
                id='graph3',
                figure={
                    'data': [positivesentiment, negativesentiment, neutralsentiment],
                    'layout':
                        go.Layout(
                            title='Sentiment Ranking by Ratio',
                            barmode='group')
                })
        ]),

        html.Div([
            html.H1(children='Conclusion'),
            html.H5(children='''
                              Algorithmic conclusion regarding the sentiment of the articles.
                          '''),
            html.Div(children=[str(senti_conclusion.best_senti(positive_sentiment))])
        ])

    ])

    app.run_server(debug=True)
