import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    
    # Define asphalt/road scan region (bottom 45% of the screen)
    road_y1 = int(h * 0.55)
    road_y2 = h
    road_x1 = int(w * 0.15)
    road_x2 = int(w * 0.85)

    # Highlight scan region on frame
    cv2.rectangle(frame, (road_x1, road_y1), (road_x2, road_y2), (255, 255, 0), 2)
    
    # Crop to scan area
    road_crop = frame[road_y1:road_y2, road_x1:road_x2]
    gray = cv2.cvtColor(road_crop, cv2.COLOR_BGR2GRAY)
    
    # Filter and find dark irregularities (potholes)
    # Apply bilateral filter to preserve edges while smoothing flat asphalt textures
    smooth = cv2.bilateralFilter(gray, 9, 75, 75)
    
    # Adaptive thresholding to isolate local dark pockets (shadows/depressions)
    thresh = cv2.adaptiveThreshold(smooth, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY_INV, 15, 8)

    # Clean morphology (opening to remove small noise lines)
    kernel = np.ones((5, 5), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # Find contours of dark spots
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    potholes_found = 0

    for c in contours:
        area = cv2.contourArea(c)
        if area < 800 or area > 15000:
            continue
            
        # Get bounding box
        x, y, wb, hb = cv2.boundingRect(c)
        aspect_ratio = float(wb) / hb
        
        # Potholes are usually oval or circular (aspect ratio between 0.5 and 2.0)
        if 0.5 < aspect_ratio < 2.0:
            potholes_found += 1
            # Draw boundary on main frame (offsetting coordinate crop back)
            mx1, my1 = x + road_x1, y + road_y1
            cv2.rectangle(frame, (mx1, my1), (mx1 + wb, my1 + hb), (0, 0, 255), 3)
            cv2.putText(frame, "POTHOLE DETECTED", (mx1, my1 - 8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Status dashboard overlay
    cv2.rectangle(frame, (0, 0), (w, 50), (40, 40, 40), -1)
    status_text = "ROAD SCANNER ACTIVE - " + ("SAFE" if potholes_found == 0 else f"WARNING: {potholes_found} POTHOLES")
    status_color = (0, 255, 0) if potholes_found == 0 else (0, 0, 255)
    cv2.putText(frame, status_text, (15, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)

    cv2.imshow("Road Damage Detection Simulation", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
