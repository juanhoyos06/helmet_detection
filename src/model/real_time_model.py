import cv2
from ultralytics import YOLO

# Cargar el modelo entrenado
model = YOLO("./runs/train/custom_exp/train/weights/best.pt")

# Capturar video desde la cámara (0 = cámara principal)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Leer un frame de la cámara
    ret, frame = cap.read()
    if not ret:
        break

    # Hacer predicciones con el modelo
    results = model.predict(frame, conf=0.6, show=False, iou=0.5)

    # Dibujar los resultados en la imagen
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Coordenadas de la caja
            conf = box.conf[0].item()  # Confianza de la predicción
            cls = int(box.cls[0])  # Clase detectada
            label = f"{model.names[cls]}: {conf:.2f}"

            # Dibujar la caja y la etiqueta
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Mostrar el frame con las detecciones
    cv2.imshow("YOLO Webcam", frame)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
