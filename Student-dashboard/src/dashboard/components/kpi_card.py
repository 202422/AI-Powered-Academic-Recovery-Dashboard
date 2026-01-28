from dash import html

def kpi_card(title, value_id):

    return html.Div(
        style={
            "backgroundColor": "white",
            "padding": "20px",
            "borderRadius": "12px",
            "boxShadow": "0px 2px 10px rgba(0,0,0,0.08)",
            "textAlign": "center"
        },
        children=[
            html.H4(title),
            html.H2(id=value_id, children="—")
        ]
    )
