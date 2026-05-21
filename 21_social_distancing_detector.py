import cv2
import numpy as np
from ultralytics import YOLO
import math

# Load pre-trained YOLOv8n model
# The file yolov8n.pt already exists in the workspace
model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)

# Social distancing distance threshold (in pixels)
SAFE_DISTANCE = 110

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 person detection
    results = model(frame, verbose=False)
    
    # Extract bounding boxes of persons (class index 0)
    person_boxes = []
    
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            if cls == 0: # Class 0 is Person
                xyxy = box.xyxy[0].cpu().numpy().astype(int)
                x1, y1, x2, y2 = xyxy
                # Centroid of the bottom edge (foot position approximation)
                cx = (x1 + x2) // 2
                cy = y2
                person_boxes.append({
                    'bbox': (x1, y1, x2, y2),
                    'foot_center': (cx, cy),
                    'violating': False
                })

    # Compare pairwise distances between detected persons
    n = len(person_boxes)
    for i in range(n):
        for j in range(i + 1, n):
            c1 = person_boxes[i]['foot_center']
            c2 = person_boxes[j]['foot_center']
            
            # Euclidean distance
            distance = math.hypot(c1[0] - c2[0], c1[1] - c2[1])
            
            if distance < SAFE_DISTANCE:
                person_boxes[i]['violating'] = True
                person_boxes[j]['violating'] = True
                
                # Draw warning link between them
                cv2.line(frame, c1, c2, (0, 0, 255), 2)
                # Display pixel distance value
                mid_x = (c1[0] + c2[0]) // 2
                mid_y = (c1[1] + c2[1]) // 2
                cv2.putText(frame, f"{int(distance)}px", (mid_x, mid_y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    # Draw bounding boxes and status labels
    for p in person_boxes:
        x1, y1, x2, y2 = p['bbox']
        cx, cy = p['foot_center']
        
        if p['violating']:
            color = (0, 0, 255) # Red for alert
            label = "ALERT"
        else:
            color = (0, 255, 0) # Green for safe
            label = "SAFE"

        # Draw box and base point
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.circle(frame, (cx, cy), 6, color, -1)
        
        # Display label
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Total violation count
    violations = sum(1 for p in person_boxes if p['violating'])
    cv2.rectangle(frame, (0, 0), (320, 50), (50, 50, 50), -1)
    cv2.putText(frame, f"People: {n} | Violations: {violations}", (15, 33),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Social Distancing Detector", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
