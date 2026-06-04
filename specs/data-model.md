# Modelo de Datos — Dashboard de Rendimiento Académico

## Tablas SQLite

### estudiantes
| Campo | Tipo | Restricciones |
|---|---|---|
| id | INTEGER | PK AUTOINCREMENT |
| nombre | TEXT | NOT NULL |
| curso | TEXT | NOT NULL (ej: 1A, 2B) |
| carrera | TEXT | NOT NULL |

### materias
| Campo | Tipo | Restricciones |
|---|---|---|
| id | INTEGER | PK AUTOINCREMENT |
| nombre | TEXT | NOT NULL |
| codigo | TEXT | UNIQUE NOT NULL |
| creditos | INTEGER | NOT NULL |

### notas
| Campo | Tipo | Restricciones |
|---|---|---|
| id | INTEGER | PK AUTOINCREMENT |
| estudiante_id | INTEGER | FK → estudiantes.id |
| materia_id | INTEGER | FK → materias.id |
| periodo | TEXT | NOT NULL (ej: 2024-1) |
| nota | REAL | NOT NULL, 0.0–10.0 |
| asistencia_pct | REAL | NOT NULL, 0.0–100.0 |

## Datos sintéticos (seeder)
- 20 estudiantes en cursos 1A, 1B, 2A, 2B, 3A — carreras Informática, Electrónica, Industrial
- 6 materias: MAT101, PRG101, FIS101, MAT201, PRG201, MAT301
- 3 períodos: 2024-1, 2024-2, 2025-1
- 360 registros de notas (20×6×3), random.seed(42)