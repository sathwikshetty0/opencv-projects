import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # Pencil Sketch algorithm:
    # 1. Convert to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 2. Invert the gray image
    inv_gray = cv2.bitwise_not(gray)
    
    # 3. Apply strong Gaussian Blur to inverted gray image
    blurred = cv2.GaussianBlur(inv_gray, (21, 21), 0)
    
    # 4. Invert the blurred image back
    inv_blurred = cv2.bitwise_not(blurred)
    
    # 5. Divide gray by the inverted blurred image to perform color dodge blend
    sketch = cv2.divide(gray, inv_blurred, scale=256.0)

    # Let's display both original and sketch in a split window
    cv2.imshow("Pencil Sketch Feed", sketch)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
