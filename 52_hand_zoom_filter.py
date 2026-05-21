
import cv2
import mediapipe as mp
import numpy as np
import math

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def main():
    with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            h, w, _ = frame.shape
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)
            output = frame.copy()

            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                mp_draw.draw_landmarks(output, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                lm = hand_landmarks.landmark
                thumb = lm[4]
                index = lm[8]
                middle = lm[12]
                ring = lm[16]
                pinky = lm[20]
                thumb_pos = (int(thumb.x * w), int(thumb.y * h))
                index_pos = (int(index.x * w), int(index.y * h))
                midpoint = ((thumb_pos[0] + index_pos[0]) // 2, (thumb_pos[1] + index_pos[1]) // 2)
                cv2.circle(output, thumb_pos, 10, (255, 0, 255), -1)
                cv2.circle(output, index_pos, 10, (255, 0, 255), -1)
                cv2.line(output, thumb_pos, index_pos, (255, 255, 0), 2)
                distance = int(math.hypot(index_pos[0] - thumb_pos[0], index_pos[1] - thumb_pos[1]))
                zoom = np.interp(distance, [30, 180], [1.0, 2.2]); crop_w = int(w / zoom); crop_h = int(h / zoom); x1 = max(0, (w - crop_w)//2); y1 = max(0, (h - crop_h)//2); crop = output[y1:y1+crop_h, x1:x1+crop_w]; output = cv2.resize(crop, (w, h)); cv2.putText(output, f"Zoom: {zoom:.1f}x", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)

            cv2.putText(output, 'Zoom and apply a filter using pinch distance', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            cv2.imshow('52 Hand Zoom Filter', output)
            if cv2.waitKey(1) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
