import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection

cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(min_detection_confidence=0.5) as face_detection:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(rgb)

        if results.detections:
            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box
                fx = int(bbox.xmin * w)
                fy = int(bbox.ymin * h)
                fw = int(bbox.width * w)
                fh = int(bbox.height * h)

                # Ensure boundaries are inside frame
                fx, fy = max(0, fx), max(0, fy)
                fw, fh = min(w - fx, fw), min(h - fy, fh)

                if fw > 0 and fh > 0:
                    # Get face ROI
                    face_roi = frame[fy : fy + fh, fx : fx + fw]
                    
                    # Apply strong Gaussian Blur (kernel must be odd)
                    blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 30)
                    
                    # Put blurred face back onto frame
                    frame[fy : fy + fh, fx : fx + fw] = blurred_face
                    
                    # Draw a warning box indicating privacy blur is active
                    cv2.rectangle(frame, (fx, fy), (fx + fw, fy + fh), (0, 0, 255), 2)
                    cv2.putText(frame, "ANONYMOUS", (fx, fy - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        cv2.putText(frame, "Privacy Filter: Face Blurring. Press 'q' to quit.", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        cv2.imshow("Privacy Shield Camera", frame)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
