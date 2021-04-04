import base64
from dash_bootstrap_components._components.Label import Label
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
from dash_html_components.Div import Div
import dash_table


import numpy as np
from datetime import date


from layouts.visualization import *



"""
-------------------------------------------------------------------------------
Tab 1
-------------------------------------------------------------------------------
"""

"""
---------------------------------------
Card 1: 
---------------------------------------
"""

BODY_TAB_1 = [
    html.Div(
        children=[
            dcc.Graph(
                id='map_TAB1_BODY_CARD1',
                className="w-100 h-100"
            )         
        ],
        className="row"
    ),
    html.Div(
        children=[
            dash_table.DataTable(
                id='table_TAB1_BODY_CARD1',
                style_table={
                    'overflowX': 'auto',
                    'overflowY': 'auto',
                    'padding':'5px'
                },
                style_cell={
                    'border': '1px solid grey',
                    'font-size': '12px',
                    # 'font_family': 'B Koodak',
                    'font_size': '12px',
                    'text_align': 'right',
                    'minWidth': 100,
                    'maxWidth': 150,
                    'width': 125
                },
                style_header={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'fontWeight': 'bold',
                    'whiteSpace': 'normal',
                },
                page_size=15
            )
        ],
        className="row justify-content-center"
    )
]