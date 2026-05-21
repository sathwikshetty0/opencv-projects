import cv2
import numpy as np

cap = cv2.VideoCapture(0)
color_mode = 'red' # 'red', 'green', 'blue'

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Color ranges in HSV
    if color_mode == 'red':
        # Red spans across the hue wrap-around boundary
        lower1 = np.array([0, 100, 100])
        upper1 = np.array([10, 255, 255])
        lower2 = np.array([170, 100, 100])
        upper2 = np.array([180, 255, 255])
        mask1 = cv2.inRange(hsv, lower1, upper1)
        mask2 = cv2.inRange(hsv, lower2, upper2)
        mask = cv2.bitwise_or(mask1, mask2)
    elif color_mode == 'green':
        lower = np.array([35, 60, 60])
        upper = np.array([85, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)
    else: # blue
        lower = np.array([100, 60, 60])
        upper = np.array([140, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)

    # Clean the mask using opening and closing
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))

    # Create grayscale background
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_3ch = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    # Combine: keep color where mask is active, otherwise keep grayscale
    mask_inv = cv2.bitwise_not(mask)
    color_part = cv2.bitwise_and(frame, frame, mask=mask)
    gray_part = cv2.bitwise_and(gray_3ch, gray_3ch, mask=mask_inv)
    output = cv2.add(color_part, gray_part)

    # UI controls
    key = cv2.waitKey(1)
    if key == ord('r'):
        color_mode = 'red'
    elif key == ord('g'):
        color_mode = 'green'
    elif key == ord('b'):
        color_mode = 'blue'
    elif key == ord('q'):
        break

    cv2.putText(output, f"Color Pop Filter: {color_mode.upper()}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(output, "Keys: r=Red | g=Green | b=Blue", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    cv2.imshow("Color Pop Filter", output)

cap.release()
cv2.destroyAllWindows()
