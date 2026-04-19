import dash
from dash import html

PAGE_TITLE = "Home Page"
PAGE_CAT = "Instructions"

dash.register_page(__name__, path="/", name=PAGE_TITLE, category=PAGE_CAT)

layout = html.Div(
    children=[
        html.H2(children="Overview"),
        html.P(
            children="""
        The models and analytics are categorized into the following sections:
        """),
        html.H3(children="Calibrated Models"),
        html.P(
            "These are models that have been calibrated to market data and can be used for pricing and risk management. Examples include: " \
            "Yield Curve, Volatility Surface, etc."
        ),
        html.H3(children="Fixed Income Analytics"),
        html.P(
            "These are tools for analyzing fixed income securities, including bond pricing, duration, convexity, and yield calculations."
        ),
        html.H3(children="Derivatives Models"),
        html.P(
            "These are models for pricing and analyzing derivatives securities, including Black Scholes, Binomial etc."
        ),
        html.H3(children="Credit Models"),
        html.P(
            "These are models for analyzing credit risk and pricing credit derivatives, including CDS Pricer etc."
        ),

    ]
)
