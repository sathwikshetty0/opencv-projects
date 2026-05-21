import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Colors: Red, Green, Blue, Eraser
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)]
color_names = ["Red", "Green", "Blue", "Eraser"]
current_color_idx = 0
brush_thickness = 8
eraser_thickness = 50

canvas = None
prev_x, prev_y = 0, 0

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.85, min_tracking_confidence=0.8) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        if canvas is None:
            canvas = np.zeros_like(frame)

        # Draw UI buttons at the top
        # Red, Green, Blue, Eraser, Clear All
        cv2.rectangle(frame, (10, 10), (100, 70), (0, 0, 255), -1)
        cv2.rectangle(frame, (110, 10), (200, 70), (0, 255, 0), -1)
        cv2.rectangle(frame, (210, 10), (300, 70), (255, 0, 0), -1)
        cv2.rectangle(frame, (310, 10), (400, 70), (200, 200, 200), -1)
        cv2.putText(frame, "Eraser", (325, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.rectangle(frame, (410, 10), (500, 70), (50, 50, 50), -1)
        cv2.putText(frame, "Clear", (430, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Display Selected tool
        cv2.putText(frame, f"Active: {color_names[current_color_idx]}", (510, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors[current_color_idx] if current_color_idx != 3 else (255, 255, 255), 2)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Landmarks: 8 = Index tip, 12 = Middle tip
            lm = hand_landmarks.landmark
            ix, iy = int(lm[8].x * w), int(lm[8].y * h)
            mx, my = int(lm[12].x * w), int(lm[12].y * h)

            # Check if fingers are up
            index_up = lm[8].y < lm[6].y
            middle_up = lm[12].y < lm[10].y

            # Selection Mode - Index and Middle both up
            if index_up and middle_up:
                prev_x, prev_y = 0, 0  # reset drawing track
                cv2.circle(frame, (ix, iy), 12, (255, 255, 255), -1) # Draw selection cursor

                # Check if clicking on header buttons
                if iy < 70:
                    if 10 < ix < 100:
                        current_color_idx = 0
                    elif 110 < ix < 200:
                        current_color_idx = 1
                    elif 210 < ix < 300:
                        current_color_idx = 2
                    elif 310 < ix < 400:
                        current_color_idx = 3 # Eraser
                    elif 410 < ix < 500:
                        canvas = np.zeros_like(frame) # Clear canvas

            # Drawing Mode - Only index finger up
            elif index_up and not middle_up:
                cv2.circle(frame, (ix, iy), brush_thickness if current_color_idx != 3 else eraser_thickness // 2, colors[current_color_idx], -1)
                
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = ix, iy

                thickness = eraser_thickness if current_color_idx == 3 else brush_thickness
                cv2.line(canvas, (prev_x, prev_y), (ix, iy), colors[current_color_idx], thickness)
                prev_x, prev_y = ix, iy
            else:
                prev_x, prev_y = 0, 0
        else:
            prev_x, prev_y = 0, 0

        # Merge canvas with original frame
        gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
        _, inv_canvas = cv2.threshold(gray_canvas, 10, 255, cv2.THRESH_BINARY_INV)
        inv_canvas = cv2.cvtColor(inv_canvas, cv2.COLOR_GRAY2BGR)
        frame = cv2.bitwise_and(frame, inv_canvas)
        frame = cv2.bitwise_or(frame, canvas)

        cv2.imshow("Virtual Paint", frame)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
