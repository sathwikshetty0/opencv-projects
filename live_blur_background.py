import cv2

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    blur = cv2.GaussianBlur(frame,(51,51),0)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    faces = face.detectMultiScale(gray,1.3,5)

    mask = blur.copy()

    for (x,y,w,h) in faces:
        mask[y:y+h,x:x+w] = frame[y:y+h,x:x+w]

    cv2.imshow("Portrait Mode",mask)

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()