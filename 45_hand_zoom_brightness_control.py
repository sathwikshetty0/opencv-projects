import cv2
import mediapipe as mp
import numpy as np
import math

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

min_dist = 30
max_dist = 160
min_zoom = 1.0
max_zoom = 2.5

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.75, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        zoom = 1.0
        brightness = 1.0
        overlay = frame.copy()

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            mp_draw.draw_landmarks(overlay, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            lm = hand_landmarks.landmark
            thumb_tip = lm[4]
            index_tip = lm[8]
            index_mcp = lm[5]

            tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)
            ix, iy = int(index_tip.x * w), int(index_tip.y * h)
            mx, my = int(index_mcp.x * w), int(index_mcp.y * h)

            cv2.circle(overlay, (tx, ty), 10, (255, 0, 255), -1)
            cv2.circle(overlay, (ix, iy), 10, (255, 0, 255), -1)
            cv2.line(overlay, (tx, ty), (ix, iy), (255, 0, 255), 2)

            pinch_distance = math.hypot(ix - tx, iy - ty)
            zoom = np.interp(pinch_distance, [min_dist, max_dist], [min_zoom, max_zoom])
            zoom = float(np.clip(zoom, min_zoom, max_zoom))

            brightness = np.interp(iy, [0, h], [1.8, 0.6])
            brightness = float(np.clip(brightness, 0.6, 1.8))

            cv2.putText(overlay, f"Zoom: {zoom:.1f}x", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            cv2.putText(overlay, f"Brightness: {brightness:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        if zoom > 1.0:
            crop_w = int(w / zoom)
            crop_h = int(h / zoom)
            x1 = max(0, (w - crop_w) // 2)
            y1 = max(0, (h - crop_h) // 2)
            x2 = x1 + crop_w
            y2 = y1 + crop_h
            cropped = overlay[y1:y2, x1:x2]
            frame = cv2.resize(cropped, (w, h), interpolation=cv2.INTER_LINEAR)
        else:
            frame = overlay

        frame = cv2.convertScaleAbs(frame, alpha=brightness, beta=0)

        cv2.rectangle(frame, (10, 10), (310, 90), (0, 0, 0), -1)
        cv2.putText(frame, "Pinch thumb+index to zoom", (20, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(frame, "Raise index to brighten", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(frame, "Press q to quit", (20, 85), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        cv2.imshow("Hand Zoom & Brightness Control", frame)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
