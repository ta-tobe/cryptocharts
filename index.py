import os

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container



external_stylesheets = [dbc.themes.CERULEAN]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

title = html.Div(
    [
        html.H1("Crypto Charts",
                style={'text-align': 'center'}),
        html.H4("compare blockchains and applications at a glance",
                style={'text-align': 'center', 'color': 'grey'})
    ], className='card-title'
)

time_interval_filter = html.Div([
    html.Div([html.P('Time interval:')],
             style={'display': 'inline-block', 'margin-left': '5px', 'margin-right': '15px'}),

    html.Div([dcc.DatePickerRange(
        id='date-picker-range',
        start_date=(pd.to_datetime(today) - pd.Timedelta(1, unit='d')).strftime('%Y-%m-%d'),
        end_date=today,
        display_format='YYYY-M-DD')],
        style={'display': 'inline-block'})
])

bundle_filter = html.Div([
    html.Div([html.P('Bundle:')],
             style={'display': 'inline-block', 'margin-left': '5px', 'margin-right': '15px'}),
    html.Div([dbc.RadioItems(
        id='multichain-radioitems',
        options=[{'label': 'Multi-chain', 'value': 'M'},
                 {'label': 'Single-chain', 'value': 'S'}],
        value='M'
    )])
])

category_filter = html.Div([
    html.Div([html.P('Category:')],
             style={'margin-left': '5px', 'margin-right': '15px'}),
    html.Div([dcc.Dropdown(
        id='category-dropdown',
        options=[
            {'label': i, 'value': i} for i in df.category.unique().tolist()
        ],
        value=df.category.unique().tolist(),
        multi=True
    )])
])

blockchain_filter = html.Div([
    html.Div([html.P('Blockchain:')],
             style={'margin-left': '5px', 'margin-right': '15px'}),
    html.Div([dcc.Dropdown(
        id='blockchain-dropdown',
        options=[
            {'label': i, 'value': i} for i in df.blockchain.unique().tolist()
        ],
        value=df.blockchain.unique().tolist(),
        multi=True
    )])
])

collapse_content = dbc.Card([dbc.Row([            html.Div("One of three columns"),
#     dbc.Col(time_interval_filter),
#                                       dbc.Col(bundle_filter),
#                                       dbc.Col(category_filter),
#                                       dbc.Col(blockchain_filter)
]
                                     )], color="light")

navbar = html.Div(
    [
        dbc.Button(
            "Filters",
            id="collapse-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),
        dbc.Collapse(
            collapse_content,
            id="collapse",
            is_open=False,
        ),
    ],
)


@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


app.layout = html.Div([title,
                       navbar,
#                        cards,
#                        attribution
                      ]
                      ,
                      style={'margin-top': 10, 'margin-bottom': 10,
                             'margin-right': '25px', 'margin-left': '25px',
                             }
                      )

# app.layout = html.Div([
#     html.H2('Hello World'),
#     dcc.Dropdown(
#         id='dropdown',
#         options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
#         value='LA'
#     ),
#     html.Div(id='display-value')
# ])

# @app.callback(dash.dependencies.Output('display-value', 'children'),
#                 [dash.dependencies.Input('dropdown', 'value')])
# def display_value(value):
#     return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(debug=True)
