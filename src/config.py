# Parámetros comunes del proyecto

# Cámara
CAMARA = 0          # si la webcam no se abre, prueba con 1
ANCHO = 1280
ALTO = 720

# Tablero de ajedrez: número de esquinas INTERIORES (no de casillas)
# Un tablero de 10 x 7 casillas tiene 9 x 6 esquinas interiores
TABLERO = (9, 6)
LADO_CASILLA_MM = 25  # mide una casilla del tablero impreso con una regla

# Rutas
CARPETA_FOTOS = "data/calibracion"
ARCHIVO_CALIBRACION = "data/calibracion.npz"
