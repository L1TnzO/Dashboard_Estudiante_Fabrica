# Especificación del Sistema: Dashboard de Rendimiento Académico

## 1. Nombre del sistema

**Dashboard de Rendimiento Académico**

---

## 2. Objetivo general

Desarrollar un dashboard interactivo con Python y Streamlit que permita a coordinadores académicos y tutores visualizar métricas consolidadas de rendimiento estudiantil de forma rápida, clara y filtrable.

El sistema debe:

- Mostrar KPIs clave: promedio general, total de estudiantes, porcentaje de aprobados, cantidad en riesgo.
- Analizar el rendimiento por materia con gráficos de barras.
- Mostrar la evolución histórica del promedio por período académico.
- Identificar y listar estudiantes en situación de riesgo académico.
- Permitir filtrar toda la información por período, curso y carrera.

---

## 3. Alcance

**Incluido:**

- Dashboard Streamlit con datos almacenados en SQLite.
- Módulo de procesamiento de datos con Pandas.
- Seeder automático con datos sintéticos (20 estudiantes, 6 materias, 3 períodos).
- Suite de pruebas con pytest y SQLite in-memory.
- Filtros dinámicos en sidebar.

**No incluido:**

- Edición de notas desde el dashboard.
- Autenticación multiusuario.
- Integración con sistemas externos (Moodle, Banner, etc.).
- Exportación a PDF o Excel.

---

## 4. Usuarios

| Rol | Descripción |
|---|---|
| Coordinador Académico | Necesita visión global del rendimiento por período, materia y carrera. |
| Tutor de Curso | Necesita identificar rápidamente estudiantes en riesgo de su curso. |

---

## 5. Funcionalidades principales

### 5.1 KPIs Generales (Tab: Resumen)

- Promedio general de notas (escala 0–10).
- Total de estudiantes con notas registradas.
- Porcentaje de aprobados (nota ≥ 4.0).
- Cantidad de estudiantes en riesgo académico.
- Gráfico de barras: aprobados vs. reprobados.

### 5.2 Análisis por Materia (Tab: Por Materia)

- Gráfico de barras con el promedio de cada materia.
- Tabla detallada con promedio y % de aprobados por materia, ordenados descendentemente.

### 5.3 Evolución Temporal (Tab: Evolución)

- Gráfico de línea con el promedio general por período académico.
- No se filtra por curso ni carrera — vista histórica global.

### 5.4 Alumnos en Riesgo (Tab: Riesgo)

- Tabla con todos los registros donde nota < 4.0 O asistencia < 75%.
- Columna "motivo": "Nota baja" o "Asistencia baja".
- Si no hay alumnos en riesgo para los filtros activos: mensaje de éxito verde.

### 5.5 Filtros Dinámicos (Sidebar)

- Selectbox de Período: lista de períodos disponibles + opción "Todos".
- Selectbox de Curso: lista de cursos + "Todos".
- Selectbox de Carrera: lista de carreras + "Todos".
- Al cambiar cualquier filtro: todos los tabs (excepto Evolución) se actualizan.

---

## 6. Modelo de datos

### Tabla: estudiantes
| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER PK | Auto-incremental |
| nombre | TEXT | Nombre completo |
| curso | TEXT | Ej: 1A, 2B, 3A |
| carrera | TEXT | Ej: Informática, Electrónica |

### Tabla: materias
| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER PK | Auto-incremental |
| nombre | TEXT | Nombre de la materia |
| codigo | TEXT UNIQUE | Ej: MAT101, PRG201 |
| creditos | INTEGER | Créditos académicos |

### Tabla: notas
| Campo | Tipo | Descripción |
|---|---|---|
| id | INTEGER PK | Auto-incremental |
| estudiante_id | INTEGER FK | Referencia a estudiantes |
| materia_id | INTEGER FK | Referencia a materias |
| periodo | TEXT | Ej: 2024-1, 2024-2 |
| nota | REAL | 0.0 a 10.0 |
| asistencia_pct | REAL | 0.0 a 100.0 |

---

## 7. Datos sintéticos (seeder)

- **20 estudiantes** en cursos 1A, 1B, 2A, 2B, 3A — carreras Informática, Electrónica, Industrial.
- **6 materias:** Matemáticas I, Programación I, Física I, Álgebra Lineal, Estructuras de Datos, Estadística.
- **3 períodos:** 2024-1, 2024-2, 2025-1.
- Total: 360 registros de notas.
- Reproducibilidad: `random.seed(42)`.

---

## 8. Stack tecnológico

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3 |
| Dashboard | Streamlit >= 1.32.0 |
| Datos | Pandas >= 2.0.0 |
| Base de datos | SQLite (stdlib) |
| Tests | pytest >= 7.0.0 |

---

## 9. Criterios de aceptación

| ID | Criterio |
|---|---|
| CA-001 | El dashboard carga en < 3 segundos con datos sintéticos. |
| CA-002 | Los 4 KPIs muestran valores correctos para el conjunto completo de datos. |
| CA-003 | El gráfico por materia refleja los promedios reales de la DB. |
| CA-004 | La tabla de riesgo solo contiene estudiantes con nota < 4.0 o asistencia < 75%. |
| CA-005 | Al cambiar un filtro, los KPIs y gráficos se actualizan correctamente. |
| CA-006 | Los 7 tests de pytest pasan con SQLite in-memory. |

---

## 10. Checklist de pruebas

```
[ ] test_seed_populates_tables          → 20 estudiantes, 6 materias, 360 notas
[ ] test_kpis_generales_sin_filtro      → promedio 0-10, pct_aprobados 0-100
[ ] test_kpis_generales_con_filtro      → KPIs cambian al filtrar por período
[ ] test_promedio_por_materia           → 6 filas, columnas materia y promedio
[ ] test_evolucion_temporal             → 3 períodos en la serie
[ ] test_estudiantes_en_riesgo_criterio → solo filas con nota<4 o asist<75
[ ] test_estudiantes_en_riesgo_vacio    → vacío cuando todos aprueban y asisten
```
