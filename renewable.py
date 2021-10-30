from dash import html
import dash_bootstrap_components as dbc

def renewables_tab(app):
    tab1 = dbc.Card(
        dbc.CardBody([
            dbc.Row(
                dbc.Card(
                    [
                        html.Iframe(src="https://www.youtube.com/embed/lNQmwWFwiiQ",title="YouTube video player",height="315"),
                        dbc.CardBody(
                            [
                                html.H2("Renewables"),
                                html.P("Renewable power is booming, as innovation brings down costs and starts to deliver on the promise of a clean energy future. American solar and wind generation are breaking records and being integrated into the national electricity grid without compromising reliability.",
                                    className="card-text"),
                                html.P("This means that renewables are increasingly displacing “dirty” fossil fuels in the power sector, offering the benefit of lower emissions of carbon and other types of pollution. But not all sources of energy marketed as “renewable” are beneficial to the environment. Biomass and large hydroelectric dams create difficult tradeoffs when considering the impact on wildlife, climate change, and other issues. Here’s what you should know about the different types of renewable energy sources—and how you can use these emerging technologies at your own home. ",
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

def nuclear_tab(app):
    tab1 = dbc.Card(
        dbc.CardBody([
            dbc.Row(
                dbc.Card(
                    [
                        html.Iframe(src="https://www.youtube.com/embed/vt179qMm_1o",title="YouTube video player",height="315"),
                        dbc.CardBody(
                            [
                                html.H2("Nuclear"),
                                html.P("""
One side effect of nuclear power is the amount of nuclear waste it produces. It has been estimated that the world produces some 34,000m3 of nuclear waste each year, waste that takes years to degrade.
Anti-nuclear environmental group Greenpeace released a report in January 2019 that detailed what it called a nuclear waste ‘crisis’ for which there is ‘no solution on the horizon’. One such solution was a concrete nuclear waste ‘coffin’ on Runit Island, which has begun to crack open and potentially release radioactive material.""", className="card-text"),

                                html.P("""
 The initial costs for building a nuclear power plant are steep. A recent virtual test reactor in the US estimate rose from $3.5bn to $6bn alongside huge extra costs to maintain the facility. South Africa scrapped plans to add 9.6GW of nuclear power to its energy mix due to the cost, which was estimated anywhere between $34-84bn. So whilst nuclear plants are cheap to run and produce inexpensive fuel, the initial costs are off-putting.                                 """,
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

def carb_price_tab(app):
    tab1 = dbc.Card(
        dbc.CardBody([
            dbc.Row(
                dbc.Card(
                    [
                        html.Iframe(src="https://www.youtube.com/embed/_4gbACmsBTw",title="YouTube video player",height="315"),
                        dbc.CardBody(
                            [
                                html.H2("Carbon Price"),
                                html.P("""
                                    Following the 2015 Paris Climate Agreement, there has been a growing understanding of the structural changes required across the global economy to shift to a low-carbon economy. The increasing regulation of carbon emissions through taxes, emissions trading schemes, and fossil fuel extraction fees is expected to play a vital role in global efforts to address climate change. Central to these efforts to reduce carbon dioxide (CO2) emission is a market mechanism known as carbon pricing.
                                    """,
                                    className="card-text"),
                                html.P("""
 Set by governments or markets, carbon prices cover a part of a country’s total emissions, charging C02 emitters for each ton released through a tax or a fee. Those fees may also apply to methane, nitrous oxide, and other gases that contribute to rising global temperatures. In a cap-and-trade system of carbon pricing, the government sets a cap on the total amount of emissions allowed, and C02 emitters are either given permits or allowances or must buy the right to emit C02; companies whose total emissions fall under the cap may choose to sell their unused emissions credits to those who surpass its carbon allotment. Either way, carbon pricing takes advantage of market mechanisms to create financial incentives to lower emissions by switching to more efficient processes or cleaner fuels.                                """,
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

def renewable_info(app):
    tabs = dbc.Tabs(
        [
            dbc.Tab(renewables_tab(app), label="Renewables"),
            dbc.Tab(nuclear_tab(app), label="Nuclear"),
            dbc.Tab(carb_price_tab(app), label="Carbon Price"),
        ]
    )
    return tabs


