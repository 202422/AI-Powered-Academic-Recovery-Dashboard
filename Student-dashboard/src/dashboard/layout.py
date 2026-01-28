from dash import html, dcc
from src.dashboard.components.kpi_card import kpi_card


layout = html.Div(
    style={
        "width": "95%",
        "margin": "auto",
        "fontFamily": "Arial, sans-serif",
        "backgroundColor": "#f8f9fa",
        "padding": "20px"
    },

    children=[

        # ======================
        # HEADER
        # ======================
        html.Div(
            style={
                "backgroundColor": "#1f2c56",
                "padding": "25px",
                "borderRadius": "15px",
                "color": "white",
                "marginBottom": "25px"
            },
            children=[
                html.H1(
                    "Student Support Dashboard",
                    style={"marginBottom": "5px"}
                ),
                html.P(
                    "AI-driven prioritization of students requiring academic support",
                    style={"fontSize": "16px", "opacity": "0.85"}
                )
            ]
        ),

        # ======================
        # KPI CARDS
        # ======================
        html.Div(
    style={
        "display": "grid",
        "gridTemplateColumns": "repeat(3, 1fr)",
        "gap": "20px",
        "marginBottom": "30px"
    },
    children=[
        kpi_card("Students", "total-students"),
        kpi_card("Average Grade", "avg-grade"),
        kpi_card("Avg Score", "avg-score")
    ]
),

        # ======================
        # MAIN GRAPH CARD
        # ======================
        html.Div(
            style={
                "backgroundColor": "white",
                "padding": "25px",
                "borderRadius": "15px",
                "boxShadow": "0px 4px 20px rgba(0,0,0,0.08)"
            },
            children=[

                html.H3(
                    "FinalGrade vs ImprovabilityScore",
                    style={"marginBottom": "10px"}
                ),

                html.P(
                    "Each point represents a student. "
                    "Higher ImprovabilityScore indicates lower complexity to improve academic performance.",
                    style={"color": "#6c757d"}
                ),

                dcc.Graph(
                    id="scatter-plot",
                    config={"displayModeBar": False}
                )
            ]
        )
    ]
)
