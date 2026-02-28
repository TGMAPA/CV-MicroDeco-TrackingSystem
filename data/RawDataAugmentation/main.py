import os
import subprocess

INPUT_FOLDER = "../data/raw/videos"
OUTPUT_FOLDER = "../data/raw_justImages"
FPS = 3 

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in os.listdir(INPUT_FOLDER):
    file_path = os.path.join(INPUT_FOLDER, file)

    if file.lower().endswith(".mp4"):
        video_name = os.path.splitext(file)[0]
        output_path = os.path.join(OUTPUT_FOLDER, video_name)

        cmd = [
            "ffmpeg",
            "-i", file_path,
            "-r", str(FPS),
            os.path.join(OUTPUT_FOLDER, "frame_%04d.jpg")
        ]

        print(f"Procesando {file}...")
        subprocess.run(cmd)

print("Proceso terminado.")