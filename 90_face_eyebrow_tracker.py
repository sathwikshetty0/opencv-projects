import cv2
import mediapipe as mp
import numpy as np

mp_face = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def main():
    # Alert threshold for raised eyebrows
    RAISED_THRESHOLD = 32

    with mp_face.FaceMesh(max_num_faces=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as face_mesh:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            h, w, _ = frame.shape
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = face_mesh.process(rgb)
            output = frame.copy()

            # Elegant HUD top bar
            cv2.rectangle(output, (0, 0), (w, 45), (30, 30, 30), -1)
            cv2.putText(output, 'Face Eyebrow Tracker - Raise eyebrows to trigger alert', (15, 28), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(output, 'Press q to quit', (w - 140, 28), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1, cv2.LINE_AA)

            if results.multi_face_landmarks:
                landmarks = results.multi_face_landmarks[0]
                points = [(int(p.x*w), int(p.y*h)) for p in landmarks.landmark]
                
                left_eyebrow = points[70]
                right_eyebrow = points[300]
                left_eye = points[159]
                right_eye = points[386]

                cv2.circle(output, left_eyebrow, 6, (0, 255, 0), -1)
                cv2.circle(output, right_eyebrow, 6, (0, 255, 0), -1)
                cv2.line(output, left_eyebrow, left_eye, (255, 0, 255), 2)
                cv2.line(output, right_eyebrow, right_eye, (255, 0, 255), 2)

                left_dist = abs(left_eyebrow[1] - left_eye[1])
                right_dist = abs(right_eyebrow[1] - right_eye[1])
                avg_dist = (left_dist + right_dist) / 2.0
                
                # Check status
                if avg_dist > RAISED_THRESHOLD:
                    cv2.putText(output, "EYEBROWS RAISED!", (w//2 - 120, h - 50), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
                    cv2.rectangle(output, (left_eyebrow[0]-20, left_eyebrow[1]-20), 
                                  (right_eyebrow[0]+20, right_eye[1]+20), (0, 0, 255), 3)
                else:
                    cv2.putText(output, "STATUS: NORMAL", (w//2 - 100, h - 50), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

                # Overlay distance metrics
                cv2.putText(output, f"L: {left_dist}px", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(output, f"R: {right_dist}px", (20, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1, cv2.LINE_AA)
                cv2.putText(output, f"Avg Dist: {avg_dist:.1f}px (Threshold: {RAISED_THRESHOLD})", (20, 140), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 1, cv2.LINE_AA)

            cv2.imshow('Face Eyebrow Tracker', output)
            if cv2.waitKey(1) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
