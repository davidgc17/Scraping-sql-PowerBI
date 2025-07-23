\# Scraping + SQL + Power BI 🚀



Proyecto de automatización y análisis de ofertas de empleo técnicas, combinando scraping web, base de datos en SQLite y visualización con Power BI.



\## 🔧 Tecnologías usadas



\- Python (requests, BeautifulSoup)

\- SQLite (vía `sqlite3`)

\- Power BI Desktop

\- Visual Studio Code (entorno de trabajo)



\## 📁 Estructura del proyecto



scraping\_sql\_powerBI/

├── scraper/ # Código para extraer datos (ej. tecnoempleo)

├── db/ # Base de datos SQLite local

├── exporter/ # Scripts para exportar a CSV

├── powerbi/ # Dashboards, capturas y archivo .pbix

├── schema.sql # Estructura de la base de datos

├── consultas.sql # Consultas SQL útiles

├── requirements.txt # Dependencias del proyecto

└── README.md



markdown

Copiar

Editar



\## 💡 Objetivo



\- Automatizar la recogida de datos de portales como \[Tecnoempleo](https://www.tecnoempleo.com/)

\- Almacenarlos de forma estructurada en SQLite

\- Visualizarlos mediante Power BI para obtener estadísticas sobre el mercado laboral



\## 📊 Estado del proyecto



\- \[x] Estructura inicial

\- \[ ] Primer scraper funcional

\- \[ ] Inserción de datos en SQLite

\- \[ ] Exportación y conexión con Power BI

