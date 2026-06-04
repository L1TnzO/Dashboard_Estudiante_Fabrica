# Revisión de Seguridad — Dashboard de Rendimiento Académico

- **Proyecto:** PROYECTO_UNO

| Riesgo | Evaluación | Estado |
|---|---|---|
| Inyección SQL | Pandas + `pd.read_sql` con interpolación de WHERE controlado internamente. Los valores de los filtros provienen de `st.selectbox` (lista cerrada) — no de input libre del usuario. | PROTEGIDO |
| Exposición de datos sensibles | La DB contiene nombres y calificaciones de estudiantes. Sin autenticación en esta fase (monousuario local). En producción se requiere auth. | ACEPTABLE (local) |
| Secretos expuestos | Sin credenciales, tokens ni API keys en el código. | SEGURO |
| Integridad de datos | El seeder usa `random.seed(42)` — datos determinísticos, no modifica datos reales. | SEGURO |
| Disponibilidad | SQLite sin concurrencia alta — adecuado para uso local/académico. | ACEPTABLE |

## Hallazgos
- Cero secretos expuestos en el código fuente.
- Para producción: implementar autenticación Streamlit (`st.login`) o reverse proxy con auth.