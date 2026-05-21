import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Create CLAHE object
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

equalize_active = True

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Apply Equalization if active
    if equalize_active:
        # Convert to YCrCb
        ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
        # Split channels
        y, cr, cb = cv2.split(ycrcb)
        # Equalize Y channel (luminance) using CLAHE
        y_eq = clahe.apply(y)
        # Merge back and convert to BGR
        processed = cv2.merge((y_eq, cr, cb))
        processed = cv2.cvtColor(processed, cv2.COLOR_YCrCb2BGR)
    else:
        processed = frame.copy()

    # Calculate histograms for R, G, B channels of the display image
    hist_w, hist_h = 256, 120
    hist_overlay = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)
    
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)] # B, G, R
    
    for i, col in enumerate(colors):
        hist = cv2.calcHist([processed], [i], None, [256], [0, 256])
        cv2.normalize(hist, hist, 0, hist_h - 10, cv2.NORM_MINMAX)
        
        # Plot histogram lines
        points = []
        for x in range(256):
            y_val = hist_h - int(hist[x][0])
            points.append((x, y_val))
            
        for x in range(1, 256):
            cv2.line(hist_overlay, points[x - 1], points[x], col, 1, cv2.LINE_AA)

    # Embed histogram overlay in top right corner of the frame
    processed[10 : 10 + hist_h, w - hist_w - 10 : w - 10] = cv2.addWeighted(
        processed[10 : 10 + hist_h, w - hist_w - 10 : w - 10], 0.3, hist_overlay, 0.7, 0
    )
    cv2.rectangle(processed, (w - hist_w - 10, 10), (w - 10, 10 + hist_h), (255, 255, 255), 1)

    # UI controls
    key = cv2.waitKey(1)
    if key == ord('e'):
        equalize_active = not equalize_active
    elif key == ord('q'):
        break

    # Text overlay
    status = "CLAHE (ON)" if equalize_active else "ORIGINAL (OFF)"
    cv2.putText(processed, f"Equalization: {status}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
    cv2.putText(processed, "Press 'e' to toggle equalization.", (10, 55),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow("Image Histogram Equalizer", processed)

cap.release()
cv2.destroyAllWindows()
