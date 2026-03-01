import cv2
from libs.utils import get_box_centroid, are_two_points_near


class Detector:
    def __init__(self):
        pass

    # Hands near Ok board detection
    def hands_near_ok_board(
            self,
            frame,
            poseEstimator_keypoints,
            tracker_boxes_cords_and_categories_dict,
            # Wrist detection confidence and distance with board thresholds
            confidence_threshold = 0.30,
            distance_threshold = 80,
            log = False
        ):

        # Initialize
        hands_near_ok_board_detected = False

        # Validate inputs and ok_board objects detected 
        if poseEstimator_keypoints is None:
            return frame, False

        if "ok_board" not in tracker_boxes_cords_and_categories_dict:
            return frame, False

        try: 
            # Get wrists (x, y, confidence)
            left_wrist  = poseEstimator_keypoints[0][9]
            right_wrist = poseEstimator_keypoints[0][10]
        except: 
            return frame, False 

        # Calculate ok_board centroids
        all_ok_board_centroid = [get_box_centroid(detected_ok_board_box) for detected_ok_board_box in tracker_boxes_cords_and_categories_dict["ok_board"]]

        # Check left wrist
        if left_wrist[2] > confidence_threshold:
            for ok_board_centroid in all_ok_board_centroid:
                if are_two_points_near(
                        left_wrist[:2],
                        ok_board_centroid,
                        distance_threshold):

                    hands_near_ok_board_detected = True

                    if log: print("-- Hand Near OK_BOARD: ", hands_near_ok_board_detected)

                    # Draw detected movement
                    cv2.circle(
                        frame,
                        (int(left_wrist[0]), int(left_wrist[1])),
                        15,
                        (0, 0, 255), 
                        -1
                    )

        # Check right wrist
        if right_wrist[2] > confidence_threshold:
            for ok_board_centroid in all_ok_board_centroid:
                if are_two_points_near(
                        right_wrist[:2],
                        ok_board_centroid,
                        distance_threshold):

                    hands_near_ok_board_detected = True

                    if log: print("-- Hand Near OK_BOARD: ", hands_near_ok_board_detected)

                    # Draw detected movement
                    cv2.circle(
                        frame,
                        (int(right_wrist[0]), int(right_wrist[1])),
                        15,
                        (0, 0, 255),
                        -1
                    )

        return frame, hands_near_ok_board_detected