import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.75, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)
        output = frame.copy()
        effect_text = "No lens effect"

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            mp_draw.draw_landmarks(output, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            lm = hand_landmarks.landmark

            center_x = int((lm[0].x + lm[9].x) / 2 * w)
            center_y = int((lm[0].y + lm[9].y) / 2 * h)
            palm_radius = int(abs(lm[0].x - lm[9].x) * w * 1.1)

            crop_x1 = max(0, center_x - palm_radius)
            crop_y1 = max(0, center_y - palm_radius)
            crop_x2 = min(w, center_x + palm_radius)
            crop_y2 = min(h, center_y + palm_radius)
            lens = output[crop_y1:crop_y2, crop_x1:crop_x2]

            if lens.size > 0:
                gray = cv2.cvtColor(lens, cv2.COLOR_BGR2GRAY)
                blurred = cv2.GaussianBlur(gray, (15, 15), 0)
                edges = cv2.Canny(blurred, 50, 150)
                edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

                effect_text = "Lens: sketch"
                output[crop_y1:crop_y2, crop_x1:crop_x2] = cv2.addWeighted(lens, 0.3, edges, 0.7, 0)

                overlay = output.copy()
                mask = np.zeros((h, w), dtype=np.uint8)
                cv2.circle(mask, (center_x, center_y), palm_radius, 255, -1)
                mask_inv = cv2.bitwise_not(mask)
                output = cv2.bitwise_and(output, output, mask=mask)
                dark = cv2.addWeighted(output, 0.4, output, 0, 0)
                output = cv2.bitwise_or(dark, cv2.bitwise_and(overlay, overlay, mask=mask_inv))

            cv2.circle(output, (center_x, center_y), palm_radius, (0, 255, 255), 2)

        cv2.putText(output, effect_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200, 200, 200), 2)
        cv2.putText(output, "Show your palm to enable lens effect", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

        cv2.imshow("Hand Camera Lens", output)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
