import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Parameters for ShiTomasi corner detection
feature_params = dict(
    maxCorners=200,
    qualityLevel=0.01,
    minDistance=30,
    blockSize=3
)

# Parameters for Lucas-Kanade optical flow
lk_params = dict(
    winSize=(15, 15),
    maxLevel=2,
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)
)

ret, prev_frame = cap.read()
if ret:
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
else:
    prev_gray = None

# Running average translation offsets
tx_avg, ty_avg = 0.0, 0.0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    stabilized_frame = frame.copy()

    if prev_gray is not None:
        # Detect corners in previous frame
        p0 = cv2.goodFeaturesToTrack(prev_gray, mask=None, **feature_params)
        
        if p0 is not None and len(p0) > 5:
            # Calculate optical flow to find match points in current frame
            p1, st, err = cv2.calcOpticalFlowPyrLK(prev_gray, gray, p0, None, **lk_params)
            
            # Select good matched points
            good_prev = p0[st == 1]
            good_curr = p1[st == 1]
            
            if len(good_prev) > 5:
                # Estimate translation/rotation transformation matrix
                # estimateAffinePartial2D accounts for translation, rotation, and scaling (rigid transform)
                matrix, inliers = cv2.estimateAffinePartial2D(good_curr, good_prev)
                
                if matrix is not None:
                    # Apply warp translation to current frame to match previous frame
                    h, w, _ = frame.shape
                    stabilized_frame = cv2.warpAffine(frame, matrix, (w, h))

    prev_gray = gray.copy()

    # Draw side-by-side comparison
    # Resize frames to fit together
    h, w, _ = frame.shape
    half_w = w // 2
    half_h = h // 2
    
    view_orig = cv2.resize(frame, (half_w, half_h))
    view_stab = cv2.resize(stabilized_frame, (half_w, half_h))
    
    cv2.putText(view_orig, "Original Feed", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(view_stab, "Stabilized Feed", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    comparison = np.hstack((view_orig, view_stab))

    cv2.putText(comparison, "Stabilization Active. Press 'q' to quit.", (10, comparison.shape[0] - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    cv2.imshow("Camera Shake Stabilizer", comparison)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
