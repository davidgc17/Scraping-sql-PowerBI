from bs4 import BeautifulSoup
import pandas as pd
import os

def extraer_peliculas_desde_html(html_path, salida_csv):
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    peliculas = soup.find_all("a", class_="block hover:opacity-75")

    datos = []
    for peli in peliculas:
        titulo = peli.get("title", "Sin título")
        enlace = peli.get("href", "")
        img_tag = peli.find("img")
        imagen = img_tag["src"] if img_tag else "Sin imagen"

        datos.append({
            "Título": titulo,
            "Enlace": enlace,
            "Imagen": imagen
        })

    df = pd.DataFrame(datos)
    df.to_csv(salida_csv, index=False, encoding="utf-8")
    print(f"{len(datos)} películas guardadas en {salida_csv}")

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    extraer_peliculas_desde_html("data/t.html", "data/peliculas_extraidas.csv")
