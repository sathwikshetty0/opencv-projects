import cv2
import numpy as np

def detect_shape(c):
    shape = "unidentified"
    # Approximate contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)

    # Triangle
    if len(approx) == 3:
        shape = "Triangle"
    
    # 4 vertices: Square or Rectangle
    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        # square has an aspect ratio close to 1
        shape = "Square" if 0.95 <= ar <= 1.05 else "Rectangle"
        
    # Pentagon
    elif len(approx) == 5:
        shape = "Pentagon"
        
    # Hexagon
    elif len(approx) == 6:
        shape = "Hexagon"
        
    # Otherwise assume circle
    elif len(approx) >= 7:
        shape = "Circle"
        
    return shape

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)[1]

    # Find contours
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        # Ignore tiny noise contours
        if cv2.contourArea(c) < 1500:
            continue

        # Get shape name
        shape = detect_shape(c)
        
        # Draw contour shape outline and name
        cv2.drawContours(frame, [c], -1, (0, 255, 0), 2)
        
        # Get center of contour to write shape name
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.putText(frame, shape, (cX - 20, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.putText(frame, "Shape Detector. Hold high-contrast shapes. Press 'q' to quit.", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2)
    cv2.imshow("Shape Detector", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
