import dash
import plotly.express as px
from dash import dcc
from dash import dash_table
from dash import html
import plotly.express as px
import pandas as pd
import app
from src import create_app

from .data import create_dataframe
from .layout import html_layout

def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/dashapp/",
    )

    # Load DataFrame
    df = create_dataframe()
    fig = px.histogram(df,
        title='Usuarios por pais',
        x = 'pais')
    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div(
        
        children=[
            dcc.Graph(
                id="histogram-graph",
                figure = fig
            ),
        ],
        id="dash-container",
    )
    return dash_app.server