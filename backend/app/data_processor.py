import pandas as pd


def get_kpis_generales(conn, where=""):
    """Retorna dict con promedio, total_estudiantes, pct_aprobados, en_riesgo."""
    query = f"""
        SELECT
            AVG(n.nota)                                                         AS promedio,
            COUNT(DISTINCT n.estudiante_id)                                     AS total_estudiantes,
            100.0 * SUM(CASE WHEN n.nota >= 4.0 THEN 1 ELSE 0 END) / COUNT(*) AS pct_aprobados,
            COUNT(DISTINCT CASE
                WHEN n.nota < 4.0 OR n.asistencia_pct < 75 THEN n.estudiante_id
            END)                                                                AS en_riesgo
        FROM notas n
        JOIN estudiantes e ON n.estudiante_id = e.id
        {where}
    """
    df = pd.read_sql(query, conn)
    return {
        "promedio":           round(float(df["promedio"].iloc[0] or 0.0), 2),
        "total_estudiantes":  int(df["total_estudiantes"].iloc[0] or 0),
        "pct_aprobados":      round(float(df["pct_aprobados"].iloc[0] or 0.0), 1),
        "en_riesgo":          int(df["en_riesgo"].iloc[0] or 0),
    }


def get_promedio_por_materia(conn, where=""):
    """DataFrame con columnas: materia, promedio, pct_aprobados."""
    query = f"""
        SELECT
            m.nombre                                                             AS materia,
            ROUND(AVG(n.nota), 2)                                               AS promedio,
            ROUND(100.0 * SUM(CASE WHEN n.nota >= 4.0 THEN 1 ELSE 0 END) / COUNT(*), 1) AS pct_aprobados
        FROM notas n
        JOIN materias    m ON n.materia_id    = m.id
        JOIN estudiantes e ON n.estudiante_id = e.id
        {where}
        GROUP BY m.id, m.nombre
        ORDER BY promedio DESC
    """
    return pd.read_sql(query, conn)


def get_evolucion_temporal(conn):
    """Serie temporal del promedio por período (sin filtros de curso/carrera)."""
    query = """
        SELECT periodo, ROUND(AVG(nota), 2) AS promedio
        FROM notas
        GROUP BY periodo
        ORDER BY periodo
    """
    return pd.read_sql(query, conn)


def get_estudiantes_en_riesgo(conn, where=""):
    """Estudiantes con nota < 4.0 O asistencia < 75%. Columna 'motivo' incluida."""
    query = f"""
        SELECT
            e.nombre          AS estudiante,
            e.curso,
            e.carrera,
            m.nombre          AS materia,
            n.periodo,
            ROUND(n.nota, 1)  AS nota,
            n.asistencia_pct  AS asistencia
        FROM notas n
        JOIN estudiantes e ON n.estudiante_id = e.id
        JOIN materias    m ON n.materia_id    = m.id
        {where}
    """
    df = pd.read_sql(query, conn)
    df_riesgo = df[(df["nota"] < 4.0) | (df["asistencia"] < 75)].copy()
    if df_riesgo.empty:
        return df_riesgo
    df_riesgo["motivo"] = df_riesgo.apply(
        lambda r: "Nota baja" if r["nota"] < 4.0 else "Asistencia baja", axis=1
    )
    return df_riesgo.sort_values("nota").reset_index(drop=True)
