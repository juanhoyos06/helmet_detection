from ultralytics import YOLO

model = YOLO("yolov8n.pt")
output_dir = "./runs/train"

model.train(
    data="./dataset/data.yaml",
    epochs=20, 
    batch=4, 
    imgsz=320, 
    device="cpu",
    project=output_dir
)

print(f"✅ Entrenamiento completado. Modelo guardado en 'runs/train'.")

# Codigo para saber si la ruta existe y obtener la ruta absoluta
# from pathlib import Path

# dataset_path = Path("./runs/train")
# print(f"El archivo existe: {dataset_path.exists()}")
# print(f"Ruta absoluta: {dataset_path.resolve()}")
