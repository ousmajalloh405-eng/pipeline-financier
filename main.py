"""Pipeline financier — Yahoo Finance."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from extract import extraire_historique
from transform import transformer
from load import initialiser_base, charger


DB_PATH = Path(__file__).parent / "data" / "finance.db"
TICKERS = ["AAPL", "MSFT", "GOOGL", "TSLA"]


def afficher_resume(conn, ticker: str):
    print(f"\n--- {ticker} ---")
    row = conn.execute("""
        SELECT cloture, rendement_journalier, moyenne_mobile_7
        FROM cours
        WHERE ticker = ?
        ORDER BY date DESC
        LIMIT 1
    """, (ticker,)).fetchone()
    if row:
        print(f"Dernier cours : {row[0]}")
        print(f"Rendement jour : {row[1]}")
        print(f"Moyenne mobile 7j : {row[2]}")


def main():
    print("=== Pipeline financier Yahoo Finance ===\n")

    conn = initialiser_base(DB_PATH)

    for ticker in TICKERS:
        print(f"Traitement de {ticker}...")
        brut = extraire_historique(ticker, jours=90)
        propre = transformer(brut)
        if propre is not None:
            nb = charger(conn, propre, ticker)
            print(f"  → {nb} lignes chargées")
            afficher_resume(conn, ticker)
        else:
            print("  → échec")

    conn.close()
    print(f"\nBase créée : {DB_PATH}")
    print("Pipeline terminé.")


if __name__ == "__main__":
    main()
