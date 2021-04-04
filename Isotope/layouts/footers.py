import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_dangerously_set_inner_html

"""
-------------------------------------------------------------------------------
Footer Tab 1
-------------------------------------------------------------------------------
"""

FOOTER_TAB_1 = html.Div(
    children=[
        html.Small(
            dcc.Markdown(
                dangerously_allow_html=True,
                children=[
                    '''
                    © All Rights Reserved by
                    <b>Khorasan Razavi Regional Water Authority</b>
                    '''
                ]
            ),
            className='page-header m-1 py-2')
    ],
    className="page-header text-center"
)
