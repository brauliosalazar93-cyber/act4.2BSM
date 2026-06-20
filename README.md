# Actividad 4.2 — Visualización de Datos X-Y con Flask

**Alumno:** Braulio Salazar  
**Asignatura:** Desarrollo de Software para Hardware  
**Evaluación:** Sumativa 4.2

---

## Descripción

Aplicación web desarrollada con **Flask** y **Jinja2** que recibe datos X e Y desde una aplicación móvil (APK) a través de un socket TCP, y los visualiza en tiempo real en el navegador mediante tres vistas distintas accesibles desde una página de inicio.

---

## Tecnologías utilizadas

- Python 3 + Flask
- HTML + CSS (dentro de `<head>`, usando únicamente selectores `id`)
- Jinja2
- Socket TCP

> No se utiliza JavaScript en ninguna vista.

---

## Estructura del proyecto

```
actividad_4.2_jesa/
├── app.py
├── README.md
├── capturas/
│   ├── archivos-base.png
│   └── vista-base.png
└── templates/
    ├── index.html   → Página de inicio
    ├── page1.html   → Vista Matriz 4×4
    ├── page2.html   → Vista Brújula
    └── page3.html   → Vista Barras
```

---

## Vistas disponibles

### `/` — Página de inicio
Menú principal con tarjetas de acceso a cada una de las tres vistas de visualización.

### `/page1` — Matriz 4×4
Grilla de 16 celdas (4 filas × 4 columnas). El eje X determina la columna y el eje Y determina la fila. La celda activa se ilumina en verde.

### `/page2` — Brújula
Vista 3×3 con puntos cardinales: N, S, E, O, NE, NO, SE, SO y Centro. Representa la dirección del movimiento del sensor. La celda activa se ilumina en azul.

### `/page3` — Barras
Dos barras segmentadas en 4 niveles: una horizontal para el eje X y una vertical para el eje Y. El segmento activo se ilumina en naranja.

Todas las vistas incluyen navegación hacia las demás páginas y se actualizan automáticamente cada 2 segundos.

---

## Requisitos

- Python 3 con Flask instalado
- Red local compartida entre el computador y el dispositivo móvil
- Aplicación APK para enviar datos X-Y (disponible con el docente)

---

## Ejecución

```bash
python3 app.py
```

Luego acceder en el navegador a:

```
http://127.0.0.1:5000
```

---

## Capturas

### Estructura de archivos

![Estructura de los archivos](capturas/archivos-base.png)

### Vista base en el navegador

![Vista HTML](capturas/vista-base.png)
