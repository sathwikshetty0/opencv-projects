import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def main():
    counter = 0
    stage = "up"
    with mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            h, w, _ = frame.shape
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(rgb)
            output = frame.copy()

            # Dynamic HUD top bar
            cv2.rectangle(output, (0, 0), (w, 45), (30, 30, 30), -1)
            cv2.putText(output, 'Pose Lunges Counter - Rep tracker & lunge posture', (15, 28), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(output, 'Press q to quit', (w - 140, 28), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1, cv2.LINE_AA)

            if results.pose_landmarks:
                mp_draw.draw_landmarks(output, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                lm = results.pose_landmarks.landmark
                
                # Check left knee angle to count lunges (Hip: 24, Knee: 26, Ankle: 28)
                hip = lm[24]
                knee = lm[26]
                ankle = lm[28]

                # Ratio maps roughly to leg bending
                ratio = int(abs((knee.y - hip.y) / (ankle.y - knee.y + 1e-6)) * 100)
                
                # Set up progress indicator bar [60% to 120%]
                progress = int(np.interp(ratio, [60, 120], [0, 100]))
                progress = np.clip(progress, 0, 100)
                
                # Draw visual feedback progress bar
                cv2.rectangle(output, (20, 100), (45, 300), (50, 50, 50), -1)
                cv2.rectangle(output, (20, 300 - int(progress * 2)), (45, 300), (0, 255, 255), -1)
                cv2.putText(output, f"{progress}%", (15, 330), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1, cv2.LINE_AA)

                # Count repetitions logic
                if ratio > 110:
                    stage = "down"
                if ratio < 80 and stage == "down":
                    stage = "up"
                    counter += 1

                # Display stats box
                cv2.rectangle(output, (w - 200, 60), (w - 15, 140), (20, 20, 20), -1)
                cv2.rectangle(output, (w - 200, 60), (w - 15, 140), (100, 100, 100), 2)
                cv2.putText(output, f"STAGE: {stage.upper()}", (w - 185, 90), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0) if stage == "up" else (0, 0, 255), 2, cv2.LINE_AA)
                cv2.putText(output, f"REPS: {counter}", (w - 185, 120), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2, cv2.LINE_AA)

            cv2.imshow('Pose Lunges Counter', output)
            if cv2.waitKey(1) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
