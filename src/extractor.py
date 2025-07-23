from bs4 import BeautifulSoup
import pandas as pd
import json
import os
import logging
from datetime import datetime

from src.utils import validar_resultados

def extraer_desde_html(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    html_path = config["html_path"]
    selectors = config["selectors"]

    # 🔁 Parámetros para exportar
    keyword = config.get("nombre_busqueda", "busqueda")
    fecha_actual = datetime.today().strftime('%Y%m%d')
    output_csv = f"data/{keyword}_{fecha_actual}.csv"
    fecha_scraping = datetime.today().strftime('%Y-%m-%d')

    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, "html.parser")
    except FileNotFoundError:
        logging.error(f"Archivo HTML no encontrado: {html_path}")
        return
    except Exception as e:
        logging.exception("Error al leer el archivo HTML")
        return

    contenedores = soup.select(selectors["container"])

    datos = []
    for i, cont in enumerate(contenedores):
        try:
            # Título y empresa
            titulo_tag = cont.find("h3")
            empresa_tag = cont.find("a", class_="text-primary")
            enlace_tag = cont.find("a", href=True)

            # Nuevos campos más controlados
            ubicacion_tag = cont.select_one("b")
            estado_tag = cont.select_one("span.badge")
            salario_tag = cont.find(text=lambda t: "€" in t if t else False)

            # 🔁 Normalizar ubicación
            ubicacion_bruta = ubicacion_tag.get_text(strip=True) if ubicacion_tag else ""
            ciudad = modalidad = ""
            if "(" in ubicacion_bruta:
                ciudad, modalidad = ubicacion_bruta.split("(", 1)
                ciudad = ciudad.strip()
                modalidad = modalidad.replace(")", "").strip()
            else:
                ciudad = ubicacion_bruta.strip()

            datos.append({
                "titulo": titulo_tag.get_text(strip=True) if titulo_tag else "",
                "empresa": empresa_tag.get_text(strip=True) if empresa_tag else "",
                "enlace": f"https://www.tecnoempleo.com{enlace_tag['href']}" if enlace_tag else "",
                "ciudad": ciudad,
                "modalidad": modalidad,
                "estado": estado_tag.get_text(strip=True) if estado_tag else "",
                "salario": salario_tag.strip() if salario_tag else "",
                "fecha_scraping": fecha_scraping
            })

        except Exception as e:
            logging.warning(f"Error al procesar contenedor {i}: {e}")

    validar_resultados(datos, contexto=config.get("url", "archivo local"))

    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(datos)
    df.to_csv(output_csv, index=False, encoding='utf-8')
    logging.info(f"CSV guardado en: {output_csv}")
