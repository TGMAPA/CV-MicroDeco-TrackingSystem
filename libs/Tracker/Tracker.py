import os, cv2
from ultralytics import YOLO


# Tracking System Function Library


TRACKING_MODEL_PATH = "models/best.pt"

class Tracker:
    def __init__(self):
        assert os.path.exists(TRACKING_MODEL_PATH), "File not found " + TRACKING_MODEL_PATH;

        self.model = YOLO(TRACKING_MODEL_PATH)

    def track(self, frame, persist = True):
        return self.model.track(frame, persist)