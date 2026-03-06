import os
import subprocess

INPUT_FOLDER = "../raw/raw_resources/secondvisit/videos"
OUTPUT_FOLDER = "../raw/raw_resources/secondvisit/just_Images_splitedVideos"
FPS = 3 

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

for file in os.listdir(INPUT_FOLDER):
    file_path = os.path.join(INPUT_FOLDER, file)

    if file.lower().endswith(".mov"):
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