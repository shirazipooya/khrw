import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_dangerously_set_inner_html


from layouts.visualization import *


from layouts.headers import *
from layouts.sidebars import *
from layouts.footers import *


"""
-------------------------------------------------------------------------------
Tab 1
-------------------------------------------------------------------------------
"""

TAB_1 = html.Div(
    children=[

        # Page Header
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

        # Page Main
        html.Div(
            children=[

                # Sidebar
                html.Div(
                    children=[
                        SIDEBAR_TAB_1
                    ],
                    className='my-sidebar'
                ),

                #
                html.Div(
                    children=[
                        "This is Main Page"
                    ],
                    className='col border p-1 m-1'
                ),

            ],
            className="row p-0 m-0 w-100"
        ),

        # Page Footer
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


    ],
    className="container-fluid p-0"
)
