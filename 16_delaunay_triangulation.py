import cv2
import mediapipe as mp
import numpy as np

# Check if a point is inside a rectangle
def rect_contains(rect, point):
    if point[0] < rect[0]:
        return False
    elif point[1] < rect[1]:
        return False
    elif point[0] > rect[2]:
        return False
    elif point[1] > rect[3]:
        return False
    return True

# Draw Delaunay triangles
def draw_delaunay(img, subdiv, color):
    triangleList = subdiv.getTriangleList()
    r = (0, 0, img.shape[1], img.shape[0])

    for t in triangleList:
        pt1 = (int(t[0]), int(t[1]))
        pt2 = (int(t[2]), int(t[3]))
        pt3 = (int(t[4]), int(t[5]))

        if rect_contains(r, pt1) and rect_contains(r, pt2) and rect_contains(r, pt3):
            cv2.line(img, pt1, pt2, color, 1, cv2.LINE_AA)
            cv2.line(img, pt2, pt3, color, 1, cv2.LINE_AA)
            cv2.line(img, pt3, pt1, color, 1, cv2.LINE_AA)

cap = cv2.VideoCapture(0)
mp_face_mesh = mp.solutions.face_mesh

with mp_face_mesh.FaceMesh(max_num_faces=1, refine_landmarks=True) as face_mesh:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0].landmark

            # Define bounding box of subdiv2D
            rect = (0, 0, w, h)
            subdiv = cv2.Subdiv2D(rect)

            # Insert a subset of points (e.g. every 3rd point to keep it clean and fast)
            # or all facial border and main contour points
            points = []
            for idx, lm in enumerate(landmarks):
                # Sample landmarks to avoid dense cluster overlap
                if idx % 4 == 0:
                    px, py = int(lm.x * w), int(lm.y * h)
                    points.append((px, py))
                    subdiv.insert((px, py))

            # Draw Delaunay Triangles
            draw_delaunay(frame, subdiv, (0, 255, 255))

            # Draw points
            for pt in points:
                cv2.circle(frame, pt, 2, (0, 0, 255), -1)

        cv2.putText(frame, "Delaunay Triangulation Face Mesh", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.imshow("Delaunay Triangulation", frame)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
