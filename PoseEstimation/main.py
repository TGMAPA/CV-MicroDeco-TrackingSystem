from ultralytics import YOLO
import cv2 
import numpy as np


# Load the YOLOv8 pose model
model = YOLO('yolov8n-pose.pt')  # Using the "nano" version for speed

# Open the default camera
cam = cv2.VideoCapture(0)

def process_frame(frame):
    # Process a video frame
    results = model(frame, show=False)

    # Extract keypoints if a person is detected
    if len(results) > 0 and hasattr(results[0], 'keypoints'):
        keypoints = results[0].keypoints.data.cpu().numpy()[0]

    #print("Restults..")
    #print(results)

    # Draw the skeletal overlay
    annotated_frame = results[0].plot()

    return annotated_frame

while True:
    ret, frame = cam.read()

    annotated_frame = process_frame(frame)

    # Display the captured frame
    cv2.imshow('Camera', frame)

    # Add movement state text in the upper right corner


    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()
#out.release()
cv2.destroyAllWindows()