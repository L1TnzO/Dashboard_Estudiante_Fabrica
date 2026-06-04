# Plan de Despliegue — Dashboard de Rendimiento Académico

- **Entorno:** Local / Académico
- **Método:** `streamlit run`

## Pasos
```bash
cd projects/PROYECTO_UNO/backend

# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Poblar la base de datos (solo primera vez)
python3 app/seeder.py

# 3. Lanzar el dashboard
streamlit run app/main.py
```

## Acceso
- URL: http://localhost:8501
- La DB se crea automáticamente en `backend/db.sqlite3`.
- El seeder también se ejecuta automáticamente si la DB está vacía.