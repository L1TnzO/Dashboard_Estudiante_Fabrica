# Plan de Pruebas — Dashboard de Rendimiento Académico

## Suite pytest — funciones de data_processor.py (SQLite in-memory)

| Test | Descripción | AC |
|---|---|---|
| `test_seed_populates_tables` | Seeder crea y pobla las 3 tablas | REQ-006 |
| `test_kpis_generales_sin_filtro` | Promedio entre 0-10, pct_aprobados 0-100 | AC-002, AC-006 |
| `test_kpis_generales_con_filtro` | KPIs cambian al filtrar por período | AC-005 |
| `test_promedio_por_materia` | DataFrame no vacío, columnas 'materia' y 'promedio' | AC-003 |
| `test_evolucion_temporal` | Serie por período, al menos 1 fila | REQ-003 |
| `test_estudiantes_en_riesgo_criterio` | Solo filas con nota<4.0 o asistencia<75 | AC-004, AC-007 |
| `test_estudiantes_en_riesgo_vacio` | Sin riesgo si todos aprueban y asisten | AC-007 |