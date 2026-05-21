import cv2
import mediapipe as mp
import math

mp_face_mesh = mp.solutions.face_mesh

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh = face_mesh_handler = mp_face_mesh.FaceMesh(max_num_faces=1)
    
    # We will instantiate inside context to prevent leaks
    with mp_face_mesh.FaceMesh(max_num_faces=1) as mesh:
        results = mesh.process(rgb)

    emotion = "NEUTRAL"
    color = (0, 255, 0)

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark

        # Extract coordinates of key nodes
        # Mouth corners: Left 61, Right 291
        # Upper lip: 13, Lower lip: 14
        # Eyebrows: Left 70, Right 300
        # Forehead center/nose tip for normalization: 168 (nose bridge), 1 (nose tip)
        
        m_left = (landmarks[61].x * w, landmarks[61].y * h)
        m_right = (landmarks[291].x * w, landmarks[291].y * h)
        lip_top = (landmarks[13].x * w, landmarks[13].y * h)
        lip_bottom = (landmarks[14].x * w, landmarks[14].y * h)
        
        # Calculate mouth width and opening height
        mouth_width = math.hypot(m_right[0] - m_left[0], m_right[1] - m_left[1])
        mouth_height = math.hypot(lip_bottom[0] - lip_top[0], lip_bottom[1] - lip_top[1])
        
        # Ratio of mouth height to width
        mouth_ratio = mouth_height / (mouth_width + 1e-6)

        # Eyebrows: left eyebrow center (107) to left eye center (159)
        # right eyebrow center (336) to right eye center (386)
        eb_left = (landmarks[107].x * w, landmarks[107].y * h)
        e_left = (landmarks[159].x * w, landmarks[159].y * h)
        eb_dist = math.hypot(eb_left[0] - e_left[0], eb_left[1] - e_left[1])

        # Smile detection: check curvature of the lip corners compared to lip center
        # Average lip center height
        lip_center_y = (lip_top[1] + lip_bottom[1]) / 2.0
        corners_avg_y = (m_left[1] + m_right[1]) / 2.0
        
        # In BGR coordinates, lower y is higher on screen.
        # If lip corners are higher (lower y value) than the center, it's a smile!
        smile_metric = lip_center_y - corners_avg_y

        # Define thresholds for classification
        if mouth_ratio > 0.45:
            emotion = "SURPRISED"
            color = (0, 255, 255) # Yellow
        elif smile_metric > 3.0:
            emotion = "SMILING"
            color = (255, 0, 255) # Magenta
        elif eb_dist < 18:
            emotion = "FOCUSED / FROWN"
            color = (0, 0, 255) # Red
        else:
            emotion = "NEUTRAL"
            color = (0, 255, 0) # Green

        # Draw critical facial circles
        for pt in [m_left, m_right, lip_top, lip_bottom]:
            cv2.circle(frame, (int(pt[0]), int(pt[1])), 4, color, -1)

    cv2.putText(frame, f"Emotion: {emotion}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
    cv2.imshow("Face Emotion Classifier", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
