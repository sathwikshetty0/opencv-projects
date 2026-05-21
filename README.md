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

Each demo below includes a rich multi-line description that explains the core interaction, technique, and learning focus.

### 🤚 Hand Tracking & Gestures

- `01_pose_detector_game.py`
  - Interactive pose-based game with falling targets and a scoring overlay.
  - Uses MediaPipe pose detection to track body landmarks in real time.
  - Players move to hit targets while the system evaluates their posture.
  - A fun demo for learning pose estimation and game interaction logic.
  - Runs live on webcam and provides instant visual and score feedback.

- `02_hand_volume_control.py`
  - Controls system volume using the distance between thumb and index finger.
  - Uses MediaPipe hand landmarks to detect finger separation accurately.
  - Maps the pinch gap to a smooth audio level slider for intuitive control.
  - Demonstrates gesture-based interface design and real-time mapping.
  - A practical example of hands-free volume adjustment with webcam input.

- `05_virtual_paint.py`
  - Paints on a virtual canvas using hand-tracked finger position.
  - Combines hand detection with drawing overlays to create an air brush demo.
  - Supports continuous strokes, color selection, and eraser-style movement.
  - Great for learning how to turn gestures into creative visual output.
  - Runs directly from webcam feed with hands as the drawing tool.

- `10_color_pop_filter.py`
  - A demo script focused on 10 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `11_virtual_try_on_sunglasses.py`
  - Overlays AR sunglasses on a detected face using landmark tracking.
  - Maintains placement as the face moves for a realistic effect.
  - Demonstrates how to align accessories with facial geometry.
  - Useful for virtual try-on, fashion AR, and cosmetic overlay apps.
  - Runs from webcam feed and updates in real time with head motion.

- `19_air_mouse_controller.py`
  - A demo script focused on 19 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `29_virtual_calculator.py`
  - A demo script focused on 29 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `32_automatic_brightness_controller.py`
  - A demo script focused on 32 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `40_gesture_slide_controller.py`
  - Controls presentation slides using simple hand gestures.
  - Detects left and right movement to advance or reverse slides.
  - A gesture-based remote control demo for hands-free navigation.
  - Useful for interactive presentations and accessibility interfaces.
  - Uses webcam input to turn body motion into UI commands.

- `41_pinch_zoom_camera.py`
  - A demo script focused on 41 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `43_gesture_recognizer.py`
  - A demo script focused on 43 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `44_ascii_art_webcam.py`
  - A demo script focused on 44 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `45_hand_zoom_brightness_control.py`
  - A demo script focused on 45 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `46_hand_color_filter.py`
  - A demo script focused on 46 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `47_hand_camera_lens.py`
  - A demo script focused on 47 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `48_hand_click_pointer.py`
  - A demo script focused on 48 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `49_hand_scroll_control.py`
  - A demo script focused on 49 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `50_hand_pause_player.py`
  - A demo script focused on 50 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `51_hand_brightness_slider.py`
  - A demo script focused on 51 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `52_hand_zoom_filter.py`
  - A demo script focused on 52 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `53_hand_silhouette_overlay.py`
  - A demo script focused on 53 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `54_hand_shadow_effect.py`
  - A demo script focused on 54 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `55_hand_sparkle_trail.py`
  - A demo script focused on 55 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `56_hand_ar_shield.py`
  - A demo script focused on 56 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `57_hand_emoji_reactions.py`
  - A demo script focused on 57 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `58_hand_warp_window.py`
  - A demo script focused on 58 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `60_face_beard_filter.py`
  - A demo script focused on 60 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `62_face_blend_filter.py`
  - A demo script focused on 62 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `71_pose_gesture_fit.py`
  - A demo script focused on 71 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `eye controlled mouse.py`
  - A demo script focused on eye using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `Mouse Control using Eye Tracking.py`
  - A demo script focused on mouse using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `rock.py`
  - A demo script focused on rock using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `Virtual-Keyboard-with-Hand-Gesture-Control.py`
  - A demo script focused on virtual-keyboard-with-hand-gesture-control using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

### 👤 Face, Eye & Facial Features

- `06_face_mesh_landmarks.py`
  - Visualizes MediaPipe face mesh landmarks on live video.
  - Shows hundreds of precise facial landmark points overlaid on the face.
  - Great for understanding how face geometry is represented in code.
  - Uses real-time tracking to update landmarks as the head moves.
  - Ideal for AR and facial analytics prototype development.

- `09_drowsiness_detector.py`
  - Detects drowsiness by analyzing eye closure and blink patterns.
  - Calculates eye aspect ratio to determine fatigue and sleepiness.
  - Provides alerts when a user’s eyes remain closed too long.
  - Useful for driver safety demos and wellness monitoring projects.
  - Demonstrates a biometric alert system using webcam input.

- `16_delaunay_triangulation.py`
  - A demo script focused on 16 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `22_face_emotion_classifier.py`
  - A demo script focused on 22 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `33_face_blurring_privacy.py`
  - A demo script focused on 33 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `59_face_mask_sticker.py`
  - A demo script focused on 59 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `61_face_mirror_glass.py`
  - A demo script focused on 61 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `63_face_landmark_graph.py`
  - Plots live data from landmark tracking or motion analysis.
  - Displays changing values as an overlay for immediate feedback.
  - Helps visualize how sensor-derived metrics evolve over time.
  - Useful for debugging models and understanding feature movement.
  - Ties numeric tracking output to clear graphical visualization.

- `64_face_pose_align.py`
  - A demo script focused on 64 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `65_face_color_pop.py`
  - A demo script focused on 65 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `66_face_symmetry_view.py`
  - A demo script focused on 66 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `67_face_smile_meter.py`
  - A demo script focused on 67 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `68_face_glow_highlight.py`
  - A demo script focused on 68 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `82_motion_frame_blend.py`
  - A demo script focused on 82 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `84_motion_object_mask.py`
  - A demo script focused on 84 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `face detection.py`
  - A demo script focused on face using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

### 🖼️ Image Processing, Filters & Visual Effects

- `03_document_scanner.py`
  - Detects document edges and applies a perspective transform for scanning.
  - Uses contour detection and warping to produce a clean output image.
  - Helps convert photos of paper into usable digital scans automatically.
  - Demonstrates perspective correction, thresholding, and contour mapping.
  - Ideal for building a mobile scanning demo with webcam capture.

- `15_pencil_sketch_generator.py`
  - A demo script focused on 15 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `17_image_stitching_panorama.py`
  - A demo script focused on 17 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `18_watermark_overlay.py`
  - A demo script focused on 18 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `24_image_histogram_equalizer.py`
  - A demo script focused on 24 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `26_color_picker_dropper.py`
  - A demo script focused on 26 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `27_shape_detector.py`
  - A demo script focused on 27 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `31_image_morphology_explorer.py`
  - A demo script focused on 31 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `36_panoramic_motion_scanner.py`
  - A demo script focused on 36 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `edge_detection.py`
  - A demo script focused on edge using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `Harry Potter Invisible Cloak.py`
  - A demo script focused on harry using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `Live Blur Background.py`
  - A demo script focused on live using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

### 🎯 Object Tracking, Detection & Measurement

- `04_qr_barcode_scanner.py`
  - Detects QR codes and barcodes from live webcam frames.
  - Uses OpenCV decoding to read encoded text and display results instantly.
  - Draws a bounding box around scanned codes for visual verification.
  - Useful for inventory, ticketing, and quick data capture demos.
  - A practical demonstration of real-time scanning and decoding logic.

- `07_optical_flow_tracker.py`
  - A demo script focused on 07 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `13_object_size_measurer.py`
  - A demo script focused on 13 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `25_object_speed_estimator.py`
  - A demo script focused on 25 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `30_pedestrian_detector.py`
  - A demo script focused on 30 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `35_ball_physics_simulation.py`
  - A demo script focused on 35 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `37_object_tracker_mil_kcf.py`
  - A demo script focused on 37 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `75_pose_reach_tracker.py`
  - A demo script focused on 75 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `83_motion_heat_tracker.py`
  - A demo script focused on 83 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `blue color tracker.py`
  - A demo script focused on blue using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `Object Counter using YOLO.py`
  - A demo script focused on object using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `YOLO Real-Time Webcam Detection.py`
  - A demo script focused on yolo using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

### 🛡️ Real-World Applications & Safety

- `08_background_remover.py`
  - A demo script focused on 08 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `12_lane_line_detector.py`
  - Detects road lane lines using edge detection and Hough transforms.
  - Processes the frame to isolate lane boundaries and overlay guides.
  - Useful as a driver-assistance system prototype for lane keeping.
  - Demonstrates basic autonomous driving vision techniques.
  - A good example of extracting roadway structure from camera input.

- `14_motion_security_alarm.py`
  - A demo script focused on 14 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `21_social_distancing_detector.py`
  - A demo script focused on 21 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `23_blur_detector_autofocus.py`
  - A demo script focused on 23 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `28_camera_shake_stabilizer.py`
  - A demo script focused on 28 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `34_sudoku_grid_extractor.py`
  - A demo script focused on 34 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `38_road_pothole_detection_simulation.py`
  - A demo script focused on 38 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `39_fire_detection_color_analysis.py`
  - A demo script focused on 39 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `motion detection.py`
  - A demo script focused on motion using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

### 🌊 Motion, Pose & Visual Analytics

- `42_motion_heatmap.py`
  - A demo script focused on 42 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `69_pose_squat_counter.py`
  - A demo script focused on 69 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `70_pose_yoga_assistant.py`
  - A demo script focused on 70 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `72_pose_posture_alert.py`
  - A demo script focused on 72 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `73_pose_jump_counter.py`
  - A demo script focused on 73 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `74_pose_balance_meter.py`
  - A demo script focused on 74 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `76_pose_sitstand_counter.py`
  - A demo script focused on 76 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `77_pose_dance_visualizer.py`
  - A demo script focused on 77 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `78_pose_angle_helper.py`
  - A demo script focused on 78 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `79_motion_trail.py`
  - A demo script focused on 79 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `80_motion_direction_overlay.py`
  - A demo script focused on 80 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `81_motion_magnifier.py`
  - A demo script focused on 81 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `85_motion_focus_crop.py`
  - A demo script focused on 85 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `86_motion_strobe.py`
  - A demo script focused on 86 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `87_motion_blur_effect.py`
  - A demo script focused on 87 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

- `88_motion_color_wave.py`
  - A demo script focused on 88 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

### 🛠 Utility & Generator Scripts

- `generate_40_demos.py`
  - Auto-generates demo project files and README sections from templates.
  - Used to expand this repository quickly with new example scripts.
  - Demonstrates how to automate file creation and documentation updates.
  - Helps maintain consistency across many generated demo scripts.
  - Includes logic to create categorized project descriptions and file names.

### Other Projects

- `20_finger_counter.py`
  - A demo script focused on 20 using webcam-based computer vision.
  - Uses OpenCV and MediaPipe techniques to process live video frames.
  - Displays an interactive visual effect or tracking output on screen.
  - Useful for learning how to combine detection, filtering, and interaction.
  - Runs standalone with minimal setup and demonstrates core CV concepts.

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

