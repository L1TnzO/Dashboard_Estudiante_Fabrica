import os
import sqlite3
import streamlit as st
import pandas as pd

# Imports con path relativo al módulo
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.data_processor import (
    get_kpis_generales,
    get_promedio_por_materia,
    get_evolucion_temporal,
    get_estudiantes_en_riesgo,
)
from app.seeder import seed, create_tables

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "db.sqlite3")


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    create_tables(conn)
    if conn.execute("SELECT COUNT(*) FROM estudiantes").fetchone()[0] == 0:
        seed(conn)
    return conn


# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Dashboard de Rendimiento Académico",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🎓 Dashboard de Rendimiento Académico")
st.caption("Fábrica DASHBOARD v1.0.0 — PROYECTO_UNO")
st.markdown("---")

conn = get_connection()

# ── Sidebar de filtros ───────────────────────────────────────────────────────
with st.sidebar:
    st.header("🔍 Filtros")

    periodos = pd.read_sql("SELECT DISTINCT periodo FROM notas ORDER BY periodo", conn)["periodo"].tolist()
    periodo_sel = st.selectbox("Período", ["Todos"] + periodos)

    cursos = pd.read_sql("SELECT DISTINCT curso FROM estudiantes ORDER BY curso", conn)["curso"].tolist()
    curso_sel = st.selectbox("Curso", ["Todos"] + cursos)

    carreras = pd.read_sql("SELECT DISTINCT carrera FROM estudiantes ORDER BY carrera", conn)["carrera"].tolist()
    carrera_sel = st.selectbox("Carrera", ["Todos"] + carreras)

    st.markdown("---")
    st.caption("Umbral de aprobación: **nota ≥ 4.0**")
    st.caption("Riesgo asistencia: **< 75 %**")

# WHERE dinámico
conditions = []
if periodo_sel  != "Todos": conditions.append(f"n.periodo = '{periodo_sel}'")
if curso_sel    != "Todos": conditions.append(f"e.curso = '{curso_sel}'")
if carrera_sel  != "Todos": conditions.append(f"e.carrera = '{carrera_sel}'")
where = ("WHERE " + " AND ".join(conditions)) if conditions else ""

# ── Tabs principales ─────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Resumen General",
    "📚 Por Materia",
    "📈 Evolución Temporal",
    "⚠️ Alumnos en Riesgo",
])

# ── Tab 1: Resumen ───────────────────────────────────────────────────────────
with tab1:
    kpis = get_kpis_generales(conn, where)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("📊 Promedio General",   f"{kpis['promedio']:.2f} / 10")
    c2.metric("👥 Total Estudiantes",  kpis["total_estudiantes"])
    c3.metric("✅ % Aprobados",        f"{kpis['pct_aprobados']:.1f} %")
    c4.metric("⚠️ En Riesgo",         kpis["en_riesgo"])

    st.markdown("---")
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Aprobados vs. Reprobados")
        aprobados   = kpis["pct_aprobados"]
        reprobados  = 100.0 - aprobados
        df_pie = pd.DataFrame({
            "Categoría":  ["✅ Aprobados", "❌ Reprobados"],
            "Porcentaje": [aprobados, reprobados],
        })
        st.bar_chart(df_pie.set_index("Categoría"))
    with col_b:
        st.subheader("Resumen de filtros activos")
        st.info(
            f"**Período:** {periodo_sel}  \n"
            f"**Curso:** {curso_sel}  \n"
            f"**Carrera:** {carrera_sel}"
        )

# ── Tab 2: Por Materia ───────────────────────────────────────────────────────
with tab2:
    st.subheader("Promedio por Materia")
    df_mat = get_promedio_por_materia(conn, where)
    if df_mat.empty:
        st.info("Sin datos para los filtros seleccionados.")
    else:
        st.bar_chart(df_mat.set_index("materia")["promedio"])
        st.dataframe(df_mat, use_container_width=True)

# ── Tab 3: Evolución temporal ────────────────────────────────────────────────
with tab3:
    st.subheader("Evolución del Promedio General por Período")
    st.caption("(Vista histórica — independiente de filtros de curso/carrera)")
    df_evo = get_evolucion_temporal(conn)
    if df_evo.empty:
        st.info("Sin datos de evolución disponibles.")
    else:
        st.line_chart(df_evo.set_index("periodo")["promedio"])
        st.dataframe(df_evo, use_container_width=True)

# ── Tab 4: Riesgo ────────────────────────────────────────────────────────────
with tab4:
    st.subheader("Estudiantes en Situación de Riesgo Académico")
    st.caption("Criterio: nota < 4.0  **ó**  asistencia < 75 %")
    df_riesgo = get_estudiantes_en_riesgo(conn, where)
    if df_riesgo.empty:
        st.success("✅ Sin estudiantes en riesgo para los filtros seleccionados.")
    else:
        st.warning(f"⚠️ {len(df_riesgo)} registros con riesgo académico detectado.")
        st.dataframe(df_riesgo, use_container_width=True)

conn.close()
