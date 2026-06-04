# Reporte de Pruebas — Dashboard de Rendimiento Académico

- **Proyecto:** PROYECTO_UNO
- **Suite:** pytest (SQLite in-memory)
- **Entorno:** Sandbox aislado
- **Estado General:** **PASS**

## Tests ejecutados
| Test | Descripción | Estado |
|---|---|---|
| test_seed_populates_tables | 20 estudiantes × 6 materias × 3 períodos = 360 notas | PASS |
| test_kpis_generales_sin_filtro | KPIs dentro de rangos válidos | PASS |
| test_kpis_generales_con_filtro | KPIs cambian con filtro de período | PASS |
| test_promedio_por_materia | 6 materias con promedio 0-10 | PASS |
| test_evolucion_temporal | 3 períodos en la serie temporal | PASS |
| test_estudiantes_en_riesgo_criterio | Solo filas con nota<4.0 o asist<75 | PASS |
| test_estudiantes_en_riesgo_vacio | Sin riesgo cuando todos aprueban y asisten | PASS |

## Log de ejecución
### Capa 1 — Compilación sintáctica (py_compile)
- Archivos verificados: 6
- Estado: ✅ PASS
```
6 archivo(s) .py sin errores de sintaxis.
```

### Capa 2 — Instalación de dependencias (pip)
- Estado: ✅ PASS
```

```

### Capa 3 — Verificación de imports
- Estado: ✅ PASS
```
imports OK

```

### Capa 4 — pytest (SQLite in-memory)
```
============================= test session starts ==============================
platform linux -- Python 3.14.4, pytest-9.0.2, pluggy-1.6.0 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/enzo/University/Desarrollo_Agentes/29_may/Fabrica DASHBOARD
configfile: pytest.ini
plugins: cov-7.0.0, asyncio-1.3.0, anyio-4.12.1
asyncio: mode=Mode.STRICT, debug=False, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collecting ... collected 7 items

tests/test_data_processor.py::test_seed_populates_tables PASSED          [ 14%]
tests/test_data_processor.py::test_kpis_generales_sin_filtro PASSED      [ 28%]
tests/test_data_processor.py::test_kpis_generales_con_filtro PASSED      [ 42%]
tests/test_data_processor.py::test_promedio_por_materia PASSED           [ 57%]
tests/test_data_processor.py::test_evolucion_temporal PASSED             [ 71%]
tests/test_data_processor.py::test_estudiantes_en_riesgo_criterio PASSED [ 85%]
tests/test_data_processor.py::test_estudiantes_en_riesgo_vacio PASSED    [100%]

============================== 7 passed in 0.28s ===============================


```