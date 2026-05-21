import cv2
import numpy as np
import subprocess
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_draw = mp.solutions.drawing_utils

def set_windows_brightness(percent):
    # Set screen brightness on Windows via PowerShell (WmiMonitorBrightnessMethods)
    # Safe to call, runs in background and won't crash if unsupported
    cmd = f"powershell -Command \"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1, {int(percent)})\""
    try:
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception:
        pass

cap = cv2.VideoCapture(0)

# Smooth brightness changes
current_brightness = 50.0

with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(rgb)

        # Default area of interest (whole frame)
        roi_brightness = 127.0
        
        if results.detections:
            for detection in results.detections:
                # Draw face bounding box
                mp_draw.draw_detection(frame, detection)
                
                # Extract face bounding box
                bbox = detection.location_data.relative_bounding_box
                fx = int(bbox.xmin * w)
                fy = int(bbox.ymin * h)
                fw = int(bbox.width * w)
                fh = int(bbox.height * h)

                # Ensure boundaries are inside frame
                fx, fy = max(0, fx), max(0, fy)
                fw, fh = min(w - fx, fw), min(h - fy, fh)

                if fw > 0 and fh > 0:
                    face_roi = frame[fy:fy+fh, fx:fx+fw]
                    gray_roi = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)
                    # Average brightness of face region (0-255)
                    roi_brightness = np.mean(gray_roi)
                    break

        # Map brightness:
        # If ambient is bright -> set high screen brightness (to counteract glare)
        # If ambient is dark -> set low screen brightness (to protect eyes)
        target_brightness = np.interp(roi_brightness, [30, 200], [20, 100])
        
        # Smooth interpolation (moving average)
        current_brightness = current_brightness + (target_brightness - current_brightness) * 0.1
        
        # Update system brightness
        set_windows_brightness(current_brightness)

        # Draw a nice visual slider gauge on screen
        cv2.rectangle(frame, (50, 400), (300, 430), (50, 50, 50), -1)
        fill_w = int((current_brightness / 100.0) * 250)
        cv2.rectangle(frame, (50, 400), (50 + fill_w, 430), (255, 255, 0), -1)
        cv2.putText(frame, f"Screen Brightness: {int(current_brightness)}%", (50, 385),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.putText(frame, f"Ambient Light: {int(roi_brightness)}/255", (50, 350),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv2.imshow("Auto Brightness Controller", frame)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
