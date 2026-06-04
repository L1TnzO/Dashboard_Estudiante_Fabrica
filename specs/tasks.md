# Checklist de Tareas — Dashboard de Rendimiento Académico

- [ ] **T-001 (DDL y Seeder):** Crear `seeder.py` con DDL de las 3 tablas y poblar con 360 registros sintéticos (seed=42). (→ REQ-006)
- [ ] **T-002 (Data Processor):** Implementar `data_processor.py` con funciones: `get_kpis_generales`, `get_promedio_por_materia`, `get_evolucion_temporal`, `get_estudiantes_en_riesgo`. Cada función recibe `conn` y `where` opcional. (→ REQ-001..REQ-004)
- [ ] **T-003 (Dashboard Streamlit):** Crear `main.py` con page config, sidebar de filtros, 4 tabs (Resumen, Por Materia, Evolución, Riesgo), métricas st.metric, gráficos st.bar_chart/st.line_chart y tabla de riesgo con highlight. (→ REQ-005, REQ-006 y todos los AC UI)
- [ ] **T-004 (Suite pytest):** Crear `tests/test_data_processor.py` con 7 tests usando fixture de SQLite in-memory. (→ AC-001..AC-007)
- [ ] **T-005 (requirements.txt):** Documentar dependencias: streamlit, pandas, pytest. (→ Plan técnico)