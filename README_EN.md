# 📊 Scraping + SQL + Power BI
![Python](https://img.shields.io/badge/python-3.11+-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Scraping](https://img.shields.io/badge/automation-playwright-informational?logo=playwright)

A complete project for automation, analysis and visualization of tech job offers. It combines web scraping, storage in a local SQLite database and dynamic visualizations with Power BI.

---

## 🚀 Technologies used

- **Python** – requests, BeautifulSoup, Playwright, sqlite3  
- **SQLite** – Lightweight relational database queried from Power BI  
- **Power BI Desktop** – Data visualization  
- **VSCode + SQLite Explorer** (optional)  
- **DB Browser for SQLite** – Manual database inspection and edits

---

## 📁 Project structure

```
Scraping-sql-PowerBI/
├── data/
├── db/
├── config/
├── scripts/
├── src/
├── Makefile
├── requirements.txt
└── README.md
```

---

## 🔄 Workflow

1. Automated scraping of job listings from Tecnoempleo using Playwright  
2. Custom CSV output named `<keyword>_<YYYYMMDD>.csv`  
3. Interactive filtering via console script  
4. Storage of selected offers in SQLite (`ofertas_filtradas`)  
5. Visualization in Power BI by connecting directly to the database

---

## 📸 Screenshots

1. Scraping execution in terminal  
2. Interactive filtering of job offers  
3. Database preview in DB Browser  
4. Power BI dashboards (full table, tech distribution, cities)

---

## 📦 Installation & Usage

```bash
# 1. Clone the repo and enter the directory
git clone https://github.com/davidgc17/Scraping-sql-PowerBI.git
cd Scraping-sql-PowerBI

# 2. Create a virtual environment
python -m venv .venv

# 3. Activate it
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Install Playwright browsers
python -m playwright install
```

```bash
# 6. Run the scraper
make scrape
# or
python main.py
```

```bash
# 7. Filter offers with the interactive script
python scripts/filtrar_ofertas_interactivamente.py
```

```text
# 8. Configure your search
Edit config/tecnoempleo.json and set:
- "url": the Tecnoempleo search URL
- "nombre_busqueda": used in the output file name
```

```text
# 9. Visualize with Power BI
- Open Power BI Desktop
- Get data → ODBC or SQLite
- Select db/aplicaciones.db
- Load the table ofertas_filtradas
- Build your custom dashboards
```

---

## 🔍 Example SQL Queries

```sql
-- All offers
SELECT * FROM ofertas_filtradas;

-- Offers per city
SELECT ciudad, COUNT(*) FROM ofertas_filtradas GROUP BY ciudad ORDER BY COUNT(*) DESC;

-- Offers per technology
SELECT estado, COUNT(*) FROM ofertas_filtradas GROUP BY estado ORDER BY COUNT(*) DESC;

-- Remote-only offers
SELECT * FROM ofertas_filtradas WHERE modalidad = '100% remoto';

-- Offers per scrape date
SELECT fecha_scraping, COUNT(*) FROM ofertas_filtradas GROUP BY fecha_scraping ORDER BY fecha_scraping DESC;
```

---

## 📬 About Me

This project is part of my personal portfolio as a developer focused on automation and data analysis.  
I'm especially interested in web scraping, Power BI visualization, and backend development.

📧 Contact: davidga276@gmail.com
