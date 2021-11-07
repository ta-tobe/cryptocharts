import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
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

if __name__ == '__main__':
    app.run_server(debug=True)
