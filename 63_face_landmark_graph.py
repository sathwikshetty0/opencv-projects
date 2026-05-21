
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
                mp_draw.draw_landmarks(output, landmarks, mp_face.FACEMESH_TESSELATION, mp_draw.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1))
                points = [(int(p.x*w), int(p.y*h)) for p in landmarks.landmark]
                for i, point in enumerate(points[10:60:10], start=10): cv2.circle(output, point, 3, (0,255,255), -1); cv2.putText(output, f"P{i}", (point[0]+5, point[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1)

            cv2.putText(output, 'Plot face landmark positions as a live graph', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            cv2.imshow('63 Face Landmark Graph', output)
            if cv2.waitKey(1) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
