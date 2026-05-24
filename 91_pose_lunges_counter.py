import cv2
import mediapipe as mp
import math

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def main():
    counter = 0
    stage = None # "up" or "down"
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

            if results.pose_landmarks:
                mp_draw.draw_landmarks(output, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                lm = results.pose_landmarks.landmark
                
                # Check left knee angle to count lunges
                # Hip: 24, Knee: 26, Ankle: 28
                hip = lm[24]
                knee = lm[26]
                ankle = lm[28]

                # Calculate angle (using simple geometry or y distance ratio for simulation)
                ratio = int(abs((knee.y - hip.y) / (ankle.y - knee.y + 1e-6)) * 100)
                
                # Logic for lunge repetition detection
                if ratio > 110:
                    stage = "down"
                if ratio < 80 and stage == "down":
                    stage = "up"
                    counter += 1

                cv2.putText(output, f"Lunge Stage: {stage}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(output, f"Reps: {counter}", (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            cv2.putText(output, 'Pose Lunges Counter - Stand in view and do lunges', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            cv2.imshow('Pose Lunges Counter', output)
            if cv2.waitKey(1) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
