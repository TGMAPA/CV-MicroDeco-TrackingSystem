import os
import random
import shutil

# =========================
# CONFIGURACIÓN
# =========================
IMAGES_DIR = "../data/raw_justImages"
LABELS_DIR = "../data/raw_justImages_yolo_labels"
OUTPUT_DIR = "../data/dataset"

TRAIN_RATIO = 0.8  # 80% train, 20% val
RANDOM_SEED = 42

# =========================
# CREAR ESTRUCTURA
# =========================
def create_folders():
    paths = [
        os.path.join(OUTPUT_DIR, "images/train"),
        os.path.join(OUTPUT_DIR, "images/val"),
        os.path.join(OUTPUT_DIR, "labels/train"),
        os.path.join(OUTPUT_DIR, "labels/val"),
    ]

    for path in paths:
        os.makedirs(path, exist_ok=True)

# =========================
# OBTENER IMÁGENES VÁLIDAS
# =========================
def get_valid_images():
    images = []

    for file in os.listdir(IMAGES_DIR):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            label_file = file.rsplit(".", 1)[0] + ".txt"
            label_path = os.path.join(LABELS_DIR, label_file)

            if os.path.exists(label_path):
                images.append(file)
            else:
                print(f"⚠ No label encontrado para {file}")

    return images

# =========================
# SPLIT DATASET
# =========================
def split_dataset(images):
    random.seed(RANDOM_SEED)
    random.shuffle(images)

    split_index = int(len(images) * TRAIN_RATIO)

    train_images = images[:split_index]
    val_images = images[split_index:]

    return train_images, val_images

# =========================
# COPIAR ARCHIVOS
# =========================
def copy_files(image_list, subset):
    for image in image_list:
        label = image.rsplit(".", 1)[0] + ".txt"

        shutil.copy(
            os.path.join(IMAGES_DIR, image),
            os.path.join(OUTPUT_DIR, f"images/{subset}", image),
        )

        shutil.copy(
            os.path.join(LABELS_DIR, label),
            os.path.join(OUTPUT_DIR, f"labels/{subset}", label),
        )

# =========================
# MAIN
# =========================
def main():
    create_folders()

    images = get_valid_images()

    print(f"Total imágenes válidas: {len(images)}")

    train_images, val_images = split_dataset(images)

    print(f"Train: {len(train_images)}")
    print(f"Val: {len(val_images)}")

    copy_files(train_images, "train")
    copy_files(val_images, "val")

    print("✅ Dataset creado correctamente.")

if __name__ == "__main__":
    main()