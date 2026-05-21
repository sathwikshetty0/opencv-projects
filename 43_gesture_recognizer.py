import cv2
import mediapipe as mp
import numpy as np
import time

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Gesture trail
trail = []
max_trail_length = 60

# Gesture recognition thresholds
def get_finger_states(landmarks, w, h):
    """Returns list of booleans for each finger being up."""
    tips = [8, 12, 16, 20]  # index, middle, ring, pinky
    pips = [6, 10, 14, 18]
    
    fingers = []
    # Thumb (special case - check x direction)
    if landmarks[4].x < landmarks[3].x:
        fingers.append(True)
    else:
        fingers.append(False)
    
    # Other fingers
    for tip, pip in zip(tips, pips):
        if landmarks[tip].y < landmarks[pip].y:
            fingers.append(True)
        else:
            fingers.append(False)
    
    return fingers

def classify_gesture(fingers):
    """Classify hand gesture based on finger states."""
    total_up = sum(fingers)
    
    if total_up == 0:
        return "FIST"
    elif total_up == 5:
        return "OPEN PALM"
    elif fingers == [False, True, False, False, False]:
        return "POINTING"
    elif fingers == [False, True, True, False, False]:
        return "PEACE"
    elif fingers == [True, True, False, False, True]:
        return "ROCK ON"
    elif fingers == [True, False, False, False, True]:
        return "HANG LOOSE"
    elif fingers == [False, False, False, False, True]:
        return "PINKY"
    elif fingers == [True, True, True, False, False]:
        return "THREE"
    elif fingers == [True, True, True, True, False]:
        return "FOUR"
    elif fingers == [True, False, False, False, False]:
        return "THUMBS UP"
    else:
        return f"{total_up} FINGERS"

# Colors for different gestures
gesture_colors = {
    "FIST": (0, 0, 255),
    "OPEN PALM": (0, 255, 0),
    "POINTING": (255, 255, 0),
    "PEACE": (255, 0, 255),
    "ROCK ON": (0, 165, 255),
    "HANG LOOSE": (255, 165, 0),
    "THUMBS UP": (0, 255, 255),
    "THREE": (128, 0, 128),
    "FOUR": (255, 128, 0),
    "PINKY": (128, 255, 128),
}

with mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_lm, hand_info in zip(results.multi_hand_landmarks, results.multi_handedness):
                mp_draw.draw_landmarks(frame, hand_lm, mp_hands.HAND_CONNECTIONS)

                hand_label = hand_info.classification[0].label
                fingers = get_finger_states(hand_lm.landmark, w, h)
                gesture = classify_gesture(fingers)

                # Get wrist position for label
                wrist = hand_lm.landmark[0]
                wx, wy = int(wrist.x * w), int(wrist.y * h)

                color = gesture_colors.get(gesture, (255, 255, 255))

                # Draw gesture label
                cv2.putText(frame, f"{hand_label}: {gesture}", (wx - 50, wy - 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

                # Add index tip to trail
                idx_tip = hand_lm.landmark[8]
                trail.append((int(idx_tip.x * w), int(idx_tip.y * h), color))
                if len(trail) > max_trail_length:
                    trail.pop(0)

        # Draw trail with fading
        for i in range(1, len(trail)):
            alpha = i / len(trail)
            thickness = int(alpha * 4) + 1
            cv2.line(frame, (trail[i-1][0], trail[i-1][1]),
                     (trail[i][0], trail[i][1]), trail[i][2], thickness)

        cv2.putText(frame, "Gesture Recognizer", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        cv2.imshow("Gesture Recognizer", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
