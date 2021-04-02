import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_dangerously_set_inner_html

"""
-------------------------------------------------------------------------------
Header Tab 1
-------------------------------------------------------------------------------
"""

HEADER_TAB_1 = html.Div(
    children=[
        html.H1(
            children=[
                "Pooya! ",
                html.Small(
                    children=[
                        "Interface Builder for Bootstrap"
                    ]
                )
            ],
            className='page-header m-1 pb-2')
    ],
    className="page-header m-1 pb-2"
)
