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
                className="w-100 h-100 mx-4 mb-4"
            )
        ],
        className="row"
    ),
    html.Div(
        children=[
            html.Div(
                children=[
                    dash_table.DataTable(
                        id='table_TAB1_BODY_CARD1',
                        style_table={
                            'overflowX': 'auto',
                            'overflowY': 'auto',
                            # 'padding': '5px'
                        },
                        style_cell={
                            'border': '1px solid grey',
                            'font-size': '14px',
                            # 'font_family': 'B Koodak',
                            'text_align': 'right',
                            'minWidth': 50,
                            'maxWidth': 100,
                            'width': 75
                        },
                        style_header={
                            'backgroundColor': 'rgb(230, 230, 230)',
                            'fontWeight': 'bold',
                            'whiteSpace': 'normal',
                        },
                        css=[{
                            'selector': '.dash-table-tooltip',
                            'rule': 'background-color: yellow;'
                        }],
                        tooltip_delay=0,
                        tooltip_duration=None,
                        page_size=15
                    )

                ],
                className="w-100 h-100 mx-3"
            )

        ],
        className="row justify-content-center"
    )
]
