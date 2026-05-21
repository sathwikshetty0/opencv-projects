import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import math
import time

pyautogui.FAILSAFE = False
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

last_click = 0.0
click_threshold = 30

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        display = frame.copy()
        status = "Move index finger to control pointer"

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            mp_draw.draw_landmarks(display, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            lm = hand_landmarks.landmark

            ix = int(lm[8].x * w)
            iy = int(lm[8].y * h)
            tx = int(lm[4].x * w)
            ty = int(lm[4].y * h)

            cv2.circle(display, (ix, iy), 12, (0, 255, 0), -1)
            cv2.circle(display, (tx, ty), 12, (255, 0, 255), -1)
            cv2.line(display, (ix, iy), (tx, ty), (255, 255, 0), 2)

            distance = math.hypot(ix - tx, iy - ty)
            status = "Pinch to click"

            screen_x = int(np.interp(ix, [0, w], [0, pyautogui.size().width]))
            screen_y = int(np.interp(iy, [0, h], [0, pyautogui.size().height]))
            pyautogui.moveTo(screen_x, screen_y, duration=0.01)

            if distance < click_threshold and time.time() - last_click > 0.4:
                pyautogui.click()
                last_click = time.time()
                status = "Clicked"

        cv2.putText(display, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(display, "Press q to quit", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

        cv2.imshow("Hand Click Pointer", display)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
