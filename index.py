import os

import dash
from dash import Input, Output, State, html
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
# from dash_bootstrap_components._components.Container import Container



external_stylesheets = [dbc.themes.CERULEAN]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

# title = html.Div(
#     [
#         html.H1("Crypto Charts",
#                 style={'text-align': 'center'}),
#         html.H4("compare blockchains and applications at a glance",
#                 style={'text-align': 'center', 'color': 'grey'})
#     ], className='card-title'
# )

# # collapse_content = dbc.Card([dbc.Row([            html.Div("One of three columns"),
# # #     dbc.Col(time_interval_filter),
# # #                                       dbc.Col(bundle_filter),
# # #                                       dbc.Col(category_filter),
# # #                                       dbc.Col(blockchain_filter)
# # ]
# #                                      )], color="light")

# # navbar = html.Div(
# #     [
# #         dbc.Button(
# #             "Filters",
# #             id="collapse-button",
# #             className="mb-3",
# #             color="primary",
# #             n_clicks=0,
# #         ),
# #         dbc.Collapse(
# #             collapse_content,
# #             id="collapse",
# #             is_open=False,
# #         ),
# #     ],
# # )


# # @app.callback(
# #     Output("collapse", "is_open"),
# #     [Input("collapse-button", "n_clicks")],
# #     [State("collapse", "is_open")],
# # )
# # def toggle_collapse(n, is_open):
# #     if n:
# #         return not is_open
# #     return is_open

# search_bar = dbc.Row(
#     [
#         dbc.Col(dbc.Input(type="search", placeholder="Search")),
#         dbc.Col(
#             dbc.Button(
#                 "Search", color="primary", className="ms-2", n_clicks=0
#             ),
#             width="auto",
#         ),
#     ],
#     className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
#     align="center",
# )

# navbar = dbc.Navbar(
#     dbc.Container(
#         [
#             html.A(
#                 # Use row and col to control vertical alignment of logo / brand
#                 dbc.Row(
#                     [
#                         dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
#                         dbc.Col(dbc.NavbarBrand("Navbar", className="ms-2")),
#                     ],
#                     align="center",
#                     className="g-0",
#                 ),
#                 href="https://plotly.com",
#                 style={"textDecoration": "none"},
#             ),
#             dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
#             dbc.Collapse(
#                 search_bar,
#                 id="navbar-collapse",
#                 is_open=False,
#                 navbar=True,
#             ),
#         ]
#     ),
#     color="dark",
#     dark=True,
# )


# # add callback for toggling the collapse on small screens
# @app.callback(
#     Output("navbar-collapse", "is_open"),
#     [Input("navbar-toggler", "n_clicks")],
#     [State("navbar-collapse", "is_open")],
# )
# def toggle_navbar_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# app.layout = html.Div([title,
#                        navbar,
# #                        cards,
# #                        attribution
#                       ]
#                       ,
#                       style={'margin-top': 10, 'margin-bottom': 10,
#                              'margin-right': '25px', 'margin-left': '25px',
#                              }
#                       )

app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA'
    ),
    html.Div(id='display-value')
])

@app.callback(dash.dependencies.Output('display-value', 'children'),
                [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
