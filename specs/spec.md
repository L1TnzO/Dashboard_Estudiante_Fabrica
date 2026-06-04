# Especificación SDD — Dashboard de Rendimiento Académico

## 1. Identificación
- **Nombre:** Dashboard de Rendimiento Académico
- **Dueño:** PO de Fábrica (Usuario)
- **Fecha:** 2026-05-30
- **ID:** PROYECTO_UNO
- **Estado:** `spec_validated`

## 2. Objetivo
- **Problema:** Los equipos docentes no tienen visibilidad rápida del rendimiento colectivo de sus estudiantes: promedios por materia, evolución temporal, y alumnos en riesgo de reprobar.
- **Para quién:** Coordinadores académicos, tutores, directores de carrera.
- **Resultado esperado:** Dashboard interactivo Streamlit que centraliza métricas académicas con filtros dinámicos, gráficos y alertas visuales.

## 3. Usuarios y roles
| Rol | Puede hacer | Restricciones |
|---|---|---|
| Coordinador Académico | Ver todos los dashboards, filtrar por período/curso/carrera | Sin edición de datos desde el dashboard |
| Tutor | Ver dashboard filtrado por su curso | Misma restricción |

## 4. Funcionalidades principales
| Funcionalidad | Descripción |
|---|---|
| KPIs Generales | Promedio general, total estudiantes, % aprobados, cantidad en riesgo |
| Análisis por Materia | Promedio y % aprobados por materia (gráfico de barras) |
| Evolución Temporal | Tendencia del promedio por período académico (gráfico de línea) |
| Alumnos en Riesgo | Tabla con estudiantes con nota < 4.0 o asistencia < 75% |
| Filtros Dinámicos | Período, Curso, Carrera (sidebar) — todos los gráficos reaccionan |

## 5. Requisitos funcionales
- **REQ-001 (KPIs):** Calcular promedio general, total estudiantes activos, % aprobados y cantidad en riesgo según filtros.
- **REQ-002 (Por Materia):** Promedio y % aprobados por materia, ordenados descendentemente.
- **REQ-003 (Evolución):** Serie temporal del promedio por período, independiente de filtros de curso/carrera.
- **REQ-004 (Riesgo):** Listar estudiantes con nota < 4.0 O asistencia < 75%, con motivo visible.
- **REQ-005 (Filtros):** Sidebar con selectboxes para período, curso y carrera. Opción "Todos".
- **REQ-006 (Datos Sintéticos):** Seeder automático con 20 estudiantes × 6 materias × 3 períodos.

## 6. Requisitos no funcionales
- **Rendimiento:** Carga inicial < 3 seg con datos sintéticos.
- **Usabilidad:** Interfaz limpia, tabs claros, métricas destacadas con `st.metric`.
- **Reproducibilidad:** Seeder usa `random.seed(42)` para resultados determinísticos.
- **Tests:** Funciones de procesamiento de datos 100% testeables con pytest + SQLite in-memory.

## 7. Modelo de datos
| Tabla | Campos clave |
|---|---|
| `estudiantes` | id, nombre, curso, carrera |
| `materias` | id, nombre, codigo, creditos |
| `notas` | id, estudiante_id(FK), materia_id(FK), periodo, nota(0-10), asistencia_pct(0-100) |

## 8. Stack
- Python 3, Streamlit, Pandas, SQLite (sqlite3), pytest, httpx (no aplica para Streamlit)

## 9. Criterios de aceptación
- **AC-001:** Dashboard carga sin errores con datos sintéticos.
- **AC-002:** Los 4 KPIs se muestran correctamente con datos reales de la DB.
- **AC-003:** El gráfico de barras por materia refleja los promedios correctos.
- **AC-004:** La tabla de riesgo solo muestra estudiantes con nota < 4.0 o asistencia < 75%.
- **AC-005:** Los filtros modifican los KPIs y gráficos reactivamente.
- **AC-006:** `get_kpis_generales()` retorna dict con claves: promedio, total_estudiantes, pct_aprobados, en_riesgo.
- **AC-007:** `get_estudiantes_en_riesgo()` solo devuelve filas que cumplen el criterio de riesgo.

## 10. Pruebas esperadas
- pytest con SQLite in-memory fixture (sin dependencia de archivo externo).
- Tests para: seed, get_kpis_generales, get_promedio_por_materia, get_evolucion_temporal, get_estudiantes_en_riesgo.

## 11. Fuera de alcance
- Edición de notas desde el dashboard, autenticación, exportación a PDF, integración con LMS externo.