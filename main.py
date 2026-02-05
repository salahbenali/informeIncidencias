from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")

incidencias = [
    {"id": 1, "texto": "El servidor no responde", "categoria": "red", "gravedad": 5, "estado": "abierta"},
    {"id": 2, "texto": "Monitor parpadea", "categoria": "hardware", "gravedad": 2, "estado": "resuelta"},
    {"id": 3, "texto": "No se puede instalar Office", "categoria": "software", "gravedad": 3, "estado": "abierta"},
    {"id": 4, "texto": "Impresora sin conexión", "categoria": "hardware", "gravedad": 3, "estado": "resuelta"},
    {"id": 5, "texto": "Página web muy lenta", "categoria": "red", "gravedad": 4, "estado": "abierta"},
    {"id": 6, "texto": "Error al abrir Excel", "categoria": "software", "gravedad": 2, "estado": "resuelta"},
    {"id": 7, "texto": "Cable de red roto", "categoria": "red", "gravedad": 4, "estado": "resuelta"},
    {"id": 8, "texto": "Teclado no funciona", "categoria": "hardware", "gravedad": 3, "estado": "abierta"},
]


@app.get("/")
def inicio():
    return RedirectResponse(url="/informe")


@app.get("/informe")
def informe(request: Request, categoria: str = None, min_gravedad: int = 1):
    
    incidencias_filtradas = []
    for inc in incidencias:
        if categoria and inc["categoria"] != categoria:
            continue
        if inc["gravedad"] < min_gravedad:
            continue
        incidencias_filtradas.append(inc)

    total = len(incidencias_filtradas)
    resueltas = sum(1 for inc in incidencias_filtradas if inc["estado"] == "resuelta")
    
    if total > 0:
        porcentaje = round((resueltas / total) * 100, 1)
    else:
        porcentaje = 0

    por_categoria = {
        "red": sum(1 for inc in incidencias_filtradas if inc["categoria"] == "red"),
        "hardware": sum(1 for inc in incidencias_filtradas if inc["categoria"] == "hardware"),
        "software": sum(1 for inc in incidencias_filtradas if inc["categoria"] == "software"),
    }
    
    abiertas = sum(1 for inc in incidencias_filtradas if inc["estado"] == "abierta")

    return templates.TemplateResponse(
        "informe.html",
        {
            "request": request,
            "incidencias": incidencias_filtradas,
            "resumen": {
                "total": total,
                "resueltas": resueltas,
                "porcentaje_resueltas": porcentaje
            },
            "filters": {
                "categoria": categoria,
                "min_gravedad": min_gravedad
            },
            "chart_data": {
                "cat_labels": ["Red", "Hardware", "Software"],
                "cat_values": [por_categoria["red"], por_categoria["hardware"], por_categoria["software"]],
                "estado_labels": ["Abiertas", "Resueltas"],
                "estado_values": [abiertas, resueltas]
            }
        },
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)