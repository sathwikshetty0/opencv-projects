import cv2
import time
import math

cap = cv2.VideoCapture(0)

tracker = None
init_bbox = None
prev_center = None
prev_time = None
speed_history = []
trail = []

# Conversion ratio (e.g., 100 pixels = 0.5 meters)
PIXELS_PER_METER = 200.0

print("Press 's' to select the object to track.")
print("Press 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape

    if tracker is not None:
        success, bbox = tracker.update(frame)
        
        if success:
            x, y, w_box, h_box = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)
            
            # Centroid
            cx = x + w_box // 2
            cy = y + h_box // 2
            curr_center = (cx, cy)
            curr_time = time.time()

            # Append to trail
            trail.append(curr_center)
            if len(trail) > 30:
                trail.pop(0)

            # Draw trail
            for idx in range(1, len(trail)):
                cv2.line(frame, trail[idx - 1], trail[idx], (0, 255, 255), 2)

            # Calculate Speed
            if prev_center is not None and prev_time is not None:
                dt = curr_time - prev_time
                if dt > 0:
                    pixel_dist = math.hypot(curr_center[0] - prev_center[0], curr_center[1] - prev_center[1])
                    # Speed in pixels/second
                    speed_px_sec = pixel_dist / dt
                    # Speed in meters/second (approximate)
                    speed_m_sec = speed_px_sec / PIXELS_PER_METER
                    # Speed in km/h
                    speed_kmh = speed_m_sec * 3.6
                    
                    # Smooth speed representation
                    speed_history.append(speed_kmh)
                    if len(speed_history) > 10:
                        speed_history.pop(0)
                    avg_speed = sum(speed_history) / len(speed_history)

                    cv2.putText(frame, f"Speed: {avg_speed:.2f} km/h", (x, y - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
            prev_center = curr_center
            prev_time = curr_time
        else:
            cv2.putText(frame, "Tracking failed!", (10, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            prev_center = None
            prev_time = None

    # Instructions
    cv2.putText(frame, "Speed Estimator. Press 's' to select ROI. 'q' to quit.", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Speed Estimator", frame)

    key = cv2.waitKey(1)
    if key == ord('s'):
        # Select bounding box
        init_bbox = cv2.selectROI("Speed Estimator", frame, fromCenter=False, showCrosshair=True)
        if init_bbox[2] > 0 and init_bbox[3] > 0:
            # We initialize TrackerKCF
            tracker = cv2.TrackerKCF_create()
            tracker.init(frame, init_bbox)
            trail.clear()
            speed_history.clear()
            prev_center = None
            prev_time = None
            print("Tracker initialized successfully.")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
