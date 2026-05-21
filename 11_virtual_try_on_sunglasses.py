import cv2
import mediapipe as mp
import math
import numpy as np

mp_face_mesh = mp.solutions.face_mesh

cap = cv2.VideoCapture(0)

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

            # Landmark coordinates
            # Left eye outer corner: 130, Right eye outer corner: 359
            # Nose bridge center: 168
            le_x, le_y = int(landmarks[130].x * w), int(landmarks[130].y * h)
            re_x, re_y = int(landmarks[359].x * w), int(landmarks[359].y * h)
            nose_x, nose_y = int(landmarks[168].x * w), int(landmarks[168].y * h)

            # Draw vector details
            eye_width = int(math.hypot(re_x - le_x, re_y - le_y) * 1.2)
            eye_angle = math.degrees(math.atan2(re_y - le_y, re_x - le_x))

            # Let's draw a set of stylish custom sunglasses using a transparent overlay
            overlay = frame.copy()
            
            # Left glass center
            lg_cx = int(le_x + (nose_x - le_x) * 0.4)
            lg_cy = int(le_y + (nose_y - le_y) * 0.4)
            
            # Right glass center
            rg_cx = int(re_x - (re_x - nose_x) * 0.4)
            rg_cy = int(re_y + (nose_y - re_y) * 0.4)

            glass_radius = int(eye_width * 0.28)

            # Draw lenses
            cv2.circle(overlay, (lg_cx, lg_cy), glass_radius, (0, 0, 0), -1)
            cv2.circle(overlay, (rg_cx, rg_cy), glass_radius, (0, 0, 0), -1)

            # Draw rims/frames
            cv2.circle(overlay, (lg_cx, lg_cy), glass_radius, (0, 255, 255), 3)
            cv2.circle(overlay, (rg_cx, rg_cy), glass_radius, (0, 255, 255), 3)

            # Draw bridge line
            cv2.line(overlay, (lg_cx + glass_radius, lg_cy), (rg_cx - glass_radius, rg_cy), (0, 255, 255), 4)

            # Draw temples/arms (extending to corners)
            cv2.line(overlay, (lg_cx - glass_radius, lg_cy), (le_x - 10, le_y), (0, 255, 255), 3)
            cv2.line(overlay, (rg_cx + glass_radius, rg_cy), (re_x + 10, re_y), (0, 255, 255), 3)

            # Render reflection glares on glass
            glare_r = int(glass_radius * 0.3)
            cv2.circle(overlay, (lg_cx - int(glass_radius * 0.3), lg_cy - int(glass_radius * 0.3)), glare_r, (255, 255, 255), -1)
            cv2.circle(overlay, (rg_cx - int(glass_radius * 0.3), rg_cy - int(glass_radius * 0.3)), glare_r, (255, 255, 255), -1)

            # Blend overlay with transparent weight
            alpha = 0.75
            frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

        cv2.putText(frame, "Virtual Sunglasses Try-On. Press 'q' to quit.", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.imshow("Sunglasses Try-on", frame)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
