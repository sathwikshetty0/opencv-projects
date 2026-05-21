import cv2
import time
from datetime import datetime

cap = cv2.VideoCapture(0)

# Initialize variables for motion detection
first_frame = None
motion_counter = 0
recording = False
out = None

# Video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'XVID')

print("Security Alarm started. Press 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    motion_detected = False
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Initialize the first frame as the static reference background
    if first_frame is None:
        first_frame = gray
        continue

    # Absolute difference between current frame and reference frame
    frame_delta = cv2.absdiff(first_frame, gray)
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

    # Dilate thresholded image to fill in holes
    thresh = cv2.dilate(thresh, None, iterations=2)
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Inspect contours
    for c in contours:
        if cv2.contourArea(c) < 5000: # Threshold for significant motion
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        motion_detected = True

    # If motion is detected, manage video recording
    if motion_detected:
        motion_counter += 1
        cv2.putText(frame, "MOTION DETECTED!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        
        # Start recording if not already doing so
        if not recording:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"security_clip_{timestamp}.avi"
            out = cv2.VideoWriter(filename, fourcc, 20.0, (frame_width, frame_height))
            recording = True
            print(f"Motion triggered. Started recording: {filename}")
    else:
        # Stop recording after motion ceases for a short while
        if recording:
            motion_counter = 0
            recording = False
            if out is not None:
                out.release()
                print("Recording saved successfully.")

    if recording and out is not None:
        # Write timestamp on the video frame
        cv2.putText(frame, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), (10, frame_height - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
        out.write(frame)

    # Dynamic background update (gently updates the static reference frame to handle lighting shifts)
    # 98% old frame, 2% new frame
    first_frame = cv2.addWeighted(first_frame, 0.98, gray, 0.02, 0)

    cv2.imshow("Security Monitor Feed", frame)

    # Key inputs
    key = cv2.waitKey(1)
    if key == ord('r'): # Reset reference frame manually
        first_frame = None
        print("Reference frame reset.")
    elif key == ord('q'):
        break

cap.release()
if out is not None:
    out.release()
cv2.destroyAllWindows()
