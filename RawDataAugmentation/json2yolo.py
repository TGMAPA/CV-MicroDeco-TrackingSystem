import os
import json
import cv2

IMAGES_DIR = "../data/raw_justImages"
JSON_DIR = "../data/raw_justImages_labels"
OUTPUT_LABELS_DIR = "../data/raw_justImages_yolo_labels"

os.makedirs(OUTPUT_LABELS_DIR, exist_ok=True)

CLASS_MAP = {
    "hand": 0,
    "ok_board": 1,
    "no_ok_board": 2
}

for json_file in os.listdir(JSON_DIR):
    if not json_file.endswith(".json"):
        continue

    json_path = os.path.join(JSON_DIR, json_file)

    with open(json_path, "r") as f:
        data = json.load(f)

    for item in data:
        image_name = item["image"]
        image_path = os.path.join(IMAGES_DIR, image_name)

        if not os.path.exists(image_path):
            print(f"No existe imagen {image_name}")
            continue

        img = cv2.imread(image_path)
        h, w, _ = img.shape

        label_lines = []

        for ann in item["annotations"]:
            label_name = ann["label"]
            coords = ann["coordinates"]

            if label_name not in CLASS_MAP:
                continue

            class_id = CLASS_MAP[label_name]

            x_center = coords["x"] / w
            y_center = coords["y"] / h
            width = coords["width"] / w
            height = coords["height"] / h

            line = f"{class_id} {x_center} {y_center} {width} {height}"
            label_lines.append(line)

        output_txt = os.path.join(
            OUTPUT_LABELS_DIR,
            image_name.replace(".jpg", ".txt")
        )

        with open(output_txt, "w") as f:
            f.write("\n".join(label_lines))

print("Conversión completada.")