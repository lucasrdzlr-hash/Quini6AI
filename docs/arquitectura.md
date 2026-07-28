# Quini6AI - Arquitectura

## Objetivo

Quini6AI es una plataforma modular para análisis estadístico,
gestión del historial de sorteos y generación inteligente
de jugadas del Quini 6.

---

## Arquitectura

Interfaz
    │
    ▼
Servicios
    │
    ▼
Motor IA
    │
    ▼
Base SQLite

---

## Capas

Interfaz

- CLI
- Futuro formulario gráfico
- Futura interfaz web

Servicios

- Ranking
- Generación
- Evaluación
- Historial
- Estadísticas
- Backtesting

Motor

- FeatureEngine
- ScoreEngine
- Generadores
- Evaluadores
- Plugins

Persistencia

SQLite

Exportadores

Excel
CSV
JSON