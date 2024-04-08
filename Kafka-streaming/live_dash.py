from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


df = pd.read_csv("sentiment_scores.txt", names=["score"])

fig = px.line(df["score"][-50:])

app.layout = html.Div(
    children=[
        html.H1(children="Hello Dash"),
        html.Div(
            children="""
        Dash: A web application framework for your data.
    """
        ),
        dcc.Graph(id="interval-graph", figure=fig),
        dcc.Interval(
            id="interval-component", interval=0.3 * 1000, n_intervals=1  # in milliseconds
        ),
    ],
    style={"background-color": "#D5E3EA", "color": "black", "height": "100%", "width": "100%"},
)


@app.callback(
    Output("interval-graph", "figure"), Input("interval-component", "n_intervals")
)
def update_figure(_):

    df = pd.read_csv("sentiment_scores.txt", names=["score"])
    df["color"] = "red"
    df["rolling_score"] = df["score"].rolling(20, min_periods=1).mean()
    fig = px.line(df["rolling_score"][-50:], range_y=[-1, 1])
    fig.update_layout(plot_bgcolor="rgb(191,204,210)", paper_bgcolor="rgb(213,227,234)")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0')
