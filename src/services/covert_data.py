import os
import xml.etree.ElementTree as ET

dataset_path = 'dataset'
annotations_path = os.path.join(dataset_path, 'annotations')
output_path = os.path.join(dataset_path, 'yolo_annotations')

os.makedirs(output_path, exist_ok=True)

class_mapping = {
    "helmet": 0,
    "head": 1,
    "face": 2,
    "head_w_helmet": 3,
    "person_w_helmet": 4,
    "person": 5
}

for split in ['train', 'val', 'test']:
    input_path = os.path.join(annotations_path, split)
    output_path_split = os.path.join(output_path, split)

    os.makedirs(output_path_split, exist_ok=True)

    for xml_file in os.listdir(input_path):
        if not xml_file.endswith('.xml'):
            continue
            
        xml_path = os.path.join(input_path, xml_file)
        txt_filename = xml_file.replace('.xml', '.txt')
        txt_path = os.path.join(output_path_split, txt_filename)

        tree = ET.parse(xml_path)
        root = tree.getroot()

        size = root.find('size')
        img_width = int(size.find('width').text)
        img_height = int(size.find('height').text)

        with open(txt_path, 'w') as f:
            for obj in root.findall('object'):
                class_name = obj.find('name').text
                if class_name not in class_mapping:
                    continue

                class_id = class_mapping[class_name]
                bndbox = obj.find('bndbox')
                xmin = int(bndbox.find('xmin').text)
                ymin = int(bndbox.find('ymin').text)
                xmax = int(bndbox.find('xmax').text)
                ymax = int(bndbox.find('ymax').text)

                x_center = (xmin + xmax) / 2.0 / img_width
                y_center = (ymin + ymax) / 2.0 / img_height
                width = (xmax - xmin) / img_width
                height = (ymax - ymin) / img_height

                f.write(f"{class_id} {x_center} {y_center} {width} {height}\n")

print("✅ Conversión completada. Archivos guardados en 'dataset_split/yolo_annotations'.")