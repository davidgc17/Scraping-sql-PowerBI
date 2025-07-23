import csv
import sqlite3
import os

# Configuración
DB_PATH = "db/aplicaciones.db"
CSV_PATH = "data/python_20250723.csv"  # Cambia esto según el archivo generado

# Conectar a SQLite y crear la tabla si no existe
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS ofertas_filtradas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    empresa TEXT,
    enlace TEXT UNIQUE,
    ciudad TEXT,
    modalidad TEXT,
    estado TEXT,
    salario TEXT,
    fecha_scraping TEXT,
    comentario TEXT
)
""")
conn.commit()

# Leer el CSV
with open(CSV_PATH, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print("\n📌 Oferta:")
        print(f"🔹 Título:    {row['titulo']}")
        print(f"🏢 Empresa:   {row['empresa']}")
        print(f"📍 Ubicación: {row['ciudad']} ({row['modalidad']})")
        print(f"📅 Estado:    {row['estado']} – {row['fecha_scraping']}")
        print(f"💰 Salario:   {row['salario']}")
        print(f"🔗 Enlace:    {row['enlace']}")

        respuesta = input("¿Te interesa esta oferta? (s/n): ").strip().lower()

        if respuesta == "s":
            comentario = input("Comentario (opcional): ").strip()

            try:
                cursor.execute("""
                INSERT INTO ofertas_filtradas (
                    titulo, empresa, enlace, ciudad, modalidad,
                    estado, salario, fecha_scraping, comentario
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    row['titulo'],
                    row['empresa'],
                    row['enlace'],
                    row['ciudad'],
                    row['modalidad'],
                    row['estado'],
                    row['salario'],
                    row['fecha_scraping'],
                    comentario
                ))
                conn.commit()
                print("✅ Oferta guardada.")
            except sqlite3.IntegrityError:
                print("⚠️ Ya existe una oferta con ese enlace (duplicado).")

        else:
            print("❌ Oferta descartada.")

conn.close()
print("\n🎉 Proceso completado. Todas las ofertas revisadas.")
