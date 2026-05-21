# 🚀 OpenCV & MediaPipe Computer Vision Demo Collection

A complete interactive repository of **80+ computer vision demos** built with Python, OpenCV, MediaPipe, and related tools.

These projects are designed for learning, experimentation, and rapid prototyping. Every script is self-contained and runs directly with webcam input or video capture.

---

## 📌 What’s Included

- Hand tracking and gesture control demos
- Face landmark and AR filter experiences
- Image processing, filtering, and style effects
- Object tracking, object detection, and motion analytics
- Real-world safety and utility applications
- 40+ additional demos for pose, motion, and live visual effects

---

## ✅ Highlights

- **Full webcam-based demos** with minimal setup
- **MediaPipe hand, face, pose, and segmentation** integrations
- **Real-time control** through gestures and visual cues
- **Educational examples** for vision-based UI, AR, and analytics

---

## 🧰 Requirements

- Python 3.8+
- Webcam or video input device
- Installed packages:
  - `opencv-python`
  - `opencv-contrib-python`
  - `mediapipe`
  - `numpy`
  - `pyautogui`
  - `matplotlib`
  - `scipy`
  - `pillow`
  - `ultralytics` (for YOLO projects)

> If you want to keep installs lightweight, only install the packages needed for the demo you run.

---

## ⚙ Setup

```powershell
cd C:\projects\PythonProject
python -m venv .venv
.venv\Scripts\activate
pip install opencv-python opencv-contrib-python mediapipe numpy pyautogui matplotlib scipy pillow ultralytics
```

---

## ▶️ Running a Demo

Use Python to run any script by name.

Example:

```powershell
python 05_virtual_paint.py
```

If a script uses MediaPipe or camera input, allow the webcam access and close it with `q`.

---

## 🗂️ Project Categories

Each demo includes a short description, the main computer vision technique used, and the core interaction or visual effect it demonstrates.

### 🤚 Hand Tracking & Gestures
- `01_pose_detector_game.py` — interactive pose game that uses body landmarks to hit falling targets and keep score.
- `02_hand_volume_control.py` — control system volume by adjusting the distance between thumb and index finger with hand tracking.
- `05_virtual_paint.py` — draw in the air on a digital canvas using finger position and real-time hand detection.
- `19_air_mouse_controller.py` — move the mouse cursor with hand gestures and simple landmark tracking.
- `20_finger_counter.py` — count how many fingers are raised using hand landmark classification.
- `29_virtual_calculator.py` — operate a gesture-driven calculator layout without touching the keyboard.
- `40_gesture_slide_controller.py` — navigate presentation slides using directional hand gestures.
- `41_pinch_zoom_camera.py` — zoom into the camera feed with pinch gestures and smooth scaling.
- `43_gesture_recognizer.py` — recognize basic hand gestures and display the detected pose label.
- `44_ascii_art_webcam.py` — convert live webcam feed into stylized ASCII art using image quantization.
- `45_hand_zoom_brightness_control.py` — pinch to zoom and move your hand vertically to adjust brightness live.
- `46_hand_color_filter.py` — change the video filter by showing different finger combinations.
- `47_hand_camera_lens.py` — apply a palm-shaped lens distortion effect to the webcam feed.
- `48_hand_click_pointer.py` — simulate mouse clicks and pointer movement using hand gestures.
- `49_hand_scroll_control.py` — scroll content with wrist tilt and hand position in the frame.
- `50_hand_pause_player.py` — pause or resume media playback using open-palm and closed-fist gestures.
- `51_hand_brightness_slider.py` — adjust brightness using finger height as a virtual slider.
- `52_hand_zoom_filter.py` — combine pinch zoom with live filter effects on the video feed.
- `53_hand_silhouette_overlay.py` — create a hand silhouette overlay from detected hand contours.
- `54_hand_shadow_effect.py` — render a dynamic shadow effect beneath the tracked hand.
- `55_hand_sparkle_trail.py` — leave a sparkling trail behind the index finger while moving.
- `56_hand_ar_shield.py` — display an AR shield graphic around the palm when both hands are detected.
- `57_hand_emoji_reactions.py` — show emoji reactions based on simple hand pose states.
- `58_hand_warp_window.py` — warp a circular window around the hand and distort the area inside.
- `rock.py` — play rock-paper-scissors against the camera using hand pose classification.
- `Virtual-Keyboard-with-Hand-Gesture-Control.py` — type with a virtual keyboard by pointing and selecting keys with hand gestures.

### 👤 Face, Eye & Facial Features
- `06_face_mesh_landmarks.py` — display MediaPipe face mesh landmarks and coordinate overlays.
- `09_drowsiness_detector.py` — monitor eye aspect ratio to detect drooping eyes and warn of drowsiness.
- `11_virtual_try_on_sunglasses.py` — overlay AR sunglasses on a detected face with landmark alignment.
- `16_delaunay_triangulation.py` — stylize a face using Delaunay triangulation on facial landmarks.
- `22_face_emotion_classifier.py` — classify basic facial expressions and label emotions in real time.
- `32_automatic_brightness_controller.py` — adjust screen brightness based on the detected lighting around the face.
- `33_face_blurring_privacy.py` — blur faces for privacy while keeping the rest of the video clear.
- `59_face_mask_sticker.py` — apply a virtual mask sticker over the nose and mouth area.
- `60_face_beard_filter.py` — add a beard filter to the lower face using facial landmark positioning.
- `61_face_mirror_glass.py` — mirror the face into stylized sunglasses for a fun AR look.
- `62_face_blend_filter.py` — blend two filter effects across the nose bridge using face landmarks.
- `63_face_landmark_graph.py` — plot selected facial landmark values as a live graph overlay.
- `64_face_pose_align.py` — display pose axes and alignment guides for the head orientation.
- `65_face_color_pop.py` — keep one facial color while desaturating the rest for dramatic effect.
- `66_face_symmetry_view.py` — compare left and right facial symmetry in a split-screen view.
- `67_face_smile_meter.py` — measure smile intensity and display a live score meter.
- `68_face_glow_highlight.py` — highlight cheeks and forehead with a glowing visual effect.
- `face detection.py` — classic Haar cascade face detection for simple webcam demos.
- `eye controlled mouse.py` — move the mouse pointer using detected eye gaze or eye landmarks.
- `Mouse Control using Eye Tracking.py` — alternate eye-tracking script for gaze-based cursor control.

### 🖼️ Image Processing, Filters & Visual Effects
- `03_document_scanner.py` — detect document edges and apply a perspective warp for scanning.
- `10_color_pop_filter.py` — isolate one color and desaturate the rest for a pop effect.
- `15_pencil_sketch_generator.py` — convert video frames into a pencil sketch style.
- `17_image_stitching_panorama.py` — stitch multiple images into a panorama using feature matching.
- `18_watermark_overlay.py` — overlay a transparent watermark on live video frames.
- `24_image_histogram_equalizer.py` — apply histogram equalization to balance brightness across the frame.
- `26_color_picker_dropper.py` — pick colors from the video feed and display RGB values.
- `27_shape_detector.py` — detect and label basic geometric shapes from contours.
- `31_image_morphology_explorer.py` — experiment with erosion, dilation, opening, and closing filters.
- `36_panoramic_motion_scanner.py` — create a slit-scan panoramic motion capture effect.
- `44_ascii_art_webcam.py` — render the webcam feed in real-time ASCII art.
- `edge_detection.py` — detect edges in each frame with Canny edge detection.
- `Live Blur Background.py` — blur the background while keeping the subject in focus.
- `Harry Potter Invisible Cloak.py` — simulate invisibility by masking a selected color range.

### 🎯 Object Tracking, Detection & Measurement
- `04_qr_barcode_scanner.py` — detect and decode QR codes and barcodes from the webcam.
- `07_optical_flow_tracker.py` — track motion of selected points using Lucas-Kanade optical flow.
- `13_object_size_measurer.py` — estimate object size in real-world units using contour calibration.
- `25_object_speed_estimator.py` — compute object speed by tracking movement between frames.
- `30_pedestrian_detector.py` — detect people with HOG-based pedestrian detection.
- `35_ball_physics_simulation.py` — simulate a bouncing ball with collision and vector motion.
- `37_object_tracker_mil_kcf.py` — compare MIL/KCF object tracking using an ROI selection.
- `blue color tracker.py` — follow a blue object using HSV color segmentation.
- `YOLO Real-Time Webcam Detection.py` — run YOLOv8 object detection on webcam video.
- `Object Counter using YOLO.py` — count detected objects from YOLO output.

### 🛡️ Real-World Applications & Safety
- `08_background_remover.py` — remove or replace the webcam background using MediaPipe segmentation.
- `12_lane_line_detector.py` — detect road lanes using edge detection and Hough transforms.
- `14_motion_security_alarm.py` — trigger an alarm and log events when motion is detected.
- `21_social_distancing_detector.py` — estimate distance between people and highlight violations.
- `23_blur_detector_autofocus.py` — detect blur in video frames and identify out-of-focus camera output.
- `28_camera_shake_stabilizer.py` — stabilize video by compensating for camera shake.
- `34_sudoku_grid_extractor.py` — detect and extract a Sudoku grid from the camera view.
- `38_road_pothole_detection_simulation.py` — simulate pothole detection using contour and color analysis.
- `39_fire_detection_color_analysis.py` — detect fire-like color regions for flame analysis.
- `motion detection.py` — basic motion detection demo with alert-style output.

### 🌊 Motion, Pose & Visual Analytics
- `69_pose_squat_counter.py` — count squats using lower-body pose estimation.
- `70_pose_yoga_assistant.py` — assist yoga poses with joint angle feedback.
- `71_pose_gesture_fit.py` — recognize simple full-body pose gestures.
- `72_pose_posture_alert.py` — warn when posture drifts from a healthy alignment.
- `73_pose_jump_counter.py` — detect and count vertical jumps from pose motion.
- `74_pose_balance_meter.py` — estimate balance from hip and shoulder alignment.
- `75_pose_reach_tracker.py` — measure arm reach distance in real time.
- `76_pose_sitstand_counter.py` — count sit-to-stand transitions using pose landmarks.
- `77_pose_dance_visualizer.py` — render a dance-style skeleton overlay on motion.
- `78_pose_angle_helper.py` — draw joint angle helpers for pose analysis.
- `79_motion_trail.py` — draw a motion trail behind moving objects.
- `80_motion_direction_overlay.py` — overlay arrows showing motion direction.
- `81_motion_magnifier.py` — magnify moving regions for emphasis.
- `82_motion_frame_blend.py` — blend recent frames to create ghosting motion effects.
- `83_motion_heat_tracker.py` — display motion hotspots as a heatmap.
- `84_motion_object_mask.py` — isolate moving objects with a mask.
- `85_motion_focus_crop.py` — crop the view around the most active motion area.
- `86_motion_strobe.py` — apply a strobe-style motion visualization.
- `87_motion_blur_effect.py` — add directional motion blur to moving regions.
- `88_motion_color_wave.py` — create a colored wave effect following motion.
- `42_motion_heatmap.py` — generate a heatmap overlay from motion intensity.

### 🛠 Utility & Generator Scripts
- `generate_40_demos.py` — script used to generate additional demo files and README entries programmatically.

---

## 💡 Tips

- Start with the smaller demos like `20_finger_counter.py` or `05_virtual_paint.py`.
- Use `q` to quit each running demo window.
- If you encounter camera issues, verify the webcam is not in use and the correct index is selected.
- Install packages inside `.venv` to avoid system-wide conflicts.

---

## 🛠 Contribution

This repository is a great base for extending computer vision demos.

To add a new demo:

1. Create a new Python script in the root folder.
2. Keep each demo self-contained and simple.
3. Document it in this README.

---

## 📜 License

This repository is intended for learning and experimentation. Feel free to reuse and modify the code for education and prototyping.

