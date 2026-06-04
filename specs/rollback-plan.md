# Plan de Rollback — Dashboard de Rendimiento Académico

- **Entorno:** Local / Académico

## Ante corrupción de datos
1. Detener Streamlit (`Ctrl + C`).
2. Eliminar `backend/db.sqlite3`.
3. Ejecutar `python3 app/seeder.py` para regenerar datos sintéticos.
4. Reiniciar: `streamlit run app/main.py`.

## Ante fallo de código
1. Ejecutar `git diff` para identificar cambios.
2. Revertir con `git checkout -- backend/` o `git stash`.
3. Re-ejecutar los tests: `python3 -m pytest backend/tests/ -v`.