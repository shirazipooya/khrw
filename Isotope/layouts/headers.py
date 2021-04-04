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
        html.H2(
            children=[
                dcc.Markdown(
                    dangerously_allow_html=True,
                    children=[
                        '''
                        <b>Isotope Analysis!</b> 
                        <small>Stable Isotope Compositions 
                        (<b>δ<sup>2</sup>H</b> & <b>δ<sup>18</sup>O</b>) 
                        of Rainfall</small>
                        '''
                    ]
                )
            ],
            className='page-header m-1 pb-2 text-dark')
    ],
    className="page-header m-1 pt-2"
)
