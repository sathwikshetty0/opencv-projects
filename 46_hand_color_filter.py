import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

filters = ["Normal", "Grayscale", "Sepia", "Sketch", "Invert", "Color Pop"]

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
        mode = 0

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            mp_draw.draw_landmarks(display, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            lm = hand_landmarks.landmark

            fingers = []
            fingers.append(1 if lm[4].x > lm[3].x else 0)
            for tip_idx in [8, 12, 16, 20]:
                fingers.append(1 if lm[tip_idx].y < lm[tip_idx - 2].y else 0)

            mode = min(sum(fingers), 5)

            cv2.putText(display, f"Gesture Filter: {filters[mode]}", (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            cv2.putText(display, "Show 1-5 fingers to change filter", (10, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (220, 220, 220), 2)

        if mode == 1:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            display = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        elif mode == 2:
            sepia_filter = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])
            display = cv2.transform(frame, sepia_filter)
            display = np.clip(display, 0, 255).astype(np.uint8)
        elif mode == 3:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (7, 7), 0)
            display = cv2.Canny(blur, 50, 150)
            display = cv2.cvtColor(display, cv2.COLOR_GRAY2BGR)
        elif mode == 4:
            display = cv2.bitwise_not(frame)
        elif mode == 5:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, (35, 50, 50), (85, 255, 255))
            pop = cv2.bitwise_and(frame, frame, mask=mask)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            display = cv2.addWeighted(pop, 1.0, gray, 0.6, 0)

        cv2.imshow("Hand Color Filter", display)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
