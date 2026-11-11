# SignaVoz

Proyecto final de **Visión por Ordenador I** (iMAT, ICAI · Universidad Pontificia Comillas, curso 2026/27).

**Autoras:** María de Yarza Lacarra y Macarena Gelado Martín.

SignaVoz permite que dos personas sentadas una al lado de la otra se comuniquen usando solo las manos. Cada letra se forma con el número de dedos levantados en cada mano (la mano izquierda elige la fila y la derecha la letra). La cámara reconoce las letras, las escribe en un chat en pantalla y el ordenador las lee en voz alta.

## Estructura

```
SignaVoz/
├── src/
│   ├── config.py            # parámetros (cámara, tablero, rutas)
│   ├── test.py              # prueba de la cámara (material de la asignatura)
│   ├── capturar_fotos.py    # fotos del tablero para calibrar
│   ├── calibracion.py       # calibración offline -> data/calibracion.npz
│   └── main.py              # programa principal
├── data/
│   └── calibracion/         # fotos del tablero
├── requirements.txt
└── README.md
```

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

Todos los comandos se ejecutan desde la carpeta raíz del proyecto.

1. Comprobar la cámara: `python src/test.py`
2. Hacer fotos del tablero (tecla `f` para guardar): `python src/capturar_fotos.py`
3. Calibrar la cámara: `python src/calibracion.py`
4. Ejecutar el sistema: `python src/main.py` (tecla `q` para salir)

## Estado

- [x] Lectura de vídeo y FPS en pantalla
- [x] Calibración de la cámara
- [ ] Sistema de seguridad: detección de patrones
- [ ] Sistema de seguridad: decodificador de secuencia
- [ ] Detección de manos y tracker
- [ ] Conteo de dedos y alfabeto
- [ ] Chat compartido y voz
- [ ] Ampliaciones
