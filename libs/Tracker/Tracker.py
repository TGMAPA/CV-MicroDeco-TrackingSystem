import os
from ultralytics import YOLO


# Tracking System Function Library


TRACKING_MODEL_PATH = "libs/Tracker/models/best.pt"


class Tracker:
    def __init__(self):
        assert os.path.exists(TRACKING_MODEL_PATH), "File not found " + TRACKING_MODEL_PATH;

        self.model = YOLO(TRACKING_MODEL_PATH)

    # Run YOLO26 tracking on the frame, persisting tracks between frames
    def track(self, frame, persist = True):
        return self.model.track(frame, persist)