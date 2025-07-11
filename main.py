from ultralytics import YOLO
import time
import threading
import config
from logger import initialize_log_file, log_violation, print_status_update
from audio import play_beep
from video_handler import initialize_video_capture, validate_frame
from ppe_detector import PPEDetector
from display import draw_status_display, display_frame, check_exit_key, cleanup_display


def main():
    # Initialize components
    model = YOLO(config.MODEL_PATH)
    cap = initialize_video_capture()
    initialize_log_file()
    detector = PPEDetector(model)

    # Initialize timing variables
    last_check_time = time.time()
    last_violation_time = 0

    # Print startup information
    print("Starting PPE detection...")
    print("Required PPE: Helmet, Safety Vest, Glasses")
    print("Violations will be logged to: ppe_violations.json")
    print("Press ESC to exit")

    try:
        while True:
            ret, frame = cap.read()

            if not ret or not validate_frame(frame):
                break

            # Detect PPE
            detection_results = detector.detect_ppe(frame)
            all_ppe_present = detection_results['all_ppe_present']

            # Handle violations
            if not all_ppe_present:
                missing_ppe = detector.get_missing_ppe(detection_results)

                current_time_for_beep = time.time()
                if current_time_for_beep - last_violation_time >= config.VIOLATION_COOLDOWN:
                    log_violation(missing_ppe)
                    threading.Thread(target=play_beep, daemon=True).start()
                    last_violation_time = current_time_for_beep

            # Update display
            missing_ppe = detector.get_missing_ppe(detection_results) if not all_ppe_present else []
            draw_status_display(frame, all_ppe_present, missing_ppe)
            display_frame(frame)

            # Periodic status updates
            current_time = time.time()
            if current_time - last_check_time >= config.STATUS_UPDATE_INTERVAL:
                last_check_time = current_time
                print_status_update(all_ppe_present)

            # Check for exit
            if check_exit_key():
                break

    except KeyboardInterrupt:
        print("\nStopping detection...")
    except Exception as e:
        print(f"Error occurred: {e}")

    # Clean up
    cap.release()
    cleanup_display()
    print("Program ended")


if __name__ == "__main__":
    main()