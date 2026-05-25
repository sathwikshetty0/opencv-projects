import cv2
import mediapipe as mp
import numpy as np

mp_face = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def main():
    blink_count = 0
    state = "open" # "open" or "closed"
    
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
                
                # Check left eye distance (top/bottom landmarks e.g. 159 and 145)
                top = points[159]
                bottom = points[145]
                left = points[33]
                right = points[133]
                
                eye_height = np.linalg.norm(np.array(top) - np.array(bottom))
                eye_width = np.linalg.norm(np.array(left) - np.array(right))
                ear = eye_height / (eye_width + 1e-6)
                
                # Simple threshold logic for ear (Eye Aspect Ratio)
                if ear < 0.17:
                    state = "closed"
                else:
                    if state == "closed":
                        blink_count += 1
                        state = "open"
                
                cv2.circle(output, top, 3, (0, 255, 0), -1)
                cv2.circle(output, bottom, 3, (0, 255, 0), -1)
                cv2.putText(output, f"Blinks: {blink_count}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
                cv2.putText(output, f"EAR: {ear:.2f}", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

            cv2.putText(output, 'Face Eye Blink Counter', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            cv2.imshow('Eye Blink Counter', output)
            if cv2.waitKey(1) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
