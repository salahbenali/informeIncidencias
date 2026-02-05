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
```
uvicorn main:app --reload
```

## Captura
- 
<img width="1914" height="977" alt="1" src="https://github.com/user-attachments/assets/14cc8a00-6435-40d0-b3c8-4e86eca0af17" />

- 
<img width="1904" height="954" alt="2" src="https://github.com/user-attachments/assets/7747060d-a7bb-4fb0-b7ab-5b1c336756e4" />


