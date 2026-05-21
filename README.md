# 🎯 OpenCV & Computer Vision Projects Collection

A comprehensive collection of **50+ interactive computer vision projects** built with OpenCV, MediaPipe, and Python. Each project is self-contained and runs directly from webcam input.

## 🚀 Quick Start

```bash
# Clone and setup
git clone <repo-url>
cd PythonProject

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# Install dependencies
pip install opencv-python opencv-contrib-python mediapipe numpy pyautogui ultralytics matplotlib scipy pillow
```

## 📂 Project Categories

### 🤚 Hand Tracking & Gestures
| File | Description |
|------|-------------|
| `01_pose_detector_game.py` | Pop falling circles using body pose tracking |
| `02_hand_volume_control.py` | Control system volume with thumb-index distance |
| `05_virtual_paint.py` | Air-draw on a digital canvas with hand tracking |
| `19_air_mouse_controller.py` | Control mouse cursor with hand gestures |
| `20_finger_counter.py` | Real-time finger counting display |
| `29_virtual_calculator.py` | Gesture-operated calculator |
| `40_gesture_slide_controller.py` | Navigate presentation slides with gestures |
| `45_hand_zoom_brightness_control.py` | Control zoom and brightness with hand gestures |
| `46_hand_color_filter.py` | Change camera filters using hand fingers |
| `47_hand_camera_lens.py` | Palm lens effect on live webcam feed |
| `48_hand_click_pointer.py` | Control pointer and click with hand gestures |
| `rock.py` | Hand-gesture rock-paper-scissors game |
| `Virtual-Keyboard-with-Hand-Gesture-Control.py` | Full virtual keyboard via hand tracking |

### 👤 Face & Facial Features
| File | Description |
|------|-------------|
| `06_face_mesh_landmarks.py` | Visualize 468 face mesh landmarks |
| `09_drowsiness_detector.py` | Eye-aspect-ratio drowsiness alert system |
| `11_virtual_try_on_sunglasses.py` | AR sunglasses overlay on detected faces |
| `16_delaunay_triangulation.py` | Low-poly face effect via triangulation |
| `22_face_emotion_classifier.py` | Classify facial expressions in real-time |
| `32_automatic_brightness_controller.py` | Auto-adjust display brightness from face lighting |
| `33_face_blurring_privacy.py` | Privacy-preserving automatic face blur |
| `face detection.py` | Basic Haar cascade face detection |
| `Mouse Control using Eye Tracking.py` | Control mouse with eye gaze |

### 🖼️ Image Processing & Filters
| File | Description |
|------|-------------|
| `03_document_scanner.py` | Perspective-warp document scanner |
| `10_color_pop_filter.py` | Isolate one color, desaturate the rest |
| `15_pencil_sketch_generator.py` | Real-time pencil sketch effect |
| `17_image_stitching_panorama.py` | Multi-image panorama stitching |
| `18_watermark_overlay.py` | Transparent watermark overlay tool |
| `24_image_histogram_equalizer.py` | Live histogram equalization with visualization |
| `26_color_picker_dropper.py` | Interactive color picker/eyedropper |
| `27_shape_detector.py` | Contour-based shape classification |
| `31_image_morphology_explorer.py` | Erosion, dilation, opening, closing explorer |
| `36_panoramic_motion_scanner.py` | Slit-scan panoramic capture |
| `edge_detection.py` | Real-time Canny edge detection |

### 🎯 Object Tracking & Detection
| File | Description |
|------|-------------|
| `04_qr_barcode_scanner.py` | Real-time QR code detection and decode |
| `07_optical_flow_tracker.py` | Lucas-Kanade optical flow on clicked points |
| `13_object_size_measurer.py` | Measure real-world object dimensions |
| `25_object_speed_estimator.py` | Estimate moving object velocity |
| `35_ball_physics_simulation.py` | Bouncing ball physics with OpenCV rendering |
| `37_object_tracker_mil_kcf.py` | ROI-based object tracking benchmark |
| `blue color tracker.py` | HSV-based blue color tracking |
| `YOLO Real-Time Webcam Detection.py` | YOLOv8 real-time object detection |
| `Object Counter using YOLO.py` | Count objects with YOLO |

### 🛡️ Real-World Applications & Safety
| File | Description |
|------|-------------|
| `08_background_remover.py` | MediaPipe background replacement |
| `12_lane_line_detector.py` | Hough-transform lane detection |
| `14_motion_security_alarm.py` | Motion-triggered security alarm with logging |
| `21_social_distancing_detector.py` | Person distance violation detector |
| `23_blur_detector_autofocus.py` | Laplacian variance blur detection |
| `28_camera_shake_stabilizer.py` | Video stabilization via feature matching |
| `30_pedestrian_detector.py` | HOG-based pedestrian detection |
| `34_sudoku_grid_extractor.py` | Sudoku grid detection and cell extraction |
| `38_road_pothole_detection_simulation.py` | Pothole detection via contour analysis |
| `39_fire_detection_color_analysis.py` | Fire/flame color-space detection |
| `Harry Potter Invisible Cloak.py` | Invisibility cloak effect |
| `Live Blur Background.py` | Real-time background blur |
| `motion detection.py` | Basic motion detection |

## 🛠️ Tech Stack

- **[OpenCV](https://opencv.org/)** — Image processing, video capture, drawing
- **[MediaPipe](https://mediapipe.dev/)** — Pose, Hands, Face Mesh, Segmentation
- **[PyAutoGUI](https://pyautogui.readthedocs.io/)** — System mouse/keyboard control
- **[Ultralytics YOLOv8](https://ultralytics.com/)** — Object detection
- **[NumPy](https://numpy.org/)** — Array operations

## 📜 License

This project is for educational purposes. Feel free to use and modify.
