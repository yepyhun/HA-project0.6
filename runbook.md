# Runbook

## v0.6 – UC/Selenium kapcsolható driver réteg

**Váltás UC ↔ Selenium:**
- Állítsd a `STEALTH_MODE` ENV-et: `uc` vagy `selenium`, majd indítsd újra a folyamatot.
- Indításkor a logban megjelenik: `driver=uc|selenium`, `headless=...` + diagnosztikák (`navigator.webdriver`, UA, UC verzió).

**UC frissítési rutin (Chrome főverzió váltás):**
1) Telepítsd az új Chrome főverziót.
2) Ha UC nem talál kompatibilis drivert, állítsd a `CHROME_MAJOR` ENV-et az új főverzióra (pl. `126`); nem kell kódot módosítani.

**Gyors diagnosztika:**
```bash
python3 bin/run_browser_diag.py
# várható logok: driver=..., diag.navigator.webdriver=..., diag.ua=..., diag.uc_version=...
```
