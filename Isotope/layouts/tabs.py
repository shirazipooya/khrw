import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_dangerously_set_inner_html


from layouts.visualization import *


from layouts.headers import *
from layouts.sidebars import *
from layouts.footers import *
from layouts.body import *


"""
-------------------------------------------------------------------------------
Tab 1
-------------------------------------------------------------------------------
"""

TAB_1 = html.Div(
    children=[
        # Header --------------------------------------------------------------
        html.Div(
            children=[
                html.Div(
                    children=[
                        HEADER_TAB_1
                    ],
                    className="col"
                )
            ],
            className="row"
        ),
        # Sidebar & Body ------------------------------------------------------
        html.Div(
            children=[
                # Sidebar ---------------------------------
                html.Div(
                    children=[
                        SIDEBAR_TAB_1
                    ],
                    className='my-sidebar'
                ),
                # Body ------------------------------------
                html.Div(
                    children=[
                        html.Div(
                            children=BODY_TAB_1,
                            className="container-fluid"
                        )
                    ],
                    className='my-body'
                ),
            ],
            className="row p-0 m-0 w-100"
        ),
        # Footer --------------------------------------------------------------
        html.Div(
            children=[
                html.Div(
                    children=[
                        FOOTER_TAB_1
                    ],
                    className="col"
                )
            ],
            className="row"
        ),
        # Hidden Div For Store Data--------------------------------------------
        html.Div(
            children=[
                html.Div(
                    id="database",
                )
            ],
            style={
                'display': 'none'
            }
        )
    ],
    className="container-fluid p-0"
)
