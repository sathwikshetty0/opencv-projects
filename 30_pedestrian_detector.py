import cv2
import numpy as np

# Initialize HOG descriptor / People detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Pedestrian detection works better on slightly smaller images
    h, w, _ = frame.shape
    scale_w = 500
    scale_h = int(h * (scale_w / w))
    resized = cv2.resize(frame, (scale_w, scale_h))

    # Detect pedestrians in the image
    # winStride determines step size of the scanning window
    # padding adds empty borders for feature inspection
    # scale controls image pyramid resizing
    rects, weights = hog.detectMultiScale(resized, winStride=(4, 4), padding=(8, 8), scale=1.05)

    # Apply Non-Max Suppression (NMS) to remove overlapping redundant bounding boxes
    rects = np.array([[x, y, x + w_box, y + h_box] for (x, y, w_box, h_box) in rects])
    pick = []
    
    # Simple NMS coordinate thresholding
    if len(rects) > 0:
        x1 = rects[:, 0]
        y1 = rects[:, 1]
        x2 = rects[:, 2]
        y2 = rects[:, 3]
        
        area = (x2 - x1 + 1) * (y2 - y1 + 1)
        idxs = np.argsort(y2)
        
        while len(idxs) > 0:
            last = len(idxs) - 1
            i = idxs[last]
            pick.append(i)
            
            xx1 = np.maximum(x1[i], x1[idxs[:last]])
            yy1 = np.maximum(y1[i], y1[idxs[:last]])
            xx2 = np.minimum(x2[i], x2[idxs[:last]])
            yy2 = np.minimum(y2[i], y2[idxs[:last]])
            
            w_overlap = np.maximum(0, xx2 - xx1 + 1)
            h_overlap = np.maximum(0, yy2 - yy1 + 1)
            
            overlap = (w_overlap * h_overlap) / area[idxs[:last]]
            idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > 0.3)[0])))

    # Draw final boxes on resized frame
    for idx in pick:
        xA, yA, xB, yB = rects[idx]
        cv2.rectangle(resized, (xA, yA), (xB, yB), (0, 255, 0), 2)
        cv2.putText(resized, "Pedestrian", (xA, yA - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.putText(resized, f"People count: {len(pick)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    cv2.imshow("Pedestrian Detector (HOG+SVM)", resized)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
