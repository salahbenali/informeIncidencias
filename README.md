# Informe de Incidencias - FastAPI + Jinja2

Aplicación web para gestionar incidencias usando Python.

## Archivos

### main.py
- Importa FastAPI y Jinja2
- Define una lista de incidencias con: id, texto, categoria, gravedad, estado
- Ruta `/informe` que filtra por categoría y gravedad mínima
- Calcula totales y datos para los gráficos

### templates/base.html
- Plantilla base con el diseño general
- Incluye Chart.js para los gráficos
- Define los estilos CSS
- Tiene bloques: titulo, header, contenido, scripts

### templates/informe.html
- Hereda de base.html
- Muestra 3 cajas con: Total, Resueltas, Porcentaje
- Formulario de filtros (categoría y gravedad)
- Tabla con las incidencias
- 2 gráficos: por categoría (barras) y por estado (circular)

## Modificación obligatoria
Se añadió un segundo gráfico (por estado) que muestra las incidencias abiertas vs resueltas.

## Cómo ejecutar
```
uvicorn main:app --reload
```
Abrir en el navegador: http://localhost:8000/informe

## Captura
*(Añadir aquí captura con filtro aplicado)*
