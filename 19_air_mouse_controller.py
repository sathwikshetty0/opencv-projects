import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Configure pyautogui
pyautogui.FAILSAFE = True  # Can move mouse to corner to abort
pyautogui.PAUSE = 0

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Get primary monitor screen dimensions
screen_w, screen_h = pyautogui.size()

# Frame coordinates mapping boundary (active box in frame)
frame_lim_x1, frame_lim_y1 = 120, 100
frame_lim_x2, frame_lim_y2 = 520, 380

# Mouse smoothing variables
prev_mx, prev_my = 0, 0
smoothing = 5
click_debounce = False

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        
        # Draw active tracking boundary box
        cv2.rectangle(frame, (frame_lim_x1, frame_lim_y1), (frame_lim_x2, frame_lim_y2), (255, 0, 0), 2)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Landmarks: 4 = Thumb tip, 8 = Index tip
            lm = hand_landmarks.landmark
            ix, iy = int(lm[8].x * w), int(lm[8].y * h)
            tx, ty = int(lm[4].x * w), int(lm[4].y * h)

            # If index finger is inside the boundary box, move the cursor
            if frame_lim_x1 < ix < frame_lim_x2 and frame_lim_y1 < iy < frame_lim_y2:
                # Map coordinates to screen size
                target_x = np.interp(ix, [frame_lim_x1, frame_lim_x2], [0, screen_w])
                target_y = np.interp(iy, [frame_lim_y1, frame_lim_y2], [0, screen_h])

                # Smooth movements
                curr_mx = prev_mx + (target_x - prev_mx) / smoothing
                curr_my = prev_my + (target_y - prev_my) / smoothing

                pyautogui.moveTo(int(curr_mx), int(curr_my))
                prev_mx, prev_my = curr_mx, curr_my

            # Check for click gesture: Distance between thumb tip and middle finger or index finger
            # Let's check distance between index tip and thumb tip
            dist_click = np.hypot(ix - tx, iy - ty)
            
            if dist_click < 25:
                if not click_debounce:
                    pyautogui.click()
                    click_debounce = True
                    print("Air Mouse Clicked!")
            else:
                click_debounce = False

        cv2.putText(frame, "Air Mouse. Use index finger to move. Pinch to click.", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.imshow("Air Mouse Feed", frame)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
