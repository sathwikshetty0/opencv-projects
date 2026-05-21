import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Slide controller state variables
x_history = []
last_action_time = 0
cooldown_seconds = 1.0
gesture_message = "READY"
msg_display_time = 0

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.75, min_tracking_confidence=0.75) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1) # Flip horizontally for natural mirror behavior
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        now = time.time()

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Center of the hand (landmark 9: Middle finger MCP joint)
            cx = int(hand_landmarks.landmark[9].x * w)
            cy = int(hand_landmarks.landmark[9].y * h)
            
            cv2.circle(frame, (cx, cy), 8, (0, 255, 0), -1)

            x_history.append((cx, now))
            # Keep history short (last 10 frames)
            if len(x_history) > 10:
                x_history.pop(0)

            # Detect swipe: compare current x with x from ~0.25 seconds ago
            if len(x_history) > 5 and (now - last_action_time > cooldown_seconds):
                start_x, start_time = x_history[0]
                dx = cx - start_x
                dt = now - start_time
                
                # Check swipe speed/threshold
                if dt > 0.05:
                    speed = dx / dt # pixels per second
                    
                    # Swipe Right -> Previous slide (Page Up)
                    if dx > 130 and abs(speed) > 400:
                        pyautogui.press('pgup')
                        last_action_time = now
                        gesture_message = "SWIPE RIGHT -> PREVIOUS SLIDE"
                        msg_display_time = now
                        x_history.clear()
                        print(gesture_message)
                        
                    # Swipe Left -> Next slide (Page Down)
                    elif dx < -130 and abs(speed) > 400:
                        pyautogui.press('pgdn')
                        last_action_time = now
                        gesture_message = "SWIPE LEFT -> NEXT SLIDE"
                        msg_display_time = now
                        x_history.clear()
                        print(gesture_message)
        else:
            x_history.clear()

        # Display active swipe status
        if now - msg_display_time < cooldown_seconds:
            cv2.rectangle(frame, (0, h - 60), (w, h), (0, 255, 0), -1)
            cv2.putText(frame, gesture_message, (50, h - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 2)
        else:
            cv2.putText(frame, "Swipe LEFT for next slide | Swipe RIGHT for previous slide", (10, h - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)

        cv2.putText(frame, "Presentation Slide Controller. Press 'q' to quit.", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        cv2.imshow("Air Slide Controller", frame)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
