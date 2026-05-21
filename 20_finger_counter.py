import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.75, min_tracking_confidence=0.75) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        total_fingers = 0

        if results.multi_hand_landmarks and results.multi_handedness:
            for hand_landmarks, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Determine if it's left or right hand
                hand_type = handedness.classification[0].label # "Left" or "Right"
                
                lm = hand_landmarks.landmark
                fingers_open = []

                # Thumb: Compare tip (4) with IP joint (3)
                # Since we flipped the image, left/right coordinates are mirrored
                if hand_type == "Right":
                    # If thumb tip is further right than knuckle/IP joint
                    if lm[4].x > lm[3].x:
                        fingers_open.append(1)
                    else:
                        fingers_open.append(0)
                else: # Left Hand
                    # If thumb tip is further left than knuckle/IP joint
                    if lm[4].x < lm[3].x:
                        fingers_open.append(1)
                    else:
                        fingers_open.append(0)

                # 4 Fingers: Index (8), Middle (12), Ring (16), Pinky (20)
                # Compare tip y coordinate with PIP joint (6, 10, 14, 18)
                # Note: y coordinate decreases as we go up
                finger_tips = [8, 12, 16, 20]
                finger_pips = [6, 10, 14, 18]

                for tip, pip in zip(finger_tips, finger_pips):
                    if lm[tip].y < lm[pip].y:
                        fingers_open.append(1)
                    else:
                        fingers_open.append(0)

                hand_count = sum(fingers_open)
                total_fingers += hand_count

                # Draw label near hand
                hx, hy = int(lm[0].x * w), int(lm[0].y * h)
                cv2.putText(frame, f"{hand_type}: {hand_count}", (hx, hy - 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.putText(frame, f"Total Fingers: {total_fingers}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)

        cv2.imshow("Finger Counter Feed", frame)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
