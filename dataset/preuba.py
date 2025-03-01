from pathlib import Path

dataset_path = Path("dataset/images/train")
print(f"El archivo existe: {dataset_path.exists()}")
print(f"Ruta absoluta: {dataset_path.resolve()}")

# # Verificar si no hay imagenes dañadas
# import os
# from PIL import Image

# valid_images_path = "C:/Users/jphoy/Desktop/helmet_detection/dataset/images/val"

# for filename in os.listdir(valid_images_path):
#     if filename.endswith(".jpg") or filename.endswith(".png"):
#         try:
#             img = Image.open(os.path.join(valid_images_path, filename))
#             img.verify()  # Verifica si la imagen está dañada
#         except Exception as e:
#             print(f"Imagen dañada: {filename} - Error: {e}")


# import os

# images_path = "C:/Users/jphoy/Desktop/helmet_detection/dataset/images/val"
# labels_path = "C:/Users/jphoy/Desktop/helmet_detection/dataset/yolo_annotations/val"

# for img in os.listdir(images_path):
#     txt_file = os.path.splitext(img)[0] + ".txt"
#     if not os.path.exists(os.path.join(labels_path, txt_file)):
#         print(f"⚠ Falta el archivo de etiquetas para: {img}")
