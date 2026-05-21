import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Zoom parameters
zoom_level = 1.0
min_zoom = 1.0
max_zoom = 4.0

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            lm = results.multi_hand_landmarks[0]
            mp_draw.draw_landmarks(frame, lm, mp_hands.HAND_CONNECTIONS)

            # Get thumb tip and index tip
            thumb_tip = lm.landmark[4]
            index_tip = lm.landmark[8]

            tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)
            ix, iy = int(index_tip.x * w), int(index_tip.y * h)

            # Distance between thumb and index
            dist = np.hypot(ix - tx, iy - ty)

            # Map distance to zoom level (close = zoom in, far = zoom out)
            zoom_level = np.interp(dist, [30, 250], [max_zoom, min_zoom])
            zoom_level = np.clip(zoom_level, min_zoom, max_zoom)

            # Draw line between fingers
            cv2.line(frame, (tx, ty), (ix, iy), (0, 255, 255), 2)
            cv2.circle(frame, (tx, ty), 8, (255, 0, 0), -1)
            cv2.circle(frame, (ix, iy), 8, (255, 0, 0), -1)

            # Center point for zoom
            cx, cy = (tx + ix) // 2, (ty + iy) // 2
            cv2.circle(frame, (cx, cy), 6, (0, 255, 0), -1)

        # Apply zoom
        zh = int(h / zoom_level)
        zw = int(w / zoom_level)
        cx_zoom = w // 2
        cy_zoom = h // 2

        x1 = max(cx_zoom - zw // 2, 0)
        y1 = max(cy_zoom - zh // 2, 0)
        x2 = min(cx_zoom + zw // 2, w)
        y2 = min(cy_zoom + zh // 2, h)

        cropped = frame[y1:y2, x1:x2]
        zoomed = cv2.resize(cropped, (w, h))

        # Display zoom level
        cv2.putText(zoomed, f"Zoom: {zoom_level:.1f}x", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Pinch Zoom Camera", zoomed)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
