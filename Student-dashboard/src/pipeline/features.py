import numpy as np

def create_features(df):
    # -----------------------------
    # Job risk mapping
    # -----------------------------
    job_risk = {
        "teacher": 0.0,
        "health": 0.2,
        "services": 0.4,
        "at_home": 0.6,
        "other": 0.8
    }

    # -----------------------------
    # Risk feature engineering
    # -----------------------------

    # Family support
    df["famsup_risk"] = df["famsup"].map({
        "yes": 0.0,
        "no": 1.0
    })

    # Past failures
    df["failures_risk"] = np.where(
        df["failures"] < 4,
        0.0,
        1.0
    )

    # Father's job
    df["Fjob_risk"] = df["Fjob"].map(job_risk)

    # Health (1 = very bad, 5 = very good)
    df["health_risk"] = 1 - (df["health"] - 1) / 4

    # Internet access
    df["internet_risk"] = df["internet"].map({
        "yes": 0.0,
        "no": 1.0
    })

    # Absences (normalized)
    df["absences_risk"] = (
        df["absences"] / df["absences"].max()
    )

    # Study time (1 = very low, 4 = very high)
    df["studytime_risk"] = 1 - (df["studytime"] - 1) / 3

    # School support
    df["schoolsup_risk"] = df["schoolsup"].map({
        "yes": 0.0,
        "no": 1.0
    })

    return df
