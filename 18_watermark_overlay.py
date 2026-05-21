import cv2
import time
import os
from datetime import datetime

cap = cv2.VideoCapture(0)

# Check if we have a custom logo image (e.g. 1.png) to use as watermark
logo_path = "1.png"
logo = None
if os.path.exists(logo_path):
    logo = cv2.imread(logo_path)
    # Resize logo to be small (e.g. 80x80)
    logo = cv2.resize(logo, (80, 80))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    overlay = frame.copy()

    # Apply Image Logo Watermark (bottom-right corner) if exists
    if logo is not None:
        logo_h, logo_w, _ = logo.shape
        roi = frame[h - logo_h - 20 : h - 20, w - logo_w - 20 : w - 20]
        # Blend logo and roi
        blended = cv2.addWeighted(roi, 0.6, logo, 0.4, 0)
        frame[h - logo_h - 20 : h - 20, w - logo_w - 20 : w - 20] = blended

    # Draw semi-transparent background bar for text watermark (top of the frame)
    cv2.rectangle(overlay, (0, 0), (w, 50), (50, 50, 50), -1)
    
    # Add text watermark and timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    cv2.putText(overlay, "SYS MONITOR CAM - 01", (15, 32), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.putText(overlay, timestamp, (w - 280, 32), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Blend overlay with original frame (alpha blending)
    alpha = 0.4
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, dst=frame)

    cv2.imshow("Watermarked Stream", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
