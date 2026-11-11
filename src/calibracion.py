# Paso 2 de la calibración (offline): calcula los parámetros de la cámara
# a partir de las fotos del tablero y los guarda en un archivo .npz

import glob
import cv2
import numpy as np
import config

# Coordenadas 3D de las esquinas del tablero (en mm, con z = 0)
puntos_tablero = np.zeros((config.TABLERO[0] * config.TABLERO[1], 3), np.float32)
puntos_tablero[:, :2] = np.mgrid[0:config.TABLERO[0], 0:config.TABLERO[1]].T.reshape(-1, 2)
puntos_tablero *= config.LADO_CASILLA_MM

puntos_3d = []   # puntos del mundo real
puntos_2d = []   # puntos en la imagen

criterio = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
fotos = sorted(glob.glob(config.CARPETA_FOTOS + "/*.jpg"))

for ruta in fotos:
    img = cv2.imread(ruta)
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    encontrado, esquinas = cv2.findChessboardCorners(gris, config.TABLERO, None)
    if encontrado:
        esquinas = cv2.cornerSubPix(gris, esquinas, (11, 11), (-1, -1), criterio)
        puntos_3d.append(puntos_tablero)
        puntos_2d.append(esquinas)
    else:
        print("No se encontró el tablero en", ruta)

print(f"Fotos válidas: {len(puntos_2d)} de {len(fotos)}")

tamano = gris.shape[::-1]
rms, K, dist, rvecs, tvecs = cv2.calibrateCamera(puntos_3d, puntos_2d, tamano, None, None)

print("\nError RMS de reproyección:", rms)
print("\nMatriz intrínseca K:\n", K)
print("\nCoeficientes de distorsión:\n", dist.ravel())

np.savez(config.ARCHIVO_CALIBRACION, K=K, dist=dist, rms=rms, tamano=tamano)
print("\nGuardado en", config.ARCHIVO_CALIBRACION)

# Imagen de ejemplo antes y después de corregir la distorsión (para el informe)
img = cv2.imread(fotos[0])
corregida = cv2.undistort(img, K, dist)
cv2.imwrite("data/ejemplo_corregida.jpg", np.hstack([img, corregida]))
