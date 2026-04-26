import dash
from dash import html, dcc, callback, Input, Output
PAGE_TITLE = "Black-Scholes-Merton"
PAGE_CAT = "Derivative Models"
dash.register_page(__name__, path="/bsm", name=PAGE_TITLE, category=PAGE_CAT)


