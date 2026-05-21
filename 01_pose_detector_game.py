import cv2
import mediapipe as mp
import random
import time
import math

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

# Game state
score = 0
target_x = random.randint(100, 540)
target_y = random.randint(100, 380)
target_radius = 30
game_duration = 30 # seconds
start_time = time.time()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Flip horizontally for natural mirror feel
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        # Time left
        elapsed = time.time() - start_time
        time_left = max(0, int(game_duration - elapsed))

        # Check game over
        if time_left == 0:
            cv2.putText(frame, "GAME OVER!", (180, 240), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
            cv2.putText(frame, f"Final Score: {score}", (200, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.imshow("Pose Detector Game", frame)
            if cv2.waitKey(1) == ord('q'):
                break
            continue

        # Process pose landmarks
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb)

        wrist_positions = []
        if results.pose_landmarks:
            mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            
            # Left wrist (15) and Right wrist (16)
            landmarks = results.pose_landmarks.landmark
            for wrist_idx in [15, 16]:
                lm = landmarks[wrist_idx]
                if lm.visibility > 0.5:
                    wrist_positions.append((int(lm.x * w), int(lm.y * h)))

        # Check collisions
        for (wx, wy) in wrist_positions:
            distance = math.sqrt((wx - target_x) ** 2 + (wy - target_y) ** 2)
            if distance < target_radius + 15: # 15 is arbitrary hand/wrist size
                score += 1
                target_x = random.randint(100, w - 100)
                target_y = random.randint(100, h - 100)
                break

        # Draw target
        cv2.circle(frame, (target_x, target_y), target_radius, (0, 255, 0), -1)
        cv2.circle(frame, (target_x, target_y), target_radius + 5, (255, 255, 255), 2)

        # Draw overlay UI
        cv2.putText(frame, f"Score: {score}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        cv2.putText(frame, f"Time: {time_left}s", (w - 150, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        cv2.imshow("Pose Detector Game", frame)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
