import cv2

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detect and decode
    data, bbox, straight_qrcode = detector.detectAndDecode(frame)

    if bbox is not None:
        # Draw bounding box
        n_pts = len(bbox[0])
        for i in range(n_pts):
            pt1 = tuple(map(int, bbox[0][i]))
            pt2 = tuple(map(int, bbox[0][(i + 1) % n_pts]))
            cv2.line(frame, pt1, pt2, (0, 255, 0), 3)

        if data:
            cv2.putText(frame, f"Data: {data}", (int(bbox[0][0][0]), int(bbox[0][0][1]) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            print(f"Decoded QR Code: {data}")

    cv2.putText(frame, "Hold a QR Code in front of the camera. Press 'q' to quit.", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.imshow("QR Code Scanner", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
