# Checklist de Requisitos — Dashboard de Rendimiento Académico

## Constitución de la Fábrica
- [x] Objetivo definido: Dashboard académico con Streamlit + Pandas + SQLite.
- [x] Stack gobernado: Python 3, Streamlit, Pandas, SQLite, pytest.
- [x] Sin invención de reglas de negocio.
- [x] Criterios de aceptación funcionales definidos.

## Proyecto PROYECTO_UNO
- [x] **REQ-001 (KPIs):** promedio, total_estudiantes, pct_aprobados, en_riesgo.
- [x] **REQ-002 (Por Materia):** Promedio y % aprobados por materia con gráfico.
- [x] **REQ-003 (Evolución):** Serie temporal del promedio por período.
- [x] **REQ-004 (Riesgo):** Filtrado por nota < 4.0 OR asistencia < 75%.
- [x] **REQ-005 (Filtros):** Sidebar con período, curso, carrera.
- [x] **REQ-006 (Seeder):** 20 estudiantes × 6 materias × 3 períodos, seed=42.