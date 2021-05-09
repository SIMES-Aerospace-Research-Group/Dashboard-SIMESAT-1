import dash_bootstrap_components as dbc
import dash_html_components as html

LOGO = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/160/apple/81/satellite_1f6f0.png"

sidebar = html.Div(
    [
        html.Div(
            [
                #  width: 3rem ensures the logo is the exact width of the collapsed sidebar (acounting for padding)
                html.Img(src=LOGO, style={"width":"4rem"}),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fas fa-home mr-2"),
                    html.Span("Home")],
                    href="/",
                    active="exact",
                    className="sidebar__header__text--grey",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-stethoscope mr-2"),
                        html.Span("Demo"),
                    ],
                    href="/demo",
                    active="exact",
                    className="sidebar__header__text--grey",
                ),
                dbc.NavLink(
                    [
                        #html.I(className="fas fa-envelope-open-t mr-2"),
                        html.I(className="fab fa-github mr-2"),
                        html.Span("GitHub Repository"),
                    ],
                    href="https://github.com/CxrlosKenobi/SIMESAT-CanSat-v1",
                    target="_blank",
                    active="exact",
                    className="sidebar__header__text--grey",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)