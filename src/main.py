# Programa principal de SignaVoz.
# De momento: lee la cámara, corrige la distorsión, pone la imagen en espejo,
# la divide en dos mitades (persona A y persona B) y muestra los FPS.

import time
import cv2
import numpy as np
import config

# Cargamos la calibración hecha offline
datos = np.load(config.ARCHIVO_CALIBRACION)
K, dist = datos["K"], datos["dist"]

cap = cv2.VideoCapture(config.CAMARA, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.ANCHO)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.ALTO)

ok, frame = cap.read()
alto, ancho = frame.shape[:2]

# Los mapas de corrección se calculan una sola vez (así va más rápido que undistort en cada frame)
mapa_x, mapa_y = cv2.initUndistortRectifyMap(K, dist, None, K, (ancho, alto), cv2.CV_16SC2)

fps = 0
t_anterior = time.time()

while True:
    ok, frame = cap.read()
    if not ok:
        print("La cámara no da imagen")
        break

    frame = cv2.remap(frame, mapa_x, mapa_y, cv2.INTER_LINEAR)  # quitar distorsión
    frame = cv2.flip(frame, 1)                                   # vista espejo

    mitad = ancho // 2
    persona_a = frame[:, :mitad]
    persona_b = frame[:, mitad:]
    # Aquí irá el procesado de cada mitad (seguridad, manos, letras...)

    # FPS suavizados para que el número no baile
    t_actual = time.time()
    fps = 0.9 * fps + 0.1 * (1 / (t_actual - t_anterior))
    t_anterior = t_actual

    cv2.line(frame, (mitad, 0), (mitad, alto), (255, 255, 255), 2)
    cv2.putText(frame, "Persona A", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 165, 255), 2)
    cv2.putText(frame, "Persona B", (mitad + 20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 150, 50), 2)
    cv2.putText(frame, f"FPS: {fps:.1f}", (ancho - 180, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("SignaVoz", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
