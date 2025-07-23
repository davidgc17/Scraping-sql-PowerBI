import logging
import os

def configurar_logging(nombre_log="scraper.log"):
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler(os.path.join("logs", nombre_log), encoding="utf-8"),
            logging.StreamHandler()
        ]
    )


def validar_resultados(lista_datos, contexto=""):
    if not lista_datos:
        logging.warning(f"No se encontraron datos en: {contexto}")
    else:
        logging.info(f"Se extrajeron {len(lista_datos)} entradas de {contexto}")
