
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
prev_frame = None

def main():
    global prev_frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        output = frame.copy()

        if prev_frame is not None:
            diff = cv2.absdiff(prev_frame, gray)
            _, mask = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
            mask_color = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
            blur = cv2.GaussianBlur(output, (0,0), sigmaX=15); output = np.where(mask[:,:,None] == 255, blur, output)

        prev_frame = gray
        cv2.putText(output, 'Apply directional blur to moving regions', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        cv2.imshow('87 Motion Blur Effect', output)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
