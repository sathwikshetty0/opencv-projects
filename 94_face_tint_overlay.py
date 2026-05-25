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
                
                # Center of the face
                nose = points[1]
                
                # Generate dynamic tint based on nose position
                # Left side of screen = Red tint, Right side = Green/Blue tint
                tint_b = int(np.clip(nose[0] / w * 255, 0, 255))
                tint_g = int(np.clip(nose[1] / h * 255, 0, 255))
                tint_r = 255 - tint_b
                
                overlay = np.zeros_like(frame)
                overlay[:] = (tint_b, tint_g, tint_r)
                
                # Apply tint with transparency
                cv2.addWeighted(overlay, 0.25, output, 0.75, 0, output)
                cv2.circle(output, nose, 10, (255, 255, 255), -1)

            cv2.putText(output, 'Face Tint Overlay - Move face to shift colors', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            cv2.imshow('Face Tint Overlay', output)
            if cv2.waitKey(1) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
