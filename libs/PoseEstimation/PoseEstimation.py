import os
from ultralytics import YOLO


POSE_MODEL_PATH = "libs/PoseEstimation/models/yolov8n-pose.pt"


class PoseEstimation:

    def __init__(self):
        assert os.path.exists(POSE_MODEL_PATH), "File not found " + POSE_MODEL_PATH

        self.model = YOLO(POSE_MODEL_PATH)

    def estimate(self, frame):
        """
        Runs pose estimation on a single frame.
        Returns:
            annotated_frame (np.ndarray)
            keypoints (np.ndarray or None)
        """

        results = self.model(frame)

        keypoints = None

        # Validate detections
        if len(results) > 0 and results[0].keypoints is not None:

            if results[0].keypoints.data is not None:

                keypoints = (
                    results[0]
                    .keypoints
                    .data
                    .cpu()
                    .numpy()
                )

        return results[0], keypoints