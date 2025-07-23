from playwright.sync_api import sync_playwright
import time
import os
import logging
import random

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Version/14.0.3 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/111.0.0.0 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 Version/14.1 Mobile/15E148 Safari/604.1"
]

def simular_interaccion(page):
    logging.info("Simulando interacción humana...")
    try:
        x = random.randint(50, 500)
        y = random.randint(50, 500)
        page.mouse.move(x, y, steps=30)
        time.sleep(random.uniform(0.5, 1.5))

        for _ in range(2):
            delta = random.randint(200, 600)
            page.mouse.wheel(0, delta)
            time.sleep(random.uniform(0.4, 1.2))
    except Exception:
        logging.warning("No se pudo simular interacción, puede ignorarse si la web no lo requiere.")

def verificar_html_bloqueado(html):
    if not html.strip():
        return "El HTML está vacío."
    sospechosas = ["access denied", "forbidden", "not authorized", "bot detected"]
    html_lower = html.lower()
    for palabra in sospechosas:
        if palabra in html_lower:
            return f"Detectado posible bloqueo: contiene '{palabra}'"
    return None

def obtener_html_con_playwright(url, output_path, selector_espera=None, tiempo_extra=0):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)

            user_agent = random.choice(USER_AGENTS)
            logging.info(f"Usando User-Agent: {user_agent}")
            page = browser.new_page(user_agent=user_agent)

            logging.info(f"Cargando página: {url}")
            page.goto(url)

            if selector_espera:
                logging.info(f"Esperando selector: {selector_espera}")
                try:
                    page.wait_for_selector(selector_espera, timeout=10000)
                except:
                    logging.warning("No se encontró el selector dentro del tiempo esperado")

            if tiempo_extra > 0:
                aleatorio = random.uniform(tiempo_extra * 0.8, tiempo_extra * 1.5)
                logging.info(f"Esperando {aleatorio:.2f} segundos (aleatorio)...")
                time.sleep(aleatorio)

            simular_interaccion(page)

            html = page.content()

            motivo_bloqueo = verificar_html_bloqueado(html)
            if motivo_bloqueo:
                logging.error(motivo_bloqueo)
                return

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(html)

            logging.info(f"HTML guardado en: {output_path}")

    except Exception as e:
        logging.exception("Error al usar Playwright para obtener el HTML")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_path = os.path.join(base_dir, "data", "t.html")

    obtener_html_con_playwright(
        url="https://flickfocus.com",
        output_path=output_path,
        selector_espera="a.block.hover\:opacity-75",
        tiempo_extra=2
    )

