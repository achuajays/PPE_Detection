import cv2
import config


def draw_status_display(frame, all_ppe_present, missing_ppe):
    """Draw status information on frame"""
    status_text = "SAFE" if all_ppe_present else "SAFETY VIOLATION"
    status_color = config.SAFE_COLOR if all_ppe_present else config.VIOLATION_COLOR

    # Draw status box
    cv2.rectangle(frame, (10, 10), (300, 80), config.STATUS_BOX_COLOR, -1)
    cv2.putText(frame, status_text, (15, 35), cv2.FONT_HERSHEY_SIMPLEX, 1.0, status_color, 2)

    # Draw missing PPE information
    if not all_ppe_present:
        missing_text = f"Missing: {', '.join(missing_ppe)}"
        cv2.putText(frame, missing_text, (15, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, config.VIOLATION_COLOR, 1)


def display_frame(frame):
    """Display frame with error handling"""
    try:
        cv2.imshow(config.WINDOW_NAME, frame)
    except cv2.error as e:
        print(f"Display error: {e}")
        print("Continuing without display...")


def check_exit_key():
    """Check if exit key is pressed"""
    key = cv2.waitKey(1) & 0xFF
    return key == config.EXIT_KEY


def cleanup_display():
    """Clean up display resources"""
    try:
        cv2.destroyAllWindows()
    except:
        pass