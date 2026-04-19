import dash
from dash import html, dcc, Dash
import dash_bootstrap_components as dbc

APP_TITLE = "PyQuant - A Quantitative Finance Toolkit in Python"


def start_app(debug: bool = True):
    app = Dash(
        APP_TITLE,
        external_stylesheets=[dbc.themes.LUX],
        use_pages=True,
        pages_folder="src/python_quant/app/pages",
        assets_folder="src/python_quant/app/assets",
    )
    """
    ===========================================================================
    Page Registry
    """

    # Get the list of registered pages by category
    page_registry = dash.page_registry
    pages_by_category = {}
    for page in page_registry.values():
        category = page.get("category", "Uncategorized")
        if category not in pages_by_category:
            pages_by_category[category] = []
        pages_by_category[category].append(page)


    """
    ===========================================================================
    Main Layout
    """

    category_list = html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.H5(category),
                            html.Ul(
                                [
                                    html.Li(
                                        dcc.Link(page["name"], href=page["path"])
                                    )
                                    for page in pages
                                ]
                            ),
                        ],
                        className="mb-4",
                    )
                    for category, pages in pages_by_category.items()
                ]
            )
        ]
    )

    layout = dbc.Container(
        [
            dbc.Row(
                dbc.Col(
                    html.H2(
                        APP_TITLE,
                        className="text-center bg-primary text-white p-2",
                    ),
                )
            ),
            dbc.Row(
                [
                    dbc.Col(category_list, width=12, lg=3, className="mt-4 border"),
                    dbc.Col(
                        dash.page_container,
                        width=12,
                        lg=9,
                        className="mt-4 border",
                    ),
                ],
                className="ms-1",
            ),
        ],
        fluid=True,
    )
    app.layout = layout
    app.run(debug=debug, threaded=True)
