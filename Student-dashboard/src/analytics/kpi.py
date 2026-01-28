# src/analytics/kpi.py
import pandas as pd

def compute_kpis(df):
    """
    Calcule les principaux KPI pour le dashboard.

    Args:
        df (pd.DataFrame): DataFrame contenant les colonnes nécessaires
            - FinalGrade
            - SSCS_final

    Returns:
        dict: dictionnaire contenant les KPI
    """
    total_students = len(df)
    
    
    # Moyenne des notes
    avg_grade = df["FinalGrade"].mean()
    
    # Moyenne SSCS
    avg_score = df["ImprovabilityScore"].mean()
    
    return {
        "total_students": total_students,
        "avg_grade": avg_grade,
        "avg_score": avg_score
    }
