import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Track variance history for plotting a graph
history_len = 150
var_history = [0] * history_len
threshold = 80.0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate Laplacian variance
    variance = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Append to history
    var_history.pop(0)
    var_history.append(variance)

    # Determine focus status
    is_blurry = variance < threshold
    status_text = "FOCUS: OK" if not is_blurry else "FOCUS: BLURRY"
    status_color = (0, 255, 0) if not is_blurry else (0, 0, 255)

    # Draw live alert banner
    cv2.rectangle(frame, (0, 0), (w, 50), (40, 40, 40), -1)
    cv2.putText(frame, f"{status_text} (Score: {int(variance)})", (15, 33),
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, status_color, 2)

    # Draw real-time graph at the bottom of the screen
    # Draw graph background
    graph_h = 100
    graph_w = w
    cv2.rectangle(frame, (0, h - graph_h), (graph_w, h), (0, 0, 0), -1)
    cv2.line(frame, (0, h - int(threshold)), (graph_w, h - int(threshold)), (0, 0, 255), 1) # threshold line

    # Plot lines
    for i in range(1, history_len):
        x1 = int((i - 1) * (graph_w / history_len))
        # Map variance to graph height (cap at 300 for display)
        v1 = min(300.0, var_history[i - 1])
        y1 = h - int(v1 * (graph_h / 300.0))

        x2 = int(i * (graph_w / history_len))
        v2 = min(300.0, var_history[i])
        y2 = h - int(v2 * (graph_h / 300.0))

        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)

    cv2.putText(frame, "Sharpness History (Max: 300)", (10, h - graph_h + 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (200, 200, 200), 1)

    cv2.imshow("Blur Detector / Autofocus Tester", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
