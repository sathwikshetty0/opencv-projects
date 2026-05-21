import cv2
import mediapipe as mp
import math
import pyautogui
import numpy as np
import time

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Disable PyAutoGUI fail-safe to prevent crash when cursor is near edges
pyautogui.FAILSAFE = False

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Volume bar configuration
vol_bar = 400
vol_per = 0
last_action_time = 0

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Landmark 4: Thumb tip, Landmark 8: Index tip
                lm = hand_landmarks.landmark
                tx, ty = int(lm[4].x * w), int(lm[4].y * h)
                ix, iy = int(lm[8].x * w), int(lm[8].y * h)

                # Draw tracking circles
                cv2.circle(frame, (tx, ty), 10, (255, 0, 255), -1)
                cv2.circle(frame, (ix, iy), 10, (255, 0, 255), -1)
                cv2.line(frame, (tx, ty), (ix, iy), (255, 0, 255), 3)

                # Center of the line
                cx, cy = (tx + ix) // 2, (ty + iy) // 2
                cv2.circle(frame, (cx, cy), 8, (0, 0, 255), -1)

                # Length of line (distance)
                distance = math.hypot(ix - tx, iy - ty)

                # Map distance (normally ~20 to ~160 pixels) to volume percentages
                vol_per = np.interp(distance, [20, 160], [0, 100])
                vol_bar = np.interp(distance, [20, 160], [400, 150])

                # Send volume commands with debounce
                now = time.time()
                if now - last_action_time > 0.15:
                    if distance < 35:
                        pyautogui.press('volumedown')
                        last_action_time = now
                    elif distance > 130:
                        pyautogui.press('volumeup')
                        last_action_time = now

        # Draw Volume Bar
        cv2.rectangle(frame, (50, 150), (85, 400), (0, 255, 0), 3)
        cv2.rectangle(frame, (50, int(vol_bar)), (85, 400), (0, 255, 0), -1)
        cv2.putText(frame, f"{int(vol_per)}%", (40, 430), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # UI instruction
        cv2.putText(frame, "Pinch < 35px: Vol- | Spread > 130px: Vol+", (120, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow("Hand Volume Control", frame)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
