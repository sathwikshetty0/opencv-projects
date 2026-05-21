import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Heatmap accumulator
ret, first_frame = cap.read()
if ret:
    first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
    first_gray = cv2.GaussianBlur(first_gray, (21, 21), 0)
    heatmap = np.zeros_like(first_gray, dtype=np.float64)

print("Motion Heatmap - Press 'q' to quit, 'r' to reset heatmap")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Compute absolute difference from first frame
    delta = cv2.absdiff(first_gray, gray)
    thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Accumulate motion into heatmap
    heatmap += thresh.astype(np.float64)

    # Normalize heatmap for display
    heatmap_display = heatmap / (heatmap.max() + 1e-5) * 255
    heatmap_display = heatmap_display.astype(np.uint8)

    # Apply color map
    heatmap_color = cv2.applyColorMap(heatmap_display, cv2.COLORMAP_JET)

    # Blend with original frame
    blended = cv2.addWeighted(frame, 0.6, heatmap_color, 0.4, 0)

    # Display info
    cv2.putText(blended, "Motion Heatmap", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    cv2.putText(blended, "Press 'r' to reset | 'q' to quit", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    cv2.imshow("Motion Heatmap", blended)
    cv2.imshow("Threshold", thresh)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('r'):
        heatmap = np.zeros_like(first_gray, dtype=np.float64)
        print("Heatmap reset!")

cap.release()
cv2.destroyAllWindows()
