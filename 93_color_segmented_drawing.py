import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def main():
    points = []
    # Default range for tracking a blue object
    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([140, 255, 255])
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Mask for blue color
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        
        # Find contours
        contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        center = None
        
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            if cv2.contourArea(c) > 500:
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                
                # Draw visual tracking guides
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
                points.append(center)
        
        # Draw tracked lines
        for i in range(1, len(points)):
            if points[i - 1] is None or points[i] is None:
                continue
            cv2.line(frame, points[i - 1], points[i], (255, 0, 0), 4)

        cv2.putText(frame, 'Color Segmented Drawing - Hold blue object to draw', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(frame, 'Press c to clear, q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        cv2.imshow('Color Segmented Drawing', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('c'):
            points.clear()

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
