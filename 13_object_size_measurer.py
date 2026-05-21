import cv2
import numpy as np
from scipy.spatial import distance as dist

def order_points(pts):
    # Sort points based on their x-coordinates
    xSorted = pts[np.argsort(pts[:, 0]), :]
    
    # Grab leftmost and rightmost points
    leftMost = xSorted[:2, :]
    rightMost = xSorted[2:, :]
    
    # Sort leftmost points by y to get top-left and bottom-left
    leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
    (tl, bl) = leftMost
    
    # Sort rightmost points by y to get top-right and bottom-right
    rightMost = rightMost[np.argsort(rightMost[:, 1]), :]
    (tr, br) = rightMost
    
    return np.array([tl, tr, br, bl], dtype="float32")

def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

# Reference object width (e.g. 2.0 cm)
REF_WIDTH_CM = 2.0

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale, blur, and find edges
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
    edged = cv2.Canny(blurred, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)

    # Find contours
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter and sort contours by area (keep larger ones)
    contours = [c for c in contours if cv2.contourArea(c) > 1000]
    
    # Sort from left to right (leftmost is reference object)
    if len(contours) > 0:
        # Get bounding box centers
        boundingBoxes = [cv2.boundingRect(c) for c in contours]
        contours = [c for _, c in sorted(zip(boundingBoxes, contours), key=lambda b: b[0][0])]

    pixelsPerMetric = None

    for idx, c in enumerate(contours):
        # Compute bounding box
        box = cv2.minAreaRect(c)
        box = cv2.boxPoints(box)
        box = np.array(box, dtype="int")
        box = order_points(box)

        # Draw contour bounding box
        cv2.drawContours(frame, [box.astype("int")], -1, (0, 255, 0), 2)

        # Midpoints of bounding box edges
        (tl, tr, br, bl) = box
        (tltrX, tltrY) = midpoint(tl, tr)
        (blbrX, blbrY) = midpoint(bl, br)
        (tlblX, tlblY) = midpoint(tl, bl)
        (trbrX, trbrY) = midpoint(tr, br)

        # Compute Euclidean distance between midpoints
        dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
        dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

        # Calibrate pixelsPerMetric based on leftmost object
        if pixelsPerMetric is None:
            # Let's say the reference object's width is dB (horizontal dimension)
            pixelsPerMetric = dB / REF_WIDTH_CM
            
            # Draw reference label
            cv2.putText(frame, "Ref Obj (2cm)", (int(tl[0]), int(tl[1]) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            cv2.drawContours(frame, [box.astype("int")], -1, (0, 0, 255), 2)

        # Calculate dimensions in cm
        dimA = dA / pixelsPerMetric
        dimB = dB / pixelsPerMetric

        # Draw dimensions
        cv2.circle(frame, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
        cv2.circle(frame, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
        cv2.circle(frame, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
        cv2.circle(frame, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)
        
        cv2.line(frame, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (255, 0, 255), 1)
        cv2.line(frame, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (255, 0, 255), 1)

        cv2.putText(frame, f"{dimA:.1f}cm", (int(tltrX) - 15, int(tltrY) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2)
        cv2.putText(frame, f"{dimB:.1f}cm", (int(trbrX) + 10, int(trbrY)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2)

    cv2.putText(frame, "Leftmost object is the 2cm Reference Card/Coin.", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.imshow("Object Size Measurer", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
