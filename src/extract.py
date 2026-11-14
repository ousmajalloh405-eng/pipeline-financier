"""Extraction des données financières via Yahoo Finance (yfinance)."""

from datetime import datetime, timedelta
from typing import Optional
import yfinance as yf


def extraire_historique(ticker: str, jours: int = 90) -> Optional[object]:
    """Télécharge l'historique des prix pour un ticker."""
    try:
        fin = datetime.now()
        debut = fin - timedelta(days=jours)
        data = yf.download(ticker, start=debut.strftime("%Y-%m-%d"),
                           end=fin.strftime("%Y-%m-%d"), progress=False)
        if data.empty:
            print(f"Aucune donnée pour {ticker}")
            return None
        data = data.reset_index()
        data["ticker"] = ticker
        return data
    except Exception as e:
        print(f"Erreur extraction {ticker}: {e}")
        return None
