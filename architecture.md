# Architecture — Pipeline financier

## Flux

```
┌────────────────┐
│  Yahoo Finance  │
│   (yfinance)    │
└────────┬───────┘
         │
         ▼
┌────────────────┐
│   extract.py    │
└────────┬───────┘
         │
         ▼
┌────────────────┐
│  transform.py   │
│  - rendement    │
│  - MM7 / MM30   │
└────────┬───────┘
         │
         ▼
┌────────────────┐
│    load.py      │
│  → finance.db   │
└────────────────┘
```

## Table `cours`

- date, ticker, cloture, volume
- rendement_journalier
- moyenne_mobile_7
- moyenne_mobile_30
