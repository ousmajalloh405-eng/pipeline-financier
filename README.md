# Pipeline financier — Yahoo Finance

> Pipeline ETL qui récupère des cours boursiers via Yahoo Finance, calcule des indicateurs et les stocke dans SQLite.

**Statut** : 🟢 Réalisé  
**Catégorie** : ⚙️ Création de pipelines ETL  
**Portfolio** : [Profil GitHub](https://github.com/ousmajalloh405-eng)

---

## 1. Problème métier

Suivre l’évolution de plusieurs actions (Apple, Microsoft, Google, Tesla) et calculer des indicateurs simples pour analyse.

## 2. Architecture ETL

```
Yahoo Finance (yfinance)
        │
        ▼
   extract.py
        │
        ▼
  transform.py  →  rendement, moyennes mobiles
        │
        ▼
    load.py     →  data/finance.db
```

## 3. Technologies

- Python 3
- `yfinance` (données Yahoo Finance)
- `pandas`
- SQLite

## 4. Installation et exécution

```bash
git clone https://github.com/ousmajalloh405-eng/pipeline-financier.git
cd pipeline-financier
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

## 5. Indicateurs calculés

- Cours de clôture
- Rendement journalier
- Moyenne mobile 7 jours
- Moyenne mobile 30 jours

## 6. Compétences pour le CV

Développement d’un pipeline ETL Python récupérant des données financières via Yahoo Finance, avec calcul d’indicateurs et stockage relationnel.

---

*Projet réalisé dans le cadre de la formation Data — Sonatel Academy.*
