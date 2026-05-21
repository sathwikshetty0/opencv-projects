import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

scan_index = 0
canvas = None
slit_width = 2 # Pixels captured per frame

print("Slit-scan camera active. Move objects across the center line. 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    if canvas is None:
        canvas = np.zeros_like(frame)

    # Slit coordinates (center of the screen)
    cx = w // 2
    slit = frame[:, cx - slit_width // 2 : cx + slit_width // 2]

    # Write slit into canvas at scan_index position
    if scan_index + slit_width <= w:
        canvas[:, scan_index : scan_index + slit_width] = slit
        scan_index += slit_width
    else:
        # Reset and clear scan index
        scan_index = 0
        canvas = np.zeros_like(frame)

    # Draw indicator line on camera feed
    display_frame = frame.copy()
    cv2.line(display_frame, (cx, 0), (cx, h), (0, 255, 0), 2)
    cv2.putText(display_frame, "Center Scan Line", (cx + 10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Show side by side: live feed with scan line vs compiled slit-scan
    cv2.putText(canvas, f"Scan Progress: {int((scan_index/w)*100)}%", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    cv2.imshow("Slit-Scan Live Feed", display_frame)
    cv2.imshow("Slit-Scan Output", canvas)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
