import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Range for fire color in HSV (typically Red/Orange/Yellow)
lower_fire = np.array([0, 80, 180])
upper_fire = np.array([35, 255, 255])

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold for fire color
    mask = cv2.inRange(hsv, lower_fire, upper_fire)
    
    # Preprocess mask
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))

    # Find contours
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    fire_active = False
    for c in contours:
        # Filter tiny noise pixels
        if cv2.contourArea(c) < 1500:
            continue
            
        fire_active = True
        (x, y, wb, hb) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + wb, y + hb), (0, 0, 255), 2)
        cv2.putText(frame, "FIRE HAZARD ZONE", (x, y - 8),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

    # If fire is detected, render flashing warning boundaries
    if fire_active:
        cv2.rectangle(frame, (0, 0), (w, h), (0, 0, 255), 8) # flashing thick frame border
        cv2.putText(frame, "WARNING: FIRE DETECTED!", (120, 240),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 0, 255), 3)

    cv2.putText(frame, "Fire Detection Color Scanner. Press 'q' to quit.", (15, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    cv2.imshow("Industrial Safety Fire Detector", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
