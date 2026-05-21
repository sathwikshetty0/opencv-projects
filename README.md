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
- `01_pose_detector_game.py` — Interactive pose-based game with falling targets and a live scoring overlay.
  - Interactive pose-based game with falling targets and a live scoring overlay. Uses MediaPipe pose landmarks to detect body motion and score hits in a playful demo.
- `02_hand_volume_control.py` — Control system volume by adjusting the distance between thumb and index finger.
  - Control system volume by adjusting the distance between thumb and index finger. Provides smooth gesture mapping to audio levels with live feedback.
- `05_virtual_paint.py` — Draw in the air on a virtual canvas using finger position tracked by MediaPipe.
  - Draw in the air on a virtual canvas using finger position tracked by MediaPipe. Supports continuous stroke drawing and gesture-based control for painting.
- `10_color_pop_filter.py` — Keeps one selected color while desaturating the rest of the frame.
  - Keeps one selected color while desaturating the rest of the frame. Creates a color pop effect for dramatic visual emphasis.
- `11_virtual_try_on_sunglasses.py` — Overlays AR sunglasses onto the face with landmark alignment.
  - Overlays AR sunglasses onto the face with landmark alignment. Moves the glasses naturally as the head shifts.
- `19_air_mouse_controller.py` — Moves the mouse cursor with hand gestures and landmark tracking.
  - Moves the mouse cursor with hand gestures and landmark tracking. Maps hand position to screen movement for an air-control demo.
- `29_virtual_calculator.py` — Operates a virtual calculator using gesture selection on a screen layout.
  - Operates a virtual calculator using gesture selection on a screen layout. Detects finger presses to input numbers and operators.
- `32_automatic_brightness_controller.py` — Adjusts brightness automatically from face lighting levels.
  - Adjusts brightness automatically from face lighting levels. Uses detected face regions to guide scene brightness correction.
- `40_gesture_slide_controller.py` — Controls slide navigation with simple hand gestures.
  - Controls slide navigation with simple hand gestures. Detects left and right motion to advance presentation slides.
- `41_pinch_zoom_camera.py` — Zooms in and out of the camera feed using pinch gestures.
  - Zooms in and out of the camera feed using pinch gestures. Adjusts scale smoothly based on thumb and index finger distance.
- `43_gesture_recognizer.py` — Recognizes simple hand gestures and labels the detected pose.
  - Recognizes simple hand gestures and labels the detected pose. Provides instant feedback for gesture-based commands.
- `44_ascii_art_webcam.py` — Converts live webcam video into ASCII art in real time.
  - Converts live webcam video into ASCII art in real time. Creates a stylized text rendering of the scene.
- `45_hand_zoom_brightness_control.py` — Zooms the feed and adjusts brightness using hand gestures.
  - Zooms the feed and adjusts brightness using hand gestures. Uses pinch for zoom and vertical placement for brightness control.
- `46_hand_color_filter.py` — Switches filters by showing different finger combinations.
  - Switches filters by showing different finger combinations. Applies live color effects based on gesture input.
- `47_hand_camera_lens.py` — Applies a palm-shaped lens distortion over the hand area.
  - Applies a palm-shaped lens distortion over the hand area. Creates a fun interactive distortion effect around the palm.
- `48_hand_click_pointer.py` — Simulates mouse clicks and pointer control with hand gestures.
  - Simulates mouse clicks and pointer control with hand gestures. Tracks the hand to perform click interactions without a mouse.
- `49_hand_scroll_control.py` — Scrolls a virtual panel using wrist tilt and hand motion.
  - Scrolls a virtual panel using wrist tilt and hand motion. Maps hand direction to scrolling speed in a demo interface.
- `50_hand_pause_player.py` — Pauses and resumes media playback with palm gestures.
  - Pauses and resumes media playback with palm gestures. Uses open/closed hand poses to control playback states.
- `51_hand_brightness_slider.py` — Adjusts brightness using finger height as a virtual slider.
  - Adjusts brightness using finger height as a virtual slider. Provides a simple gesture-based brightness control demo.
- `52_hand_zoom_filter.py` — Combines pinch zoom with live filter effects on the camera feed.
  - Combines pinch zoom with live filter effects on the camera feed. Lets users interactively magnify and stylize the view.
- `53_hand_silhouette_overlay.py` — Draws a silhouette overlay from detected hand contours.
  - Draws a silhouette overlay from detected hand contours. Creates a stylized shadow shape around the live hand pose.
- `54_hand_shadow_effect.py` — Renders a dynamic shadow effect beneath the hand.
  - Renders a dynamic shadow effect beneath the hand. Uses contour and landmark data to simulate a shadow cast.
- `55_hand_sparkle_trail.py` — Leaves a sparkling trail behind the index finger as it moves.
  - Leaves a sparkling trail behind the index finger as it moves. Provides a magical drawing effect in the live feed.
- `56_hand_ar_shield.py` — Displays an AR shield graphic when both hands are detected.
  - Displays an AR shield graphic when both hands are detected. Visualizes augmented reality overlays around the palm.
- `57_hand_emoji_reactions.py` — Shows emoji reactions based on hand pose states.
  - Shows emoji reactions based on hand pose states. Provides expressive visual feedback for gestures.
- `58_hand_warp_window.py` — Warps a circular window around the hand and distorts its contents.
  - Warps a circular window around the hand and distorts its contents. Creates a dynamic, interactive distortion effect.
- `60_face_beard_filter.py` — Adds a beard filter to the lower face area using landmarks.
  - Adds a beard filter to the lower face area using landmarks. Keeps the effect aligned as the face moves and rotates.
- `62_face_blend_filter.py` — Blends two filter effects across the nose bridge using facial landmarks.
  - Blends two filter effects across the nose bridge using facial landmarks. Creates a split-face fusion effect with live alignment.
- `71_pose_gesture_fit.py` — Recognizes simple full-body pose gestures for fitness activities.
  - Recognizes simple full-body pose gestures for fitness activities. Detects basic exercise and movement patterns.
- `eye controlled mouse.py` — Demo project for Eye Controlled Mouse, showcasing live webcam-based computer vision and real-time interactivity..
  - Demo project for Eye Controlled Mouse, showcasing live webcam-based computer vision and real-time interactivity.
- `Mouse Control using Eye Tracking.py` — Demo project for Mouse Control Using Eye Tracking, showcasing live webcam-based computer vision and real-time interactivity..
  - Demo project for Mouse Control Using Eye Tracking, showcasing live webcam-based computer vision and real-time interactivity.
- `rock.py` — Demo project for Rock, showcasing live webcam-based computer vision and real-time interactivity..
  - Demo project for Rock, showcasing live webcam-based computer vision and real-time interactivity.
- `Virtual-Keyboard-with-Hand-Gesture-Control.py` — Demo project for Virtual Keyboard With Hand Gesture Control, showcasing live webcam-based computer vision and real-time interactivity..
  - Demo project for Virtual Keyboard With Hand Gesture Control, showcasing live webcam-based computer vision and real-time interactivity.

### 👤 Face, Eye & Facial Features
- `06_face_mesh_landmarks.py` — Displays MediaPipe face mesh landmarks on a live video feed with coordinate overlays.
  - Displays MediaPipe face mesh landmarks on a live video feed with coordinate overlays. Ideal for understanding facial landmark detection in real time.
- `09_drowsiness_detector.py` — Monitors eye aspect ratio to detect blinking and drowsiness.
  - Monitors eye aspect ratio to detect blinking and drowsiness. Warns the user when prolonged eye closure suggests fatigue.
- `16_delaunay_triangulation.py` — Stylizes the face with Delaunay triangulation on facial landmarks.
  - Stylizes the face with Delaunay triangulation on facial landmarks. Produces a low-poly visual effect over the detected face.
- `22_face_emotion_classifier.py` — Classifies basic facial expressions and labels emotions.
  - Classifies basic facial expressions and labels emotions. Uses face features to determine live mood categories.
- `33_face_blurring_privacy.py` — Blurs faces to preserve privacy while keeping the rest visible.
  - Blurs faces to preserve privacy while keeping the rest visible. Great for demonstrating privacy-aware computer vision.
- `59_face_mask_sticker.py` — Places a virtual mask sticker over the detected face.
  - Places a virtual mask sticker over the detected face. Uses landmarks to keep the sticker aligned and natural-looking.
- `61_face_mirror_glass.py` — Mirrors the face into stylized sunglasses for a cool AR look.
  - Mirrors the face into stylized sunglasses for a cool AR look. Tracks landmarks to place the mirrored graphic accurately.
- `63_face_landmark_graph.py` — Plots facial landmark changes as a live graph overlay.
  - Plots facial landmark changes as a live graph overlay. Useful for visualizing landmark motion over time.
- `64_face_pose_align.py` — Displays head orientation axes and alignment guides.
  - Displays head orientation axes and alignment guides. Helps visualize face rotation and pose direction in real time.
- `65_face_color_pop.py` — Preserves one facial color while desaturating the rest.
  - Preserves one facial color while desaturating the rest. Creates a dramatic color-highlight effect for the face.
- `66_face_symmetry_view.py` — Shows facial symmetry using a mirrored split-screen view.
  - Shows facial symmetry using a mirrored split-screen view. Highlights asymmetry and alignment differences visually.
- `67_face_smile_meter.py` — Measures smile intensity and displays a live score meter.
  - Measures smile intensity and displays a live score meter. Tracks mouth landmarks to infer smiling strength.
- `68_face_glow_highlight.py` — Highlights cheeks and forehead with a glowing effect.
  - Highlights cheeks and forehead with a glowing effect. Adds a soft beauty-style light effect to the face.
- `82_motion_frame_blend.py` — Blends recent frames together for ghosting motion effects.
  - Blends recent frames together for ghosting motion effects. Shows motion history in a single composite view.
- `84_motion_object_mask.py` — Masks moving objects while keeping the background intact.
  - Masks moving objects while keeping the background intact. Emphasizes motion by isolating active regions.
- `face detection.py` — Demo project for Face Detection, showcasing live webcam-based computer vision and real-time interactivity..
  - Demo project for Face Detection, showcasing live webcam-based computer vision and real-time interactivity.

### 🖼️ Image Processing, Filters & Visual Effects
- `03_document_scanner.py` — Detects document edges and applies a perspective warp for a clean scan.
  - Detects document edges and applies a perspective warp for a clean scan. Corrects skew and highlights the detected page boundaries automatically.
- `15_pencil_sketch_generator.py` — Converts the webcam feed into a stylized pencil sketch.
  - Converts the webcam feed into a stylized pencil sketch. Uses edge detection and blending to create an artistic outline effect.
- `17_image_stitching_panorama.py` — Stitches multiple images into a panorama using feature matching.
  - Stitches multiple images into a panorama using feature matching. Demonstrates classical image stitching techniques in OpenCV.
- `18_watermark_overlay.py` — Overlays a transparent watermark on live video frames.
  - Overlays a transparent watermark on live video frames. Useful for watermarking and branding demos on camera output.
- `24_image_histogram_equalizer.py` — Applies histogram equalization to balance contrast in the frame.
  - Applies histogram equalization to balance contrast in the frame. Enhances image detail in darker or overexposed areas.
- `26_color_picker_dropper.py` — Picks colors from the live feed and shows RGB values.
  - Picks colors from the live feed and shows RGB values. Acts like an eyedropper tool for interactive color sampling.
- `27_shape_detector.py` — Detects and labels geometric shapes from contours.
  - Detects and labels geometric shapes from contours. Identifies triangles, rectangles, circles, and quadrilaterals in the scene.
- `31_image_morphology_explorer.py` — Experiments with erosion, dilation, opening, and closing filters.
  - Experiments with erosion, dilation, opening, and closing filters. Shows how morphological operations alter image structure.
- `36_panoramic_motion_scanner.py` — Creates a slit-scan panoramic effect from frame slices.
  - Creates a slit-scan panoramic effect from frame slices. Builds a motion-based panorama from live video input.
- `edge_detection.py` — Demo project for Edge Detection, showcasing live webcam-based computer vision and real-time interactivity..
  - Demo project for Edge Detection, showcasing live webcam-based computer vision and real-time interactivity.
- `Harry Potter Invisible Cloak.py` — Demo project for Harry Potter Invisible Cloak, showcasing live webcam-based computer vision and real-time interactivity..
  - Demo project for Harry Potter Invisible Cloak, showcasing live webcam-based computer vision and real-time interactivity.
- `Live Blur Background.py` — Demo project for Live Blur Background, showcasing live webcam-based computer vision and real-time interactivity..
  - Demo project for Live Blur Background, showcasing live webcam-based computer vision and real-time interactivity.

### 🎯 Object Tracking, Detection & Measurement
- `04_qr_barcode_scanner.py` — Detects and decodes QR codes and barcodes from a live webcam feed.
  - Detects and decodes QR codes and barcodes from a live webcam feed. Shows decoded results and highlights the scanned region on screen.
- `07_optical_flow_tracker.py` — Tracks motion of selected points using Lucas-Kanade optical flow.
  - Tracks motion of selected points using Lucas-Kanade optical flow. Visualizes point trajectories and motion vectors for live motion analysis.
- `13_object_size_measurer.py` — Estimates object size using contour calibration and known reference points.
  - Estimates object size using contour calibration and known reference points. Shows measurements on the live camera view.
- `25_object_speed_estimator.py` — Estimates object speed by tracking motion between frames.
  - Estimates object speed by tracking motion between frames. Displays velocity values for moving objects in view.
- `30_pedestrian_detector.py` — Detects pedestrians using HOG-based person detection.
  - Detects pedestrians using HOG-based person detection. Draws bounding boxes around people detected in the camera feed.
- `35_ball_physics_simulation.py` — Simulates a bouncing ball with collision and motion physics.
  - Simulates a bouncing ball with collision and motion physics. Displays motion vectors and boundary interactions in 2D.
- `37_object_tracker_mil_kcf.py` — Tracks a user-selected object using MIL/KCF algorithms.
  - Tracks a user-selected object using MIL/KCF algorithms. Compares tracker performance and follows the ROI in real time.
- `75_pose_reach_tracker.py` — Measures arm reach distance in real time with pose landmarks.
  - Measures arm reach distance in real time with pose landmarks. Useful for tracking flexibility and range of motion.
- `83_motion_heat_tracker.py` — Displays motion hotspots as a heatmap overlay.
  - Displays motion hotspots as a heatmap overlay. Highlights the most active areas in the scene.
- `blue color tracker.py` — Demo project for Blue Color Tracker, showcasing live webcam-based computer vision and real-time interactivity..
  - Demo project for Blue Color Tracker, showcasing live webcam-based computer vision and real-time interactivity.
- `Object Counter using YOLO.py` — Demo project for Object Counter Using Yolo, showcasing live webcam-based computer vision and real-time interactivity..
  - Demo project for Object Counter Using Yolo, showcasing live webcam-based computer vision and real-time interactivity.
- `YOLO Real-Time Webcam Detection.py` — Demo project for Yolo Real Time Webcam Detection, showcasing live webcam-based computer vision and real-time interactivity..
  - Demo project for Yolo Real Time Webcam Detection, showcasing live webcam-based computer vision and real-time interactivity.

### 🛡️ Real-World Applications & Safety
- `08_background_remover.py` — Removes or replaces the webcam background using segmentation.
  - Removes or replaces the webcam background using segmentation. Offers a simple green-screen effect for privacy and AR-style scenes.
- `12_lane_line_detector.py` — Detects lane boundaries using edge detection and Hough transform.
  - Detects lane boundaries using edge detection and Hough transform. Demonstrates a prototype driver-assistance scene analysis.
- `14_motion_security_alarm.py` — Triggers an alarm when motion is detected in the scene.
  - Triggers an alarm when motion is detected in the scene. Logs events and highlights moving regions for a basic security demo.
- `21_social_distancing_detector.py` — Estimates distance between people and flags safety violations.
  - Estimates distance between people and flags safety violations. Highlights individuals who are too close in the camera frame.
- `23_blur_detector_autofocus.py` — Detects blur in video frames and identifies out-of-focus scenes.
  - Detects blur in video frames and identifies out-of-focus scenes. Helps illustrate image quality assessment and autofocus needs.
- `28_camera_shake_stabilizer.py` — Stabilizes shaky video by compensating for camera motion.
  - Stabilizes shaky video by compensating for camera motion. Shows a smoothed output with reduced frame jitter.
- `34_sudoku_grid_extractor.py` — Detects a Sudoku grid and extracts its individual cells.
  - Detects a Sudoku grid and extracts its individual cells. Useful for preprocessing images for OCR and puzzle solving.
- `38_road_pothole_detection_simulation.py` — Simulates pothole detection using contours and color analysis.
  - Simulates pothole detection using contours and color analysis. Highlights potential road defects for a safety demo.
- `39_fire_detection_color_analysis.py` — Detects flame-like colors to identify fire regions.
  - Detects flame-like colors to identify fire regions. Uses color segmentation to highlight dangerous red-orange areas.
- `motion detection.py` — Demo project for Motion Detection, showcasing live webcam-based computer vision and real-time interactivity..
  - Demo project for Motion Detection, showcasing live webcam-based computer vision and real-time interactivity.

### 🌊 Motion, Pose & Visual Analytics
- `42_motion_heatmap.py` — Displays a heatmap of motion intensity over time.
  - Displays a heatmap of motion intensity over time. Shows which areas have the most activity in the scene.
- `69_pose_squat_counter.py` — Counts squats using lower-body pose tracking and angle detection.
  - Counts squats using lower-body pose tracking and angle detection. Detects repetitions based on hip and knee movement.
- `70_pose_yoga_assistant.py` — Assists yoga poses with joint angle feedback and guidance.
  - Assists yoga poses with joint angle feedback and guidance. Uses pose landmarks to encourage better alignment.
- `72_pose_posture_alert.py` — Alerts when posture drifts from healthy alignment.
  - Alerts when posture drifts from healthy alignment. Monitors shoulder and spine position to detect slouching.
- `73_pose_jump_counter.py` — Counts vertical jumps using pose motion and height changes.
  - Counts vertical jumps using pose motion and height changes. Detects jump repetitions automatically in the live feed.
- `74_pose_balance_meter.py` — Estimates balance using hip and shoulder alignment.
  - Estimates balance using hip and shoulder alignment. Displays a balance score for body stability assessment.
- `76_pose_sitstand_counter.py` — Counts sit-to-stand transitions using pose landmark changes.
  - Counts sit-to-stand transitions using pose landmark changes. Detects when the user stands up or sits down repeatedly.
- `77_pose_dance_visualizer.py` — Renders a dance-style skeleton overlay over live motion.
  - Renders a dance-style skeleton overlay over live motion. Visualizes body movement with artistic pose effects.
- `78_pose_angle_helper.py` — Draws joint angle helpers to assist pose analysis.
  - Draws joint angle helpers to assist pose analysis. Shows angle measurements for elbows, knees, and shoulders.
- `79_motion_trail.py` — Draws a persistent trail behind moving objects.
  - Draws a persistent trail behind moving objects. Highlights motion paths with a continuous visualization.
- `80_motion_direction_overlay.py` — Overlays arrows indicating motion direction.
  - Overlays arrows indicating motion direction. Makes movement orientation visible for tracked objects.
- `81_motion_magnifier.py` — Magnifies moving regions to emphasize activity.
  - Magnifies moving regions to emphasize activity. Creates a zoomed-in view around detected motion.
- `85_motion_focus_crop.py` — Automatically crops around the most active motion area.
  - Automatically crops around the most active motion area. Centers the view on the region with the highest activity.
- `86_motion_strobe.py` — Applies a strobe-style visual effect to motion frames.
  - Applies a strobe-style visual effect to motion frames. Creates a pulsing motion visualization.
- `87_motion_blur_effect.py` — Adds directional motion blur to moving regions.
  - Adds directional motion blur to moving regions. Emphasizes speed and movement with streaking blur.
- `88_motion_color_wave.py` — Draws a colored wave effect behind moving objects.
  - Draws a colored wave effect behind moving objects. Creates a vibrant motion trail that follows activity.

### 🛠 Utility & Generator Scripts
- `generate_40_demos.py` — Auto-generates demo files and README entries from templates.
  - Auto-generates demo files and README entries from templates. Used to populate the repository with new example projects quickly.

### Other Projects
- `20_finger_counter.py` — Counts raised fingers in real time using hand landmarks.
  - Counts raised fingers in real time using hand landmarks. Displays a live counter and highlights the detected hand pose.

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

