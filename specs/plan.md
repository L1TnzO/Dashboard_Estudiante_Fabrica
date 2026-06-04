# Plan Técnico — Dashboard de Rendimiento Académico

## 1. Arquitectura
Aplicación monolítica Streamlit — sin API HTTP separada:
```
backend/
  app/
    main.py           ← Streamlit app (presentación)
    data_processor.py ← Funciones Pandas/SQL (lógica de datos)
    seeder.py         ← Creación y poblado de DB sintética
  tests/
    test_data_processor.py ← pytest con SQLite in-memory
  db.sqlite3          ← Auto-creada en ejecución
  requirements.txt
```

## 2. Módulos
| Módulo | Responsabilidad |
|---|---|
| `main.py` | UI Streamlit: sidebar de filtros, tabs, métricas, gráficos |
| `data_processor.py` | Funciones puras SQL+Pandas: KPIs, promedios, riesgo |
| `seeder.py` | DDL + INSERT de datos sintéticos determinísticos |

## 3. Dependencias aprobadas
```
streamlit>=1.32.0
pandas>=2.0.0
pytest>=7.0.0
```
*(sqlite3 es parte de la biblioteca estándar de Python)*

## 4. Ejecución
```bash
cd backend
python3 app/seeder.py          # Solo si la DB no existe
streamlit run app/main.py      # Inicia el dashboard en http://localhost:8501
```