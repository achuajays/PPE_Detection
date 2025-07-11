import cv2
import config

class PPEDetector:
    def __init__(self, model):
        self.model = model
    
    def detect_ppe(self, frame):
        """Detect PPE in frame and return detection results"""
        results = self.model(frame, verbose=False)
        detected_classes = []
        
        helmet_detected = False
        vest_detected = False
        glasses_detected = False
        
        for r in results:
            for c in r.boxes:
                class_name = self.model.names[int(c.cls)]
                if class_name in config.REQUIRED_PPE:
                    detected_classes.append(class_name)
                    x1, y1, x2, y2 = map(int, c.xyxy[0])
                    
                    if class_name.lower() in ['helmet']:
                        helmet_detected = True
                        color = config.DETECTED_COLOR
                    elif class_name.lower() in ['safety-vest']:
                        vest_detected = True
                        color = config.DETECTED_COLOR
                    elif class_name.lower() in ['glass']:
                        glasses_detected = True
                        color = config.DETECTED_COLOR
                    
                    # Draw bounding box
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(frame, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        all_ppe_present = helmet_detected and vest_detected and glasses_detected
        
        return {
            'all_ppe_present': all_ppe_present,
            'helmet_detected': helmet_detected,
            'vest_detected': vest_detected,
            'glasses_detected': glasses_detected,
            'detected_classes': detected_classes
        }
    
    def get_missing_ppe(self, detection_results):
        """Get list of missing PPE items"""
        missing_ppe = []
        if not detection_results['helmet_detected']:
            missing_ppe.append("Helmet")
        if not detection_results['vest_detected']:
            missing_ppe.append("Safety-Vest")
        if not detection_results['glasses_detected']:
            missing_ppe.append("Glasses")
        return missing_ppe