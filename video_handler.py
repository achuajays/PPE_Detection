import cv2
import config


def initialize_video_capture():
    """Initialize video capture with fallback to webcam"""
    cap = cv2.VideoCapture(config.VIDEO_PATH)

    # Check if video file exists and can be opened
    if not cap.isOpened():
        print(f"Error: Could not open video file '{config.VIDEO_PATH}'")
        print("Please check if:")
        print("1. The file 'video_to_check.mp4' exists in the current directory")
        print("2. The file is not corrupted")
        print("3. The file format is supported")

        # Try with webcam as fallback
        print("\nTrying webcam as fallback...")
        cap = cv2.VideoCapture(config.WEBCAM_INDEX)
        if not cap.isOpened():
            print("Error: Could not open webcam either")
            exit()
        else:
            print("Using webcam successfully")

    return cap


def validate_frame(frame):
    """Validate if frame is valid for processing"""
    if frame is None:
        print("Error: Could not read frame from video")
        print("Video might have ended or there's an issue with the source")
        return False

    if frame.size == 0:
        print("Error: Frame is empty")
        return False

    return True