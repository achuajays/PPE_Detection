import winsound  # For Windows beep sound
import config

def play_beep():
    """Play beep sound for violation"""
    try:
        # Windows beep sound
        winsound.Beep(config.BEEP_FREQUENCY, config.BEEP_DURATION)
    except:
        try:
            # Alternative beep for other systems
            print('\a')  # ASCII bell character
        except:
            print("🔊 BEEP! (Sound not available)")