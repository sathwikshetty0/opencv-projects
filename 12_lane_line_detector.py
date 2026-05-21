import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img

def draw_lines(img, lines, color=(0, 255, 0), thickness=5):
    if lines is None:
        return
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Preprocessing: Blur and Canny Edges
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Define a trapezoidal Region of Interest (ROI) at the bottom half of the frame
    # matching a standard dashboard camera perspective
    bottom_left = (int(w * 0.1), h)
    top_left = (int(w * 0.4), int(h * 0.6))
    top_right = (int(w * 0.6), int(h * 0.6))
    bottom_right = (int(w * 0.9), h)
    
    roi_vertices = np.array([[bottom_left, top_left, top_right, bottom_right]], dtype=np.int32)
    cropped_edges = region_of_interest(edges, roi_vertices)

    # Hough Transform
    # parameters: threshold=50, minLineLength=50, maxLineGap=100
    lines = cv2.HoughLinesP(cropped_edges, 1, np.pi/180, 50, minLineLength=40, maxLineGap=150)

    # Draw detected lines on a blank image, then combine
    line_img = np.zeros_like(frame)
    draw_lines(line_img, lines)
    
    # Overlay lines onto the frame
    output = cv2.addWeighted(frame, 0.8, line_img, 1.0, 0.0)

    # Visual overlays showing ROI area
    cv2.polylines(output, roi_vertices, True, (0, 0, 255), 2)
    
    cv2.putText(output, "Lane Line Detector (ROI marked in Red)", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.imshow("Lane Line Detection", output)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
