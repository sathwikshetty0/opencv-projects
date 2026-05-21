import cv2
import numpy as np

# Global variables for user clicks
clicked_points = []

def select_point(event, x, y, flags, param):
    global clicked_points
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))
        print(f"Added point to track: ({x}, {y})")

cap = cv2.VideoCapture(0)
cv2.namedWindow("Optical Flow Tracker")
cv2.setMouseCallback("Optical Flow Tracker", select_point)

# Parameters for Lucas-Kanade optical flow
lk_params = dict(
    winSize=(15, 15),
    maxLevel=2,
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
)

# Parameters for ShiTomasi corner detection
feature_params = dict(
    maxCorners=100,
    qualityLevel=0.3,
    minDistance=7,
    blockSize=7
)

# Take first frame and find corners
ret, old_frame = cap.read()
if ret:
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
    # Create a mask image for drawing tracks
    mask = np.zeros_like(old_frame)
else:
    p0 = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # If the user clicked new points, add them to p0
    if len(clicked_points) > 0:
        new_pts = np.array(clicked_points, dtype=np.float32).reshape(-1, 1, 2)
        if p0 is not None:
            p0 = np.vstack((p0, new_pts))
        else:
            p0 = new_pts
        clicked_points.clear()

    if p0 is not None and len(p0) > 0:
        # Calculate optical flow
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

        # Select good points
        if p1 is not None:
            good_new = p1[st == 1]
            good_old = p0[st == 1]

            # Draw tracks
            for i, (new, old) in enumerate(zip(good_new, good_old)):
                a, b = new.ravel()
                c, d = old.ravel()
                mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), (0, 255, 255), 2)
                frame = cv2.circle(frame, (int(a), int(b)), 5, (0, 0, 255), -1)

            img = cv2.add(frame, mask)
            # Update the previous frame and previous points
            p0 = good_new.reshape(-1, 1, 2)
        else:
            img = frame
            p0 = None
    else:
        img = frame

    old_gray = frame_gray.copy()

    # Clear track mask if key 'c' is pressed
    key = cv2.waitKey(1)
    if key == ord('c'):
        mask = np.zeros_like(frame)
        # Re-detect automatic corners
        p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
    elif key == ord('q'):
        break

    # Instructions
    cv2.putText(img, "Click screen to add tracking point. Press 'c' to clear tracks.", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.imshow("Optical Flow Tracker", img)

cap.release()
cv2.destroyAllWindows()
