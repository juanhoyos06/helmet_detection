from ultralytics import YOLO

model = YOLO("./runs/train/weights/best.pt")

results = model("./assets/prueba1.jpg", conf=0.3, iou=0.6, show=True, save=True)	
# from pathlib import Path

# dataset_path = Path("./runs/train/custom_exp/train/weights/best.pt")
# print(f"El archivo existe: {dataset_path.exists()}")
# print(f"Ruta absoluta: {dataset_path.resolve()}")