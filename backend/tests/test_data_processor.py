import sys
import os
import pytest
import sqlite3

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app.seeder import seed, create_tables
from app.data_processor import (
    get_kpis_generales,
    get_promedio_por_materia,
    get_evolucion_temporal,
    get_estudiantes_en_riesgo,
)


@pytest.fixture
def conn():
    """SQLite in-memory con datos sintéticos."""
    c = sqlite3.connect(":memory:")
    seed(c)
    yield c
    c.close()


def test_seed_populates_tables(conn):
    assert conn.execute("SELECT COUNT(*) FROM estudiantes").fetchone()[0] == 20
    assert conn.execute("SELECT COUNT(*) FROM materias").fetchone()[0]    == 6
    assert conn.execute("SELECT COUNT(*) FROM notas").fetchone()[0]       == 360


def test_kpis_generales_sin_filtro(conn):
    kpis = get_kpis_generales(conn)
    assert 0.0 <= kpis["promedio"] <= 10.0
    assert kpis["total_estudiantes"] == 20
    assert 0.0 <= kpis["pct_aprobados"] <= 100.0
    assert kpis["en_riesgo"] >= 0


def test_kpis_generales_con_filtro(conn):
    kpis_todos    = get_kpis_generales(conn)
    kpis_filtrado = get_kpis_generales(conn, where="WHERE n.periodo = '2024-1'")
    # El promedio general de todos los períodos no tiene que ser igual al de un período
    assert isinstance(kpis_filtrado["promedio"], float)
    assert kpis_filtrado["total_estudiantes"] <= kpis_todos["total_estudiantes"]


def test_promedio_por_materia(conn):
    df = get_promedio_por_materia(conn)
    assert not df.empty
    assert "materia"  in df.columns
    assert "promedio" in df.columns
    assert all(0.0 <= p <= 10.0 for p in df["promedio"])
    assert len(df) == 6  # 6 materias


def test_evolucion_temporal(conn):
    df = get_evolucion_temporal(conn)
    assert not df.empty
    assert "periodo"  in df.columns
    assert "promedio" in df.columns
    assert len(df) == 3  # 3 períodos


def test_estudiantes_en_riesgo_criterio(conn):
    df = get_estudiantes_en_riesgo(conn)
    if not df.empty:
        for _, row in df.iterrows():
            assert (row["nota"] < 4.0) or (row["asistencia"] < 75), (
                f"Fila no cumple criterio de riesgo: nota={row['nota']}, asist={row['asistencia']}"
            )


def test_estudiantes_en_riesgo_vacio(conn):
    """Si forzamos todas las notas >= 4 y asistencia >= 75, no debe haber riesgo."""
    conn.execute("UPDATE notas SET nota = 8.0, asistencia_pct = 90.0")
    conn.commit()
    df = get_estudiantes_en_riesgo(conn)
    assert df.empty
