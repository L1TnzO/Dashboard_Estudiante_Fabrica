# Aclaraciones — Dashboard de Rendimiento Académico

## Supuestos
- **DATOS:** La DB SQLite se crea y puebla automáticamente con el seeder si no existe. No se requiere carga manual.
- **APROBACIÓN:** Nota >= 4.0 (escala 0-10). Asistencia mínima: 75%.
- **FILTROS:** Al seleccionar "Todos" en cualquier filtro, no se aplica restricción.
- **EVOLUCIÓN TEMPORAL:** La evolución ignora los filtros de curso y carrera (siempre muestra todos los períodos) para una vista histórica completa.
- **SEEDER DETERMINÍSTICO:** `random.seed(42)` garantiza los mismos datos en cada ejecución.

## Decisiones de diseño
- `data_processor.py` contiene todas las funciones de consulta puras (reciben `conn` y `where`).
- `main.py` es el entry point de Streamlit (presentación únicamente).
- `seeder.py` es ejecutable como script independiente y como módulo.
- Tests usan `sqlite3.connect(":memory:")` — sin dependencia de archivos del sistema de archivos.