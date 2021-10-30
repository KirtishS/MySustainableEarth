import dash
from dash.dependencies import Output, Input
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc


from dashboard_components.population_vs_electricity_section import population_vs_electricity_section
from dashboard_components.glaciers_oil_areas_dash import glacier_and_oil_impacts
from dashboard_components.emissions import emission_section
from dashboard_components.catastrophe_section import catastrophe_section
from dashboard_components.machine_learning_section import machine_learning_results

from non_renewable import non_renewable_info
from renewable import renewable_info

fstcard = dbc.Card(
            dbc.CardBody([
                dbc.Row(
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H3("Impact on Earth", className="card-title"),
                                    html.H4("Humans are the only beings who are contributing to this huge temperature rise.", className="card-title"),
                                    html.P("Livings on this planet is a blessing to us but we don't realise the importance of the resources being provided by Mother Earth to us. The quote says it rightly 'Human needs can't be fulfilled, craving for more is our non-removable nature. But do we realise on what cost we are fulfilling our needs and what is the adverse side effect of this huge craving, the answer would be a big' NO", className="card-text"),
                                    html.P("Global warming is the increase of average world temperature as a result of what is known as the greenhouse effect. ", className="card-text"),
                                ]
                            ),
                            dbc.CardImg(src="https://media.newyorker.com/photos/5d7baf31a5350d0008a14576/master/pass/McKibben-ClimateFinance2.jpg", bottom=True),
                        ],
                    )


            ),html.Hr(),
            ]),
            className="mt-6 mt-auto",
        )

sndcrd = dbc.Card(
    dbc.CardBody([
        dbc.Row(
            dbc.Card(
                [
                    dbc.CardImg(
                        src="https://images.unsplash.com/photo-1571896851392-055658ba3c9f?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fGdsb2JhbCUyMHdhcm1pbmd8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60",
                        bottom=True),
                    dbc.CardBody(
                        [
                            html.P("We use coal and oil but what do we produce, we produce Carbon Dioxide(CO2). We produce nuclear power but on what cost. ",className="card-text"),
                            html.P("The price paid is the death of people and the hazardous side effect of the test which is conducted is the extinction of those Oxygen producing blessings that are TREES. We cut of the trees to set up industrial amuzement parks and the stocks go up to give us a huge profit and a enourmous anual turnover but on what on cost and are we benefitted by the loss of pure air we breathe. We use fuel run automobiles and what do we do produce CO2, SO2, NO2 and the adverse effect goes on to be global warming, noise pollution, acid rain and hugely affecting problems that is melting of glaciers.",className="card-text"),
                        ]
                    ),
                ],
            )
        ), html.Hr(),
    ]),
    className="mt-6 mt-auto",
)

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#0D1321",
    "color" : "#F0EBD8",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H4("My Sustainable Earth"),
        html.Hr(),

        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Analysis", href="/page-1", active="exact"),
                dbc.NavLink("Solutions", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)



def dashboard():

    app = dash.Dash(external_stylesheets=[dbc.themes.DARKLY])

    @app.callback(
        Output("page-content", "children"),
        [Input("url", "pathname")]
    )
    def render_page_content(pathname):
        if pathname == "/":
            return [
                html.Hr(),
                html.H2(children="Electricity Generation Information:"),
                population_vs_electricity_section(app),

                html.Hr(),

                html.H2(children="Glaciers and Oil"),
                glacier_and_oil_impacts(app),

                html.Hr(),

                html.H2(children="Emissions:"),
                emission_section(app),

                html.Hr(),

                html.H2(children="Catastrophe Information:"),
                catastrophe_section(app),

                html.Hr(),
            ]
        elif pathname == "/page-1":
            return [
                html.H2(children="Machine Learning Results:"),
                machine_learning_results(app),

                html.Hr(),

                html.H2(children="Awareness"),

                dbc.Row([
                    dbc.Col(fstcard, width=6),
                    dbc.Col(sndcrd, width=6),
                ]),

                html.Hr(),
            ]
        elif pathname == "/page-2":
            return [
                html.H3(children="Non renewable"),

                non_renewable_info(app),

                html.Hr(),

                html.H3(children="Renewable"),

                renewable_info(app),

                html.Hr(),
            ]

    app.layout = html.Div([
        dcc.Location(id="url"),
        sidebar,
        content
    ])

    return app


if __name__ == "__main__":
    app = dashboard()
    app.run_server(debug=True)
