import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Ball physical parameters
bx, by = 320.0, 50.0
vx, vy = 5.0, 0.0
radius = 15
gravity = 0.65
elasticity = 0.82

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Preprocessing: Detect edges in the scene
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 60, 150)
    
    # Physics updates
    vy += gravity
    bx += vx
    by += vy

    # Bounce off boundaries
    if bx - radius < 0:
        bx = radius
        vx = -vx * elasticity
    elif bx + radius > w:
        bx = w - radius
        vx = -vx * elasticity

    if by - radius < 0:
        by = radius
        vy = -vy * elasticity
    elif by + radius > h:
        by = h - radius
        vy = -vy * elasticity
        # Re-kick if ball is rolling slowly at the bottom
        if abs(vy) < 1.5:
            vy = -12.0
            vx = np.random.uniform(-6, 6)

    # Check collisions with real-world Canny edges
    # We sample a few points around the ball periphery
    collision = False
    angles = [0, 45, 90, 135, 180, 225, 270, 315]
    for angle in angles:
        rad = np.deg2rad(angle)
        px = int(bx + radius * np.cos(rad))
        py = int(by + radius * np.sin(rad))
        
        # Verify indices within boundary
        if 0 <= px < w and 0 <= py < h:
            if edges[py, px] == 255:
                # Bounce along the angle direction (simplistic reflection)
                collision = True
                vx = -vx * elasticity - 2 * np.cos(rad)
                vy = -vy * elasticity - 2 * np.sin(rad)
                # Cap velocities to prevent exploding speeds
                vx = np.clip(vx, -15, 15)
                vy = np.clip(vy, -15, 15)
                break
                
    # Draw ball
    cv2.circle(frame, (int(bx), int(by)), radius, (0, 0, 255), -1)
    cv2.circle(frame, (int(bx), int(by)), radius + 2, (255, 255, 255), 2)
    
    # Optionally overlay thin edges in blue so the user sees what the ball is hitting
    edge_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    edge_mask = edges > 0
    frame[edge_mask] = (255, 0, 0) # Draw outlines in blue

    cv2.putText(frame, "Interactive Ball Physics. Ball bounces off edges. 'q' to quit.", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2)
    
    cv2.imshow("Webcam Ball Physics", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
