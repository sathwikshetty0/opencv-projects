import cv2
import mediapipe as mp
import numpy as np
import os

mp_self_segmentation = mp.solutions.self_segmentation

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Try to load virtual background image, fallback to solid color
bg_img_path = "BG.png"
if os.path.exists(bg_img_path):
    bg_image = cv2.imread(bg_img_path)
    bg_image = cv2.resize(bg_image, (640, 480))
else:
    bg_image = np.zeros((480, 640, 3), dtype=np.uint8)
    bg_image[:] = (0, 255, 0) # Solid green screen fallback

bg_mode = 0 # 0: virtual image, 1: blurred background, 2: solid green

with mp_self_segmentation.SelfSegmentation(model_selection=1) as segmenter:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        # Process segmentation mask
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = segmenter.process(rgb)

        # Draw segmentation mask
        # results.segmentation_mask contains values from 0.0 to 1.0 (probability of human)
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.45

        # Resize background image to match frame size if it changes
        if bg_image.shape[:2] != (h, w):
            bg_image = cv2.resize(bg_image, (w, h))

        # Setup background based on mode
        if bg_mode == 0:
            current_bg = bg_image
        elif bg_mode == 1:
            current_bg = cv2.GaussianBlur(frame, (55, 55), 0)
        else:
            current_bg = np.zeros_like(frame)
            current_bg[:] = (0, 255, 0) # Green screen

        # Combine frame and background using the condition mask
        output_frame = np.where(condition, frame, current_bg)

        # Handle UI keys
        key = cv2.waitKey(1)
        if key == ord('0'):
            bg_mode = 0
        elif key == ord('1'):
            bg_mode = 1
        elif key == ord('2'):
            bg_mode = 2
        elif key == ord('q'):
            break

        # UI Overlay
        cv2.putText(output_frame, "Mode (0: Img | 1: Blur | 2: Green)", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.imshow("Background Remover/Replacer", output_frame)

cap.release()
cv2.destroyAllWindows()
