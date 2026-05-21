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

### 🤚 Hand Tracking & Gestures
- `01_pose_detector_game.py` — body pose game with falling targets
- `02_hand_volume_control.py` — volume control using thumb-index distance
- `05_virtual_paint.py` — air drawing on a digital canvas
- `19_air_mouse_controller.py` — mouse cursor control via hand gestures
- `20_finger_counter.py` — count raised fingers in real time
- `29_virtual_calculator.py` — gesture-operated calculator interface
- `40_gesture_slide_controller.py` — slide navigation using hand gestures
- `45_hand_zoom_brightness_control.py` — pinch zoom and brightness control
- `46_hand_color_filter.py` — switch camera filters with fingers
- `47_hand_camera_lens.py` — live palm lens effect overlay
- `48_hand_click_pointer.py` — pointer and click control by hand
- `49_hand_scroll_control.py` — scroll panel with hand tilt
- `50_hand_pause_player.py` — pause/play with palm gestures
- `51_hand_brightness_slider.py` — brightness slider via finger height
- `52_hand_zoom_filter.py` — pinch zoom plus camera filtering
- `53_hand_silhouette_overlay.py` — silhouette overlay from hand pose
- `54_hand_shadow_effect.py` — dynamic hand shadow rendering
- `55_hand_sparkle_trail.py` — sparkle trail behind the index finger
- `56_hand_ar_shield.py` — AR shield effect for the palm
- `57_hand_emoji_reactions.py` — emoji reactions from hand pose
- `58_hand_warp_window.py` — warp window around the hand
- `rock.py` — rock-paper-scissors gesture game
- `Virtual-Keyboard-with-Hand-Gesture-Control.py` — virtual keyboard control

### 👤 Face & Facial Features
- `06_face_mesh_landmarks.py` — face mesh landmark visualization
- `09_drowsiness_detector.py` — eye blink and sleepiness alert
- `11_virtual_try_on_sunglasses.py` — AR sunglasses overlay
- `16_delaunay_triangulation.py` — low-poly face stylization
- `22_face_emotion_classifier.py` — real-time expression detection
- `32_automatic_brightness_controller.py` — auto brightness from face lighting
- `33_face_blurring_privacy.py` — live face privacy blur
- `59_face_mask_sticker.py` — virtual mask overlay
- `60_face_beard_filter.py` — beard filter with face landmarks
- `61_face_mirror_glass.py` — mirrored sunglasses effect
- `62_face_blend_filter.py` — blended face filter effect
- `63_face_landmark_graph.py` — live landmark graph visualization
- `64_face_pose_align.py` — pose axes and alignment guides
- `65_face_color_pop.py` — single-color pop on the face
- `66_face_symmetry_view.py` — symmetry split view
- `67_face_smile_meter.py` — smile intensity meter
- `68_face_glow_highlight.py` — glow highlight on facial areas
- `face detection.py` — classic Haar-based face detection
- `Mouse Control using Eye Tracking.py` — gaze-based mouse control

### 🖼️ Image Processing & Filters
- `03_document_scanner.py` — perspective document scanning
- `10_color_pop_filter.py` — single-color pop filter
- `15_pencil_sketch_generator.py` — pencil sketch effect
- `17_image_stitching_panorama.py` — panorama stitching demo
- `18_watermark_overlay.py` — watermark overlay on video frames
- `24_image_histogram_equalizer.py` — live histogram equalization
- `26_color_picker_dropper.py` — color picker/eyedropper tool
- `27_shape_detector.py` — contour-based shape classification
- `31_image_morphology_explorer.py` — erosion/dilation explorer
- `36_panoramic_motion_scanner.py` — slit-scan motion capture
- `edge_detection.py` — real-time Canny edge detection

### 🎯 Object Tracking & Detection
- `04_qr_barcode_scanner.py` — real-time QR and barcode detection
- `07_optical_flow_tracker.py` — Lucas-Kanade optical flow tracker
- `13_object_size_measurer.py` — real-world object measurement
- `25_object_speed_estimator.py` — object velocity estimation
- `35_ball_physics_simulation.py` — physics and motion rendering
- `37_object_tracker_mil_kcf.py` — ROI tracking benchmark
- `blue color tracker.py` — HSV-based blue object tracking
- `YOLO Real-Time Webcam Detection.py` — YOLOv8 object detection
- `Object Counter using YOLO.py` — counting objects with YOLOv8

### 🛡️ Real-World Applications & Safety
- `08_background_remover.py` — background replacement demo
- `12_lane_line_detector.py` — lane boundary detection
- `14_motion_security_alarm.py` — motion-triggered alarm system
- `21_social_distancing_detector.py` — distance violation detection
- `23_blur_detector_autofocus.py` — blur and autofocus checker
- `28_camera_shake_stabilizer.py` — stabilization from video frames
- `30_pedestrian_detector.py` — HOG pedestrian detection
- `34_sudoku_grid_extractor.py` — sudoku board detection and extraction
- `38_road_pothole_detection_simulation.py` — pothole detection demo
- `39_fire_detection_color_analysis.py` — flame/color fire detection
- `Harry Potter Invisible Cloak.py` — invisibility cloak effect
- `Live Blur Background.py` — webcam background blur
- `motion detection.py` — basic motion detection utility

### 🌊 Motion & Visual Effects
- `79_motion_trail.py` — motion trail rendering
- `80_motion_direction_overlay.py` — motion direction arrows
- `81_motion_magnifier.py` — motion region magnifier
- `82_motion_frame_blend.py` — motion frame blending
- `83_motion_heat_tracker.py` — motion heatmap overlay
- `84_motion_object_mask.py` — moving object masking
- `85_motion_focus_crop.py` — focused motion cropping
- `86_motion_strobe.py` — strobe motion effect
- `87_motion_blur_effect.py` — directional motion blur
- `88_motion_color_wave.py` — color wave motion overlay

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

