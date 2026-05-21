import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

# Create a window for controls
cv2.namedWindow("Morphology Explorer")

# Create trackbars
cv2.createTrackbar("Operator", "Morphology Explorer", 0, 3, nothing) # 0: Erode, 1: Dilate, 2: Open, 3: Close
cv2.createTrackbar("Kernel Size", "Morphology Explorer", 3, 21, nothing)
cv2.createTrackbar("Kernel Shape", "Morphology Explorer", 0, 2, nothing) # 0: Rect, 1: Cross, 2: Ellipse

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Threshold to binary for clear morphology demonstration
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # Read Trackbar states
    op_idx = cv2.getTrackbarPos("Operator", "Morphology Explorer")
    k_size = cv2.getTrackbarPos("Kernel Size", "Morphology Explorer")
    k_shape = cv2.getTrackbarPos("Kernel Shape", "Morphology Explorer")

    # Kernel size must be odd and at least 1
    if k_size < 1:
        k_size = 1
    elif k_size % 2 == 0:
        k_size += 1

    # Select kernel shape
    if k_shape == 0:
        shape = cv2.MORPH_RECT
        shape_name = "RECTANGLE"
    elif k_shape == 1:
        shape = cv2.MORPH_CROSS
        shape_name = "CROSS"
    else:
        shape = cv2.MORPH_ELLIPSE
        shape_name = "ELLIPSE"

    kernel = cv2.getStructuringElement(shape, (k_size, k_size))

    # Apply operator
    if op_idx == 0:
        result = cv2.erode(binary, kernel, iterations=1)
        op_name = "EROSION"
    elif op_idx == 1:
        result = cv2.dilate(binary, kernel, iterations=1)
        op_name = "DILATION"
    elif op_idx == 2:
        result = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
        op_name = "OPENING"
    else:
        result = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)
        op_name = "CLOSING"

    # Display results side-by-side (Binary vs Morphological result)
    h, w = binary.shape
    half_w, half_h = w // 2, h // 2
    
    view_bin = cv2.resize(binary, (half_w, half_h))
    view_res = cv2.resize(result, (half_w, half_h))

    # Convert to BGR to write colored text
    view_bin_bgr = cv2.cvtColor(view_bin, cv2.COLOR_GRAY2BGR)
    view_res_bgr = cv2.cvtColor(view_res, cv2.COLOR_GRAY2BGR)

    cv2.putText(view_bin_bgr, "Binary Threshold", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(view_res_bgr, f"Result: {op_name}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(view_res_bgr, f"Kernel: {k_size}x{k_size} ({shape_name})", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)

    comparison = np.hstack((view_bin_bgr, view_res_bgr))

    cv2.imshow("Morphology Explorer", comparison)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
