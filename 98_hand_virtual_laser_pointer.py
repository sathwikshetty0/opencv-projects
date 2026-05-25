import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def main():
    points = []
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
                index_pos = (int(lm[8].x * w), int(lm[8].y * h))
                points.append(index_pos)
                
                # Draw a glowing red circle at the finger tip
                cv2.circle(output, index_pos, 10, (0, 0, 255), -1)
                cv2.circle(output, index_pos, 20, (0, 0, 255), 2)
            else:
                points.append(None)

            # Limit length of trail
            if len(points) > 30:
                points.pop(0)

            # Draw laser trail with gradual fading/thickness decay
            for i in range(1, len(points)):
                if points[i - 1] is None or points[i] is None:
                    continue
                thickness = int(np.sqrt(64 / float(i + 1)) * 2)
                cv2.line(output, points[i - 1], points[i], (0, 0, 255), thickness)

            cv2.putText(output, 'Hand Virtual Laser Pointer - Move index finger', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            cv2.imshow('Hand Virtual Laser Pointer', output)
            if cv2.waitKey(1) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
