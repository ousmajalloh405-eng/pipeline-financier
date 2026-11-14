"""Transformation des données financières."""

import pandas as pd
from typing import Optional


def transformer(df: Optional[pd.DataFrame]) -> Optional[pd.DataFrame]:
    """Nettoie et calcule des indicateurs simples."""
    if df is None or df.empty:
        return None

    df = df.copy()

    # Aplatir les colonnes MultiIndex si nécessaire
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] for col in df.columns]

    # Garder les colonnes utiles
    colonnes = ["Date", "Close", "Volume", "ticker"]
    df = df[[c for c in colonnes if c in df.columns]]

    # Renommer
    df = df.rename(columns={"Date": "date", "Close": "cloture", "Volume": "volume"})

    # Supprimer les lignes avec valeurs manquantes
    if "cloture" not in df.columns:
        return None
    df = df.dropna(subset=["cloture"])

    # Indicateurs
    df["rendement_journalier"] = df["cloture"].pct_change()
    df["moyenne_mobile_7"] = df["cloture"].rolling(window=7).mean()
    df["moyenne_mobile_30"] = df["cloture"].rolling(window=30).mean()

    # Arrondir
    for col in ["cloture", "rendement_journalier", "moyenne_mobile_7", "moyenne_mobile_30"]:
        if col in df.columns:
            df[col] = df[col].round(4)

    return df
