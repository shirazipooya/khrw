import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_dangerously_set_inner_html

from server import app
from layouts.tabs import *


"""
-------------------------------------------------------------------------------
Tab Pan
-------------------------------------------------------------------------------
"""
TAB_PAN = html.Div(
    children=[

        # Nav Tabs ------------------------------------------------------------
        dash_dangerously_set_inner_html.DangerouslySetInnerHTML(
            """
                    <ul class="nav nav-tabs mt-1" role="tablist">
                        <li class="nav-item">
                            <a class="nav-link active" data-toggle="tab" href="#Tab_1">Data Entry Tab</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-toggle="tab" href="#Tab_2">Section 2</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" data-toggle="tab" href="#Tab_3">Section 3</a>
                        </li>
                    </ul>
            """
        ),

        # Tab Panes -----------------------------------------------------------
        html.Div(
            children=[
                html.Div(
                    children=[
                        TAB_1
                    ],
                    className="tab-pane active",
                    id="Tab_1"
                ),
                html.Div(
                    children=[
                        "Section 2"
                    ],
                    className="tab-pane fade",
                    id="Tab_2"
                ),
                html.Div(
                    children=[
                        "Section 3"
                    ],
                    className="tab-pane fade",
                    id="Tab_3"
                )
            ],
            className="tab-content"
        )
    ],
    className="tabbable"
)


"""
-------------------------------------------------------------------------------
Main Layout
-------------------------------------------------------------------------------
"""

main_layout = html.Div(
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        TAB_PAN
                    ],
                    className="col"
                )
            ],
            className="row"
        )
    ],
    className="container-fluid"
)
