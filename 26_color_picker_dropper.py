import cv2
import numpy as np

# Global variables
current_color = (0, 0, 0)
hsv_color = (0, 0, 0)
hex_color = "#000000"
mouse_x, mouse_y = 0, 0

def mouse_callback(event, x, y, flags, param):
    global current_color, hsv_color, hex_color, mouse_x, mouse_y, frame
    mouse_x, mouse_y = x, y
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get color at (y, x) because numpy is row-major
        # Avoid boundary checks
        if y < frame.shape[0] and x < frame.shape[1]:
            b, g, r = frame[y, x]
            current_color = (int(b), int(g), int(r))
            
            # Convert single pixel BGR to HSV
            pixel_bgr = np.uint8([[[b, g, r]]])
            pixel_hsv = cv2.cvtColor(pixel_bgr, cv2.COLOR_BGR2HSV)
            hsv_color = tuple(pixel_hsv[0][0])
            
            # Convert BGR to HEX
            hex_color = f"#{r:02x}{g:02x}{b:02x}".upper()
            print(f"Picked Color: BGR={current_color} | HSV={hsv_color} | HEX={hex_color}")

cap = cv2.VideoCapture(0)
cv2.namedWindow("Color Picker Dropper")
cv2.setMouseCallback("Color Picker Dropper", mouse_callback)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    
    # Make a copy for display
    display_frame = frame.copy()

    # Draw color swatch box in top-right corner
    swatch_w, swatch_h = 120, 80
    cv2.rectangle(display_frame, (w - swatch_w - 10, 10), (w - 10, 10 + swatch_h), current_color, -1)
    cv2.rectangle(display_frame, (w - swatch_w - 10, 10), (w - 10, 10 + swatch_h), (255, 255, 255), 2)

    # Print values on screen
    cv2.putText(display_frame, f"HEX: {hex_color}", (w - swatch_w - 10, 10 + swatch_h + 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
    cv2.putText(display_frame, f"RGB: {current_color[2]},{current_color[1]},{current_color[0]}", (w - swatch_w - 10, 10 + swatch_h + 38),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
    cv2.putText(display_frame, f"HSV: {hsv_color[0]},{hsv_color[1]},{hsv_color[2]}", (w - swatch_w - 10, 10 + swatch_h + 56),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)

    # Draw small crosshair and live color under cursor
    if 0 <= mouse_x < w and 0 <= mouse_y < h:
        # Get live BGR values
        lb, lg, lr = frame[mouse_y, mouse_x]
        cv2.circle(display_frame, (mouse_x, mouse_y), 8, (255, 255, 255), 1)
        cv2.circle(display_frame, (mouse_x, mouse_y), 3, (int(lb), int(lg), int(lr)), -1)

    cv2.putText(display_frame, "Click anywhere to pick color. Press 'q' to quit.", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow("Color Picker Dropper", display_frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
