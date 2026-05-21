import cv2
import mediapipe as mp
import numpy as np
import time

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# Calculator button layout configuration
class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img, hover=False):
        x, y = self.pos
        color = (180, 180, 180) if not hover else (100, 200, 100)
        cv2.rectangle(img, (x, y), (x + self.width, y + self.height), color, -1)
        cv2.rectangle(img, (x, y), (x + self.width, y + self.height), (255, 255, 255), 2)
        cv2.putText(img, self.value, (x + 20, y + 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    def is_hovered(self, x, y):
        bx, by = self.pos
        return bx < x < bx + self.width and by < y < by + self.height

# Instantiate calculator buttons
buttons = []
button_values = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row_idx, row in enumerate(button_values):
    for col_idx, val in enumerate(row):
        buttons.append(Button((50 + col_idx * 75, 120 + row_idx * 75), 65, 65, val))

equation = ""
debounce_time = 0.0

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        # Draw display screen
        cv2.rectangle(frame, (50, 40), (350, 100), (220, 220, 220), -1)
        cv2.rectangle(frame, (50, 40), (350, 100), (0, 0, 0), 3)
        # Display current equation text
        cv2.putText(frame, equation, (60, 85), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        # Process hand coordinates
        clicked_val = None
        hover_idx = -1

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            lm = hand_landmarks.landmark
            # 8: Index fingertip, 4: Thumb tip
            ix, iy = int(lm[8].x * w), int(lm[8].y * h)
            tx, ty = int(lm[4].x * w), int(lm[4].y * h)

            # Draw cursor on index finger tip
            cv2.circle(frame, (ix, iy), 10, (0, 255, 255), -1)

            # Check hovering
            for idx, btn in enumerate(buttons):
                if btn.is_hovered(ix, iy):
                    hover_idx = idx
                    
                    # Check pinch clicking gesture (distance < 25)
                    dist = np.hypot(ix - tx, iy - ty)
                    if dist < 22 and (time.time() - debounce_time > 0.5):
                        clicked_val = btn.value
                        debounce_time = time.time()
                        cv2.circle(frame, (ix, iy), 20, (0, 255, 0), 4) # flash green circle click
                        break

        # Draw all buttons
        for idx, btn in enumerate(buttons):
            btn.draw(frame, hover=(idx == hover_idx))

        # Handle Click logic
        if clicked_val is not None:
            if clicked_val == "C":
                equation = ""
            elif clicked_val == "=":
                try:
                    # Evaluate arithmetic expression safely
                    equation = str(eval(equation))
                except Exception:
                    equation = "Error"
            else:
                if equation in ["Error", "0"]:
                    equation = clicked_val
                else:
                    equation += clicked_val

        cv2.putText(frame, "Pinch thumb and index over keys. 'q' to quit.", (10, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)
        
        cv2.imshow("Virtual Calculator", frame)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
