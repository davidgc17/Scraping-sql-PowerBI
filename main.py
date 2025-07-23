import json
import sys
import os
import logging

from src.extractor import extraer_desde_html
from src.browser import obtener_html_con_playwright
from src.utils import configurar_logging

def cargar_config(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    configurar_logging()
    config_path = os.path.join("config", "tecnoempleo.json")

    if not os.path.exists(config_path):
        logging.error(f"Archivo de configuración no encontrado: {config_path}")
        sys.exit(1)

    config = cargar_config(config_path)

    if config["source"] == "html":
        extraer_desde_html(config_path)

    elif config["source"] == "url":
        base_dir = os.path.dirname(os.path.abspath(__file__))
        html_path = os.path.join(base_dir, config["html_path"])


        obtener_html_con_playwright(
            url=config["url"],
            output_path=html_path,
            selector_espera=config["selectors"].get("container"),
            tiempo_extra=2
        )

        extraer_desde_html(config_path)

    else:
        logging.warning(f"Modo de extracción no soportado: {config['source']}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.exception("Error inesperado durante la ejecución del scraper")
