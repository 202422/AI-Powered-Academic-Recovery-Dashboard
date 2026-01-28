import pandas as pd


def compute_improvability(df: pd.DataFrame, config: dict) -> pd.DataFrame:
    """
    Compute Student Support Complexity Score (SSCS)
    """

    scoring_cfg = config["scoring"]

    weights = scoring_cfg["risk_weights"]

    # =========================
    # SSCS base score
    # =========================
    df["SSCS"] = sum(
        weights[col] * df[col]
        for col in weights
    )

    # =========================
    # Grade complexity factor
    # =========================
    bins = scoring_cfg["grade_bins"]
    factors = scoring_cfg["complexity_factors"]

    df["grade_complexity_factor"] = pd.cut(
        df["FinalGrade"],
        bins=bins,
        labels=factors,
        include_lowest=True
    ).astype(float)

    # =========================
    # Final score
    # =========================
    normalization = scoring_cfg.get("normalization_factor", 1.0)

    df["SSCS_final"] = (
        df["SSCS"] + df["grade_complexity_factor"]
    ) / normalization

    # =========================
    # Improvability Score
    # =========================
    df["ImprovabilityScore"] = 1 - df["SSCS_final"]

    return df
