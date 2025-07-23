from ultralytics import YOLO

model = YOLO("./runs/train/weights/best.pt")

results = model("./assets/image.png", conf=0.5, show=False, save=True)	
# from pathlib import Path

# dataset_path = Path("./runs/train/custom_exp/train/weights/best.pt")
# print(f"El archivo existe: {dataset_path.exists()}")
# print(f"Ruta absoluta: {dataset_path.resolve()}")