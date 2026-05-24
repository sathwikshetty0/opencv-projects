import cv2
import mediapipe as mp
import numpy as np

mp_face = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def main():
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

            if results.multi_face_landmarks:
                landmarks = results.multi_face_landmarks[0]
                points = [(int(p.x*w), int(p.y*h)) for p in landmarks.landmark]
                
                # Draw eyebrow points (left eyebrow 70 to 107 roughly, right eyebrow 300 to 336)
                # Let's use some specific landmark points: Left: 70, 107. Right: 300, 336.
                left_eyebrow = points[70]
                right_eyebrow = points[300]
                left_eye = points[159]
                right_eye = points[386]

                cv2.circle(output, left_eyebrow, 8, (0, 255, 0), -1)
                cv2.circle(output, right_eyebrow, 8, (0, 255, 0), -1)
                cv2.line(output, left_eyebrow, left_eye, (0, 0, 255), 2)
                cv2.line(output, right_eyebrow, right_eye, (0, 0, 255), 2)

                left_dist = abs(left_eyebrow[1] - left_eye[1])
                right_dist = abs(right_eyebrow[1] - right_eye[1])
                cv2.putText(output, f"L-Eyebrow Dist: {left_dist}px", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
                cv2.putText(output, f"R-Eyebrow Dist: {right_dist}px", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

            cv2.putText(output, 'Face Eyebrow Tracker', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            cv2.imshow('Face Eyebrow Tracker', output)
            if cv2.waitKey(1) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
