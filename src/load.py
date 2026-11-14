"""Chargement des données financières dans SQLite."""

import sqlite3
from pathlib import Path
import pandas as pd


def initialiser_base(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS cours (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            ticker TEXT,
            cloture REAL,
            volume REAL,
            rendement_journalier REAL,
            moyenne_mobile_7 REAL,
            moyenne_mobile_30 REAL
        )
    """)
    conn.execute("CREATE INDEX IF NOT EXISTS idx_ticker_date ON cours(ticker, date)")
    conn.commit()
    return conn


def charger(conn: sqlite3.Connection, df: pd.DataFrame, ticker: str) -> int:
    if df is None or df.empty:
        return 0
    conn.execute("DELETE FROM cours WHERE ticker = ?", (ticker,))
    count = 0
    for _, row in df.iterrows():
        conn.execute(
            """INSERT INTO cours 
               (date, ticker, cloture, volume, rendement_journalier, moyenne_mobile_7, moyenne_mobile_30)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                str(row["date"])[:10],
                ticker,
                row.get("cloture"),
                row.get("volume"),
                row.get("rendement_journalier"),
                row.get("moyenne_mobile_7"),
                row.get("moyenne_mobile_30"),
            ),
        )
        count += 1
    conn.commit()
    return count
