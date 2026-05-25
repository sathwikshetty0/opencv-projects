import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def main():
    ret, prev_frame = cap.read()
    if not ret:
        return
    prev_frame = cv2.flip(prev_frame, 1)
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    
    # Threshold percentage of pixels in motion to trigger alarm
    THRESHOLD_PERCENT = 4.5

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        diff = cv2.absdiff(prev_gray, gray)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        
        # Calculate percentage of moving pixels
        non_zero = cv2.countNonZero(thresh)
        total_pixels = thresh.shape[0] * thresh.shape[1]
        motion_percent = (non_zero / total_pixels) * 100
        
        output = frame.copy()
        
        if motion_percent > THRESHOLD_PERCENT:
            # Draw flash warning
            cv2.rectangle(output, (0, 0), (output.shape[1], output.shape[0]), (0, 0, 255), 15)
            cv2.putText(output, "WARNING: MOTION SPEED HIGH!", (10, 100), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 3)
        
        cv2.putText(output, f"Motion Intensity: {motion_percent:.2f}%", (10, 130), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        prev_gray = gray

        cv2.putText(output, 'Motion Speed Threshold Alert - Move fast to trigger alert', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.imshow('Motion Speed Alert', output)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
