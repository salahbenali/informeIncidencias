# Informe de Incidencias - FastAPI + Jinja2

Aplicación web para gestionar incidencias usando Python.

### main.py
- Importa FastAPI y Jinja2
- Define una lista de incidencias con: id, texto, categoria, gravedad, estado
- Ruta `/informe` que filtra por categoría y gravedad mínima
- Calcula totales y datos para los gráficos

### templates/base.html
- Plantilla base con el diseño general
- Incluye Chart.js para los gráficos
- Tiene bloques: titulo, header, contenido, scripts

### templates/informe.html
- Hereda de base.html
- Muestra 3 cajas con: Total, Resueltas, Porcentaje
- Formulario de filtros (categoría y gravedad)
- Tabla con las incidencias
- 2 gráficos: por categoría y por estado

## Cómo ejecutar

Dándole al play O ejecutando
uvicorn main:app --reload

## Captura

