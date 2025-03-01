import os
import shutil
import random

# Se configuran las rutas de los directorios de las imágenes y las anotaciones
dataset_path = 'Safety_Helmet_Dataset'
images_path = os.path.join(dataset_path, 'images')
annotations_path = os.path.join(dataset_path, 'annotations')

output_path = 'dataset'
train_ratio, val_ratio, test_ratio = 0.7, 0.2, 0.1

if os.path.exists(output_path):
    shutil.rmtree(output_path)
# Se crean los directorios de salida
for split in ['train', 'val', 'test']:
    os.makedirs(os.path.join(output_path, 'images', split), exist_ok=True)
    os.makedirs(os.path.join(output_path, 'annotations', split), exist_ok=True)

images_files = [f for f in os.listdir(images_path) if f.endswith('.png')]
random.shuffle(images_files)

total = len(images_files)
train_count = int(total * train_ratio)
val_count = int(total * val_ratio)

splits ={
    'train': images_files[:train_count],
    'val': images_files[train_count:train_count + val_count],
    'test': images_files[train_count + val_count:]
}

for split, files in splits.items():
    for file in files:
        img_src = os.path.join(images_path, file)
        xml_src = os.path.join(annotations_path, file.replace(".png", ".xml"))

        img_dst = os.path.join(output_path, "images", split, file)
        xml_dst = os.path.join(output_path, "annotations", split, file.replace(".png", ".xml"))

        os.makedirs(os.path.dirname(img_dst), exist_ok=True)
        os.makedirs(os.path.dirname(xml_dst), exist_ok=True)

        if os.path.exists(img_src) and os.path.exists(xml_src):
            shutil.copy(img_src, img_dst)
            shutil.copy(xml_src, xml_dst)
        else:
            print(f"⚠️ Archivo faltante: {file} o su anotación.")

print("✅ División de datos completada.")
