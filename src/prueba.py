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
    fig = px.histogram(df['pais'])
    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div(
        
        children=[
            dcc.Graph(
                id="histogram-graph",
                figure = fig
            ),
            
            html.Div(
                children=[
            dcc.Graph(
                id="histogram-grap21h",
                
            ),
            
            
        ],
            )
        ],
        
        id="dash-container",
    )
    return dash_app.server
    

def create_histograma(df):
    """Create Dash datatable from Pandas DataFrame."""
    """ fig = px.histogram(df)
    fig.show() """
    table = dash_table.DataTable(
        id="database-table",
        sort_action="native",
        sort_mode="native",
        page_size=300,
    )
    return table

def create_histograma2(df):
    """Create Dash datatable from Pandas DataFrame."""
    """ fig = px.histogram(df)
    fig.show() """
    table = dash_table.DataTable(
        id="database-table2",
        sort_action="native",
        sort_mode="native",
        page_size=300,
    )
    return table