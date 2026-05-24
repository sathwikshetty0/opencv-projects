import cv2
import mediapipe as mp
import numpy as np

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def main():
    canvas = None
    with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            h, w, _ = frame.shape
            if canvas is None:
                canvas = np.zeros((h, w, 3), dtype=np.uint8)

            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb)
            output = frame.copy()

            # Draw a sample shape on canvas to erase
            cv2.circle(canvas, (w//2, h//2), 60, (0, 0, 255), -1)
            cv2.rectangle(canvas, (80, 80), (200, 200), (0, 255, 0), 3)

            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                mp_draw.draw_landmarks(output, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                lm = hand_landmarks.landmark
                index_pos = (int(lm[8].x * w), int(lm[8].y * h))
                
                # Erase by drawing a black circle on the canvas
                cv2.circle(canvas, index_pos, 40, (0, 0, 0), -1)
                cv2.circle(output, index_pos, 40, (0, 255, 255), 2)

            # Combine canvas and frame
            gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(gray_canvas, 10, 255, cv2.THRESH_BINARY)
            foreground = cv2.bitwise_and(canvas, canvas, mask=mask)
            background = cv2.bitwise_and(output, output, mask=cv2.bitwise_not(mask))
            output = cv2.add(foreground, background)

            cv2.putText(output, 'Hand Virtual Eraser - Move index finger to erase shapes', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            cv2.imshow('Hand Virtual Eraser', output)
            if cv2.waitKey(1) == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
