# Scraping + SQL + Power BI 🚀

Proyecto de automatización y análisis de ofertas de empleo técnicas, combinando scraping web, base de datos en SQLite y visualización con Power BI.

---

## 🔧 Tecnologías usadas

- Python (requests, BeautifulSoup, sqlite3)
- SQLite
- Power BI Desktop
- VSCode + SQLite Explorer (opcional)
- DB Browser for SQLite (visualización alternativa)

---

## 📁 Estructura del proyecto

scraping_sql_powerBI/
├── src/ # Scraper y extracción HTML
├── config/ # Configuraciones JSON por origen
├── data/ # Archivos HTML y CSV generados
├── db/ # Base de datos SQLite
├── scripts/ # Scripts interactivos y utilidades
│ └── filtrar_ofertas_interactivamente.py
├── consultas.sql # Consultas SQL útiles
├── schema.sql # Definición de tablas SQL
├── requirements.txt
└── README.md

markdown
Copiar
Editar

---

## 🧠 Flujo de trabajo

1. **Scraping automático** desde Tecnoempleo (`src/`)
2. **Extracción enriquecida**: título, empresa, ciudad, modalidad, salario, estado, fecha
3. **CSV personalizado** generado por búsqueda y fecha
4. **Filtrado interactivo** desde consola (`scripts/`): el usuario revisa las ofertas una a una y guarda solo las interesantes en `ofertas_filtradas`
5. **Almacenamiento** en SQLite (`aplicaciones.db`)
6. (Pendiente) **Visualización con Power BI directamente conectado a SQLite**

