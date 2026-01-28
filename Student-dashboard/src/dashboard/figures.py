import plotly.express as px

def create_scatter(df):

    df = df.sort_values("FinalGrade", ascending=False)

    fig = px.scatter(
        df,
        x="FinalGrade",
        y="ImprovabilityScore",
        hover_data={
            "FirstName": True,
            "FamilyName": True,
            "FinalGrade": True,
            "absences": True,
            "failures": True,
            "studytime": True,
            "Walc": True,
            "Fjob": True,
            "famsup": True,
            "ImprovabilityScore": ":.2f"
        },
        labels={
            "ImprovabilityScore": "ImprovabilityScore",
            "FinalGrade": "FinalGrade"
        },
        title="Students prioritization"
    )

    fig.update_traces(marker=dict(size=12))

    fig.update_layout(
        height=800,  # <-- ici on agrandit l'échelle verticale
        xaxis=dict(autorange="reversed"),
        hoverlabel=dict(bgcolor="white")
    )

    return fig
