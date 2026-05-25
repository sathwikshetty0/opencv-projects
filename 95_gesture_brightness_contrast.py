import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def main():
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

            brightness = 1.0
            contrast = 0  # offset

            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                mp_draw.draw_landmarks(output, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                lm = hand_landmarks.landmark
                index = lm[8]
                
                # Map index finger y to brightness [0.5, 2.5]
                brightness = np.interp(index.y, [0.0, 1.0], [2.5, 0.5])
                # Map index finger x to contrast offset [-50, 50]
                contrast = int(np.interp(index.x, [0.0, 1.0], [-50, 50]))
                
                cv2.circle(output, (int(index.x*w), int(index.y*h)), 15, (0, 0, 255), -1)

            # Apply scale/shift adjustments
            adjusted = cv2.convertScaleAbs(frame, alpha=brightness, beta=contrast)
            
            # Show original overlay elements on top of the adjusted frame
            if results.multi_hand_landmarks:
                mp_draw.draw_landmarks(adjusted, results.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)
                cv2.circle(adjusted, (int(index.x*w), int(index.y*h)), 15, (0, 255, 255), 2)
            
            output = adjusted
            cv2.putText(output, f'Brightness: {brightness:.2f}  Contrast: {contrast}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
            cv2.putText(output, 'Gesture Brightness & Contrast Control', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            cv2.imshow('Gesture Brightness Contrast', output)
            if cv2.waitKey(1) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
