import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from app import app, server
from apps import home, technical, resources


sidebar_header = dbc.Row(
	[
		dbc.Col(html.H2("COVID-19", className="h1", style={'color':'#ffffff'})),
		dbc.Col(
			html.Button(
				html.Span(className="navbar-toggler-icon"),
				className="navbar-toggler",
				style={"color": "rgba(0,0,0,.5)","border-color": "rgba(250,250,250,.3)"},
				id="toggle",
			),
			width="auto",
			align="center",
		),
	]
)

sidebar = html.Div(
    [
        sidebar_header,
        html.Div(
            [
                html.Hr(style={'borderColor':'#ffffff'}),
                html.P("Monitoring the very first pandemic caused by a coronavirus.",
                className="lead",style={'color':'#ffffff','textAlign':'justify'})
            ],
            id="blurb",
        ),
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("DASHBOARD", href="/home", id="page-1-link",style={'color':'#ffffff'}),
                    dbc.NavLink("TECHNICAL", href="/apps/technical", id="page-2-link",style={'color':'#ffffff'}),
                    dbc.NavLink("RESOURCES", href="/apps/resources", id="page-3-link",style={'color':'#ffffff'}),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
    style={'backgroundColor':'#017cbf'}
)

content = html.Div(id="page-content", style={'backgroundColor':'#dfe6e9',})

def serve_layout():
	return html.Div([dcc.Location(id="url"), sidebar, content])

app.layout = serve_layout

# active pill
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        return True, False, False
    return [pathname == "/home", pathname == "/apps/technical", pathname == "/apps/resources"]
    
# toggle -- side bar when hidden (interaction)
@app.callback(
    Output("collapse", "is_open"),
    [Input("toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# this is where linking to other apps happen
@app.callback(Output("page-content", "children"), 
			[Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname in ["/", "/home"]:
        return home.layout
    elif pathname == "/apps/technical":
        return technical.layout
    elif pathname == "/apps/resources":
        return resources.layout
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

if __name__ == "__main__":
    app.run_server(debug=True)
