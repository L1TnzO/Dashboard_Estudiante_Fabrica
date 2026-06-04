import sqlite3
import os
import random


def create_tables(conn):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS estudiantes (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre  TEXT    NOT NULL,
        curso   TEXT    NOT NULL,
        carrera TEXT    NOT NULL
    );
    CREATE TABLE IF NOT EXISTS materias (
        id       INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre   TEXT    NOT NULL,
        codigo   TEXT    UNIQUE NOT NULL,
        creditos INTEGER NOT NULL
    );
    CREATE TABLE IF NOT EXISTS notas (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        estudiante_id   INTEGER NOT NULL REFERENCES estudiantes(id),
        materia_id      INTEGER NOT NULL REFERENCES materias(id),
        periodo         TEXT    NOT NULL,
        nota            REAL    NOT NULL,
        asistencia_pct  REAL    NOT NULL
    );
    """)
    conn.commit()


def seed(conn):
    create_tables(conn)

    nombres = [
        "Ana García", "Luis Martín", "María López", "Carlos Pérez", "Laura Díaz",
        "Jorge Torres", "Sofía Ruiz", "Miguel Chen", "Andrea Silva", "Pablo Mora",
        "Valentina Castro", "Rodrigo Fuentes", "Camila Vargas", "Diego Romero",
        "Isabella Vega", "Mateo Soto", "Gabriela Muñoz", "Sebastián Lara",
        "Natalia Jiménez", "Felipe Guerrero",
    ]
    cursos = ["1A", "1B", "2A", "2B", "3A"]
    carreras = ["Informática", "Electrónica", "Industrial"]

    materias_data = [
        ("Matemáticas I", "MAT101", 6),
        ("Programación I", "PRG101", 6),
        ("Física I",       "FIS101", 4),
        ("Álgebra Lineal", "MAT201", 6),
        ("Estructuras de Datos", "PRG201", 6),
        ("Estadística",    "MAT301", 4),
    ]
    periodos = ["2024-1", "2024-2", "2025-1"]

    conn.executemany(
        "INSERT OR IGNORE INTO materias (nombre, codigo, creditos) VALUES (?,?,?)",
        materias_data,
    )
    for i, nombre in enumerate(nombres):
        conn.execute(
            "INSERT OR IGNORE INTO estudiantes (nombre, curso, carrera) VALUES (?,?,?)",
            (nombre, cursos[i % len(cursos)], carreras[i % len(carreras)]),
        )
    conn.commit()

    cursor = conn.cursor()
    estudiantes = cursor.execute("SELECT id FROM estudiantes").fetchall()
    materias    = cursor.execute("SELECT id FROM materias").fetchall()

    random.seed(42)
    for est in estudiantes:
        for mat in materias:
            for per in periodos:
                nota   = round(random.uniform(2.0, 10.0), 1)
                asist  = round(random.uniform(50.0, 100.0), 1)
                conn.execute(
                    "INSERT INTO notas (estudiante_id, materia_id, periodo, nota, asistencia_pct) VALUES (?,?,?,?,?)",
                    (est[0], mat[0], per, nota, asist),
                )
    conn.commit()


if __name__ == "__main__":
    db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "db.sqlite3")
    conn = sqlite3.connect(db_path)
    seed(conn)
    conn.close()
    print("Base de datos sembrada exitosamente.")
