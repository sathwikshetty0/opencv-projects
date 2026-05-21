import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Available ASCII character sets (dark to light)
ASCII_CHARS_DETAILED = "@%#*+=-:. "
ASCII_CHARS_SIMPLE = "@#$%&*o+=-. "

# Settings
ascii_width = 120
font_scale = 0.3
char_set = ASCII_CHARS_DETAILED

print("ASCII Webcam - Press 'q' to quit, 's' to switch charset, '+'/'-' to resize")

use_detailed = True

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate aspect ratio for ASCII
    aspect_ratio = h / w
    ascii_height = int(ascii_width * aspect_ratio * 0.5)

    # Resize for ASCII conversion
    small = cv2.resize(gray, (ascii_width, ascii_height))

    # Create black canvas for ASCII art
    canvas_h = int(ascii_height * 12)
    canvas_w = int(ascii_width * 7)
    canvas = np.zeros((canvas_h, canvas_w, 3), dtype=np.uint8)

    # Convert pixels to ASCII characters
    for row_idx in range(ascii_height):
        for col_idx in range(ascii_width):
            pixel = small[row_idx, col_idx]
            char_idx = int(pixel / 255 * (len(char_set) - 1))
            char = char_set[char_idx]

            # Color from original frame
            orig_y = int(row_idx / ascii_height * h)
            orig_x = int(col_idx / ascii_width * w)
            b, g, r = frame[orig_y, orig_x]

            x_pos = col_idx * 7
            y_pos = row_idx * 12 + 10

            cv2.putText(canvas, char, (x_pos, y_pos),
                        cv2.FONT_HERSHEY_SIMPLEX, font_scale,
                        (int(b), int(g), int(r)), 1)

    # Display
    display = cv2.resize(canvas, (640, 480))
    cv2.putText(display, f"ASCII Art | Cols: {ascii_width}", (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 1)

    cv2.imshow("ASCII Webcam", display)
    cv2.imshow("Original", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        use_detailed = not use_detailed
        char_set = ASCII_CHARS_DETAILED if use_detailed else ASCII_CHARS_SIMPLE
        print(f"Charset: {'detailed' if use_detailed else 'simple'}")
    elif key == ord('+') or key == ord('='):
        ascii_width = min(ascii_width + 10, 200)
        print(f"Width: {ascii_width}")
    elif key == ord('-'):
        ascii_width = max(ascii_width - 10, 40)
        print(f"Width: {ascii_width}")

cap.release()
cv2.destroyAllWindows()
