from dash import Output, Input
from .figures import create_scatter
from src.analytics.kpi import compute_kpis  # à créer si pas encore fait

def register_callbacks(app, df):

    @app.callback(
        Output("scatter-plot", "figure"),
        Output("total-students", "children"),
        Output("avg-grade", "children"),
        Output("avg-score", "children"),
        Input("scatter-plot", "id")  # déclencheur au chargement
    )
    def update_dashboard(_):

        # -----------------------------
        # 1️⃣ Créer la figure
        # -----------------------------
        fig = create_scatter(df)

        # -----------------------------
        # 2️⃣ Calculer les KPI
        # -----------------------------
        kpis = compute_kpis(df)
        # kpis devrait retourner un dict avec :
        # {"total_students": ..., "high_complexity": ..., "avg_grade": ..., "avg_sscs": ...}

        # -----------------------------
        # 3️⃣ Retourner tous les outputs
        # -----------------------------
        return (
            fig,
            kpis["total_students"],
            round(kpis["avg_grade"], 2),
            round(kpis["avg_score"], 2)
        )
