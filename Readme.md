# PPE Detection System

A real-time Personal Protective Equipment (PPE) detection system using YOLO computer vision to monitor workplace safety compliance. The system automatically detects helmets, safety vests, and safety glasses, logging violations and providing audio alerts when PPE is missing.

## Features

- **Real-time Detection**: Monitors video feeds or webcam for PPE compliance
- **Multi-PPE Support**: Detects helmets, safety vests, and safety glasses
- **Violation Logging**: Automatic JSON logging of safety violations with timestamps
- **Audio Alerts**: Beep notifications when PPE violations are detected
- **Visual Interface**: Real-time display with bounding boxes and status indicators
- **Fallback Support**: Automatically switches to webcam if video file is unavailable
- **Modular Design**: Clean, organized code structure for easy maintenance

## Requirements

### Hardware
- Windows/Linux/Mac computer with webcam (optional)
- Minimum 4GB RAM recommended
- GPU recommended for better performance (optional)

### Software Dependencies
```
ultralytics
opencv-python
numpy
```

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ppe-detection-system
   ```

2. **Install required packages**
   ```bash
   pip install ultralytics opencv-python numpy
   ```

3. **Download or train your YOLO model**
   - Place your trained model file as `yolov8s_custom.pt` in the project directory
   - Or modify the `MODEL_PATH` in `config.py` to point to your model

4. **Prepare video source**
   - Place your video file as `video_to_check.mp4` in the project directory
   - Or modify the `VIDEO_PATH` in `config.py`
   - The system will automatically fallback to webcam if video file is not found

## Usage

### Basic Usage
```bash
python main.py
```

### Controls
- **ESC**: Exit the application
- **Ctrl+C**: Force stop the application

### Configuration
Edit `config.py` to customize:
- Model path and video source
- PPE requirements
- Logging settings
- Audio notification settings
- Display colors and timing

## File Structure

```
ppe-detection-system/
├── main.py                 # Main application entry point
├── config.py              # Configuration settings
├── logger.py              # Logging functions
├── audio.py               # Audio notification functions
├── video_handler.py       # Video capture handling
├── ppe_detector.py        # PPE detection logic
├── display.py             # Display and UI functions
├── yolov8s_custom.pt      # YOLO model file (user provided)
├── video_to_check.mp4     # Video file to analyze (user provided)
├── ppe_violations.json    # Violation log file (auto-generated)
└── README.md              # This file
```

## Configuration Options

### Model Settings
- `MODEL_PATH`: Path to your YOLO model file
- `REQUIRED_PPE`: List of PPE items to detect

### Video Settings
- `VIDEO_PATH`: Path to video file for analysis
- `WEBCAM_INDEX`: Webcam index (usually 0)

### Detection Settings
- `VIOLATION_COOLDOWN`: Seconds between violation alerts
- `STATUS_UPDATE_INTERVAL`: Seconds between status updates

### Audio Settings
- `BEEP_FREQUENCY`: Beep sound frequency in Hz
- `BEEP_DURATION`: Beep sound duration in milliseconds

## Output

### Console Output
- Real-time status updates
- Violation alerts with timestamps
- System status messages

### Log Files
- `ppe_violations.json`: JSON file containing all violations with timestamps
- Format:
  ```json
  [
    {
      "timestamp": "2024-01-15T10:30:45",
      "violation": "No Helmet, No Safety-Vest"
    }
  ]
  ```

### Visual Display
- Live video feed with bounding boxes
- Status indicator (SAFE/SAFETY VIOLATION)
- Missing PPE information overlay

## PPE Detection Classes

The system detects the following PPE items:
- **Helmet**: Hard hats and safety helmets
- **Safety-Vest**: High-visibility safety vests
- **Glass**: Safety glasses and goggles

## Troubleshooting

### Common Issues

1. **Video file not found**
   - Ensure `video_to_check.mp4` exists in the project directory
   - System will automatically fallback to webcam

2. **Model file not found**
   - Check if `yolov8s_custom.pt` exists in the project directory
   - Verify the model path in `config.py`

3. **No webcam detected**
   - Check if webcam is connected and not in use by other applications
   - Try changing `WEBCAM_INDEX` in `config.py`

4. **Display errors**
   - System will continue running without display if OpenCV display fails
   - Check if display server is available (for Linux systems)

5. **Audio not working**
   - Windows: Ensure system sounds are enabled
   - Linux/Mac: Audio fallback to console beep

### Error Messages

- `Error: Could not open video file`: Video file not found or corrupted
- `Error: Could not open webcam`: Webcam not available
- `Display error`: OpenCV display issues (system continues running)
- `Sound not available`: Audio system not available (visual alerts continue)

## Performance Optimization

### For better performance:
1. Use GPU acceleration if available
2. Reduce video resolution in `config.py`
3. Increase `VIOLATION_COOLDOWN` to reduce processing
4. Close unnecessary applications

### For better accuracy:
1. Ensure good lighting conditions
2. Position camera at appropriate distance
3. Train model with diverse PPE examples
4. Adjust detection confidence thresholds

## Development

### Adding New PPE Types
1. Update `REQUIRED_PPE` in `config.py`
2. Modify detection logic in `ppe_detector.py`
3. Update display functions in `display.py`

### Custom Model Training
1. Collect and label PPE images
2. Train YOLO model with your dataset
3. Replace `yolov8s_custom.pt` with your trained model

### Integration
The modular design allows easy integration into existing systems:
- Import individual modules as needed
- Extend classes for custom functionality
- Modify configuration for specific requirements

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues and questions:
1. Check the troubleshooting section
2. Search existing issues
3. Create a new issue with detailed description

## Changelog

### Version 1.0.0
- Initial release
- Real-time PPE detection
- JSON logging
- Audio alerts
- Modular architecture

---

