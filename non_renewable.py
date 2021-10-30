from dash import html
import dash_bootstrap_components as dbc

def coal_tab(app):
    tab1 = dbc.Card(
        dbc.CardBody([
            dbc.Row(
                dbc.Card(
                    [
                        html.Iframe(src="https://www.youtube.com/embed/JONcq3KPsQo",title="YouTube video player",height="315"),
                        dbc.CardBody(
                            [
                                html.H2("Coal"),
                                html.P(
                                    "COAL Highly Taxed Several principal emissions result from coal combustion:1.Sulfur dioxide (SO2), which contributes to acid rain and respiratory illnesses.2.Nitrogen oxides (NOx), which contribute to smog and respiratory illnesses. ",
                                    className="card-text"),
                                html.P(
                                    "Coal phase-out has a positive synergy between the global climate challenge and local environmental pollution. In international climate negotiations, governments need to factor-in that exiting coal is a cheap way to substantially reduce global greenhouse gas emissions and has huge co-benefits at home. Our study shows that national and global interests are not necessarily trading-off, but can go hand in hand.  ",
                                    className="card-text"),
                            ]
                        ),
                    ],
                )
            ), html.Hr(),
        ]),
        className="mt-6 mt-auto",
    )
    return tab1

def oil_tab(app):
    tab1 = dbc.Card(
        dbc.CardBody([
            dbc.Row(
                dbc.Card(
                    [
                        html.Iframe(src="https://www.youtube.com/embed/yn2oV1WSEfA",title="YouTube video player",height="315"),
                        dbc.CardBody(
                            [
                                html.H2("Oil"),
                                html.Ol([
                                  html.Li("Pollution impacts communities.") ,
                                  html.Li("Dangerous emissions fuel climate change.") ,
                                  html.Li("Oil and gas development can ruin wildlands.") ,
                                  html.Li("Drilling disrupts wildlife habitat.") ,
                                  html.Li("Oil spills can be deadly to animals.") ,
                                ]),
                                html.P("""
Oil and gas drilling has a serious impact on our wildlands and communities. Drilling projects operate around the clock generating pollution, fueling climate change, disrupting wildlife and damaging public lands that were set aside to benefit all people.""",
                                    className="card-text"),
                                # html.P(
                                #     "Coal phase-out has a positive synergy between the global climate challenge and local environmental pollution. In international climate negotiations, governments need to factor-in that exiting coal is a cheap way to substantially reduce global greenhouse gas emissions and has huge co-benefits at home. Our study shows that national and global interests are not necessarily trading-off, but can go hand in hand.  ",
                                #     className="card-text"),
                            ]
                        ),
                    ],
                )
            ), html.Hr(),
        ]),
        className="mt-6 mt-auto",
    )
    return tab1

def natgas_tab(app):
    tab1 = dbc.Card(
        dbc.CardBody([
            dbc.Row(
                dbc.Card(
                    [
                        html.Iframe(src="https://www.youtube.com/embed/vyEt4rckt7E",title="YouTube video player",height="315"),
                        dbc.CardBody(
                            [
                                html.H2("Natural Gas"),
                                html.P(
                                    "COAL Highly Taxed Several principal emissions result from coal combustion:1.Sulfur dioxide (SO2), which contributes to acid rain and respiratory illnesses.2.Nitrogen oxides (NOx), which contribute to smog and respiratory illnesses. ",
                                    className="card-text"),
                                html.P(
                                    "Coal phase-out has a positive synergy between the global climate challenge and local environmental pollution. In international climate negotiations, governments need to factor-in that exiting coal is a cheap way to substantially reduce global greenhouse gas emissions and has huge co-benefits at home. Our study shows that national and global interests are not necessarily trading-off, but can go hand in hand.  ",
                                    className="card-text"),
                            ]
                        ),
                    ],
                )
            ), html.Hr(),
        ]),
        className="mt-6 mt-auto",
    )
    return tab1

def non_renewable_info(app):
    tabs = dbc.Tabs(
        [
            dbc.Tab(oil_tab(app), label="Oil" ),
            dbc.Tab(coal_tab(app), label="Coal"),
            dbc.Tab(natgas_tab(app), label="Natural Gas"),
        ]
    )
    return tabs


