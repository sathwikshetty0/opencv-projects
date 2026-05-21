import cv2
import mediapipe as mp
import math
import time

# Eye landmarks indices from Mediapipe Face Mesh
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def get_ear(landmarks, eye_indices, w, h):
    # Convert normalized landmarks to pixel coords
    coords = []
    for idx in eye_indices:
        lm = landmarks[idx]
        coords.append((lm.x * w, lm.y * h))
    
    # Calculate distances
    # coords[1] to coords[5] (vertical)
    # coords[2] to coords[4] (vertical)
    # coords[0] to coords[3] (horizontal)
    d_v1 = distance(coords[1], coords[5])
    d_v2 = distance(coords[2], coords[4])
    d_h = distance(coords[0], coords[3])
    
    ear = (d_v1 + d_v2) / (2.0 * d_h + 1e-6)
    return ear

cap = cv2.VideoCapture(0)
mp_face_mesh = mp.solutions.face_mesh

# Drowsiness threshold and frame count
EAR_THRESHOLD = 0.21
CONSECUTIVE_FRAMES = 25

closed_counter = 0
alarm_active = False

with mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True) as face_mesh:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark
            
            left_ear = get_ear(landmarks, LEFT_EYE, w, h)
            right_ear = get_ear(landmarks, RIGHT_EYE, w, h)
            
            avg_ear = (left_ear + right_ear) / 2.0

            # Draw eye contours for visualization
            for eye in [LEFT_EYE, RIGHT_EYE]:
                for idx in eye:
                    lm = landmarks[idx]
                    cv2.circle(frame, (int(lm.x * w), int(lm.y * h)), 2, (0, 255, 0), -1)

            # Check if average EAR is below threshold
            if avg_ear < EAR_THRESHOLD:
                closed_counter += 1
                if closed_counter >= CONSECUTIVE_FRAMES:
                    alarm_active = True
            else:
                closed_counter = 0
                alarm_active = False

            # Display EAR metrics
            cv2.putText(frame, f"EAR: {avg_ear:.2f}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        else:
            avg_ear = 0.0

        if alarm_active:
            # Visual alarm
            cv2.rectangle(frame, (0, 0), (w, h), (0, 0, 255), 10)
            cv2.putText(frame, "DROWSINESS DETECTED!", (80, 240), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
            # Standard CLI beep trigger
            print("\a", end="")

        cv2.imshow("Drowsiness Detector", frame)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
