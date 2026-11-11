# Paso 1 de la calibración: hacer fotos del tablero de ajedrez.
# Teclas: 'f' guarda la foto, 'q' sale.
# Haz entre 15 y 25 fotos moviendo el tablero (cerca, lejos, inclinado, en las esquinas).

import os
import cv2
import config

os.makedirs(config.CARPETA_FOTOS, exist_ok=True)

cap = cv2.VideoCapture(config.CAMARA, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.ANCHO)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.ALTO)

n = len(os.listdir(config.CARPETA_FOTOS))

while True:
    ok, frame = cap.read()
    if not ok:
        print("La cámara no da imagen")
        break

    # Comprobamos si se ve el tablero (solo para ayudar a hacer buenas fotos)
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    encontrado, esquinas = cv2.findChessboardCorners(gris, config.TABLERO, cv2.CALIB_CB_FAST_CHECK)

    vista = frame.copy()
    if encontrado:
        cv2.drawChessboardCorners(vista, config.TABLERO, esquinas, encontrado)
    texto = f"Fotos: {n}  |  tablero: {'SI' if encontrado else 'no'}  |  f = guardar, q = salir"
    cv2.putText(vista, texto, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.imshow("Captura para calibrar", vista)

    tecla = cv2.waitKey(1) & 0xFF
    if tecla == ord('f') and encontrado:
        ruta = os.path.join(config.CARPETA_FOTOS, f"foto_{n:02d}.jpg")
        cv2.imwrite(ruta, frame)   # guardamos la imagen original, sin dibujos
        print("Guardada", ruta)
        n += 1
    elif tecla == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
