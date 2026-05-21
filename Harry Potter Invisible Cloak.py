import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

time.sleep(2)

background = None

for i in range(30):
    ret, background = cap.read()

while True:

    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))

    mask_inv = cv2.bitwise_not(mask)

    res1 = cv2.bitwise_and(background, background, mask=mask)

    res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)

    final = cv2.add(res1, res2)

    cv2.imshow("Invisible Cloak", final)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()