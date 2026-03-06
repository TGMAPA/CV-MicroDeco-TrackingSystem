# tracking system exec


import cv2
from Camera import Camera
from libs.Tracker.Tracker import Tracker
from libs.PoseEstimation.PoseEstimation import PoseEstimation
from libs.Detector.Detector import Detector


# tracker category map
tracker_category_map = {
    0 : "hand",
    1 : "ok_board",
    2 : "no_ok_board"
}


def exec_training_system(
        source = "data/raw/raw_resources/secondvisit/IMG_9054.MOV", # "data/raw/videos/VIDEO-2026-02-18-16-32-46.mp4"
        window_title = "TrackingSystem",
        log = True
):
    print("[Starting Tracking System]")

    # Initialize video capture
    cam = Camera(source)

    # Object Tracker
    tracker = Tracker()

    # Object PoseEstimator
    pose_estimator = PoseEstimation()

    # Object Detector
    detector = Detector()

    # Main loop
    while True:
        # Read a frame from the video source
        success, frame = cam.getFrame()

        if success:
            # -- Tracker Analysis
            # Execute tracking
            tracker_results = list(tracker.track(frame))[0]

            # -- PoseEstimator Analysis
            poseEstimator_results, keypoints = pose_estimator.estimate(frame)
            
            # -- Final Frame
            # Visualize the tracker_results on the frame
            tracker_annotated_frame = tracker_results.plot()
            annotated_frame = poseEstimator_results.plot()

            # Create final annotated frame masking 
            mask = tracker_annotated_frame != frame
            annotated_frame[mask] = tracker_annotated_frame[mask]


            # --- Geometric logic and detection
            # Extract boxes centroids for every tracker detected category [hand, ok_board, no_ok_board]           
            boxes_cords_and_categories = {}
            for box, clas in zip(tracker_results.boxes.xyxy, tracker_results.boxes.cls):
                if tracker_category_map[int(clas)] not in boxes_cords_and_categories.keys():
                    boxes_cords_and_categories[tracker_category_map[int(clas)]] = [box]
                else:
                    boxes_cords_and_categories[tracker_category_map[int(clas)]].append(box)

            
            # Hand naer ok_board detector
            detector.hands_near_ok_board(
                annotated_frame,
                keypoints,
                boxes_cords_and_categories,
                confidence_threshold=0.3,
                distance_threshold=200,
                log= log    
            )

            # -- Window configuraStion and condition for loop breaking
            cv2.imshow(window_title, annotated_frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cam.kill()
    cv2.destroyAllWindows()

    print("[Closing TrackingSystem]")
