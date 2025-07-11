# Configuration settings for PPE detection system

# Model configuration
MODEL_PATH = 'yolov8s_custom.pt'

# Video source configuration
VIDEO_PATH = 'video_to_check.mp4'
WEBCAM_INDEX = 0

# PPE requirements
REQUIRED_PPE = ['Helmet', 'Safety-Vest', 'Glass', 'helmet']

# Logging configuration
LOG_FILE = 'ppe_violations.json'

# Timing configuration
VIOLATION_COOLDOWN = 5  # seconds between beeps for same violation
STATUS_UPDATE_INTERVAL = 15  # seconds between status updates

# Sound configuration
BEEP_FREQUENCY = 1000  # Hz
BEEP_DURATION = 500    # milliseconds

# Display configuration
WINDOW_NAME = 'PPE Detection'
STATUS_BOX_COLOR = (0, 0, 0)  # Black background for status
SAFE_COLOR = (0, 255, 0)      # Green for safe status
VIOLATION_COLOR = (0, 0, 255)  # Red for violation
DETECTED_COLOR = (0, 255, 0)   # Green for detected PPE

# Exit key
EXIT_KEY = 27  # ESC key