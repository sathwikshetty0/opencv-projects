from pathlib import Path
import textwrap

root = Path(__file__).resolve().parent
projects = [
    ('49_hand_scroll_control.py', 'Scroll through a virtual panel with hand tilt'),
    ('50_hand_pause_player.py', 'Play/pause media with a palm gesture'),
    ('51_hand_brightness_slider.py', 'Adjust screen brightness by finger height'),
    ('52_hand_zoom_filter.py', 'Zoom and apply a filter using pinch distance'),
    ('53_hand_silhouette_overlay.py', 'Draw a hand silhouette overlay in real time'),
    ('54_hand_shadow_effect.py', 'Render a dynamic shadow from the hand outline'),
    ('55_hand_sparkle_trail.py', 'Leave a sparkling trail behind the index finger'),
    ('56_hand_ar_shield.py', 'Show an AR shield when both palms are visible'),
    ('57_hand_emoji_reactions.py', 'Display emoji reactions from hand pose'),
    ('58_hand_warp_window.py', 'Warp a circular window around your hand'),
    ('59_face_mask_sticker.py', 'Place a virtual mask overlay on detected faces'),
    ('60_face_beard_filter.py', 'Add a beard filter using face landmarks'),
    ('61_face_mirror_glass.py', 'Mirror the face into stylized sunglasses'),
    ('62_face_blend_filter.py', 'Blend two face filters along the nose line'),
    ('63_face_landmark_graph.py', 'Plot face landmark positions as a live graph'),
    ('64_face_pose_align.py', 'Show face pose axes and alignment guides'),
    ('65_face_color_pop.py', 'Pop one facial color while desaturating the rest'),
    ('66_face_symmetry_view.py', 'Visualize facial symmetry with a split view'),
    ('67_face_smile_meter.py', 'Measure smile intensity from mouth landmarks'),
    ('68_face_glow_highlight.py', 'Highlight cheek and forehead with glow effect'),
    ('69_pose_squat_counter.py', 'Count squats using pose landmarks'),
    ('70_pose_yoga_assistant.py', 'Assist yoga poses with angle feedback'),
    ('71_pose_gesture_fit.py', 'Recognize simple pose gestures for fitness'),
    ('72_pose_posture_alert.py', 'Alert on poor sitting posture'),
    ('73_pose_jump_counter.py', 'Count vertical jumps with body pose tracking'),
    ('74_pose_balance_meter.py', 'Display balance score from hip/shoulder alignment'),
    ('75_pose_reach_tracker.py', 'Track arm reach distance in real time'),
    ('76_pose_sitstand_counter.py', 'Count sit-to-stand transitions with pose data'),
    ('77_pose_dance_visualizer.py', 'Render a dance skeleton overlay on motion'),
    ('78_pose_angle_helper.py', 'Draw joint angle helpers for body pose'),
    ('79_motion_trail.py', 'Generate a motion trail behind moving objects'),
    ('80_motion_direction_overlay.py', 'Show motion direction arrows for moving contours'),
    ('81_motion_magnifier.py', 'Magnify motion areas for emphasis'),
    ('82_motion_frame_blend.py', 'Blend recent frames to create motion trails'),
    ('83_motion_heat_tracker.py', 'Track motion hotspots with a heatmap overlay'),
    ('84_motion_object_mask.py', 'Mask moving objects and keep background intact'),
    ('85_motion_focus_crop.py', 'Automatically crop to the most active motion region'),
    ('86_motion_strobe.py', 'Create a strobe-style motion effect'),
    ('87_motion_blur_effect.py', 'Apply directional blur to moving regions'),
    ('88_motion_color_wave.py', 'Render a colored motion wave behind moving objects'),
]

hand_template = textwrap.dedent('''
    import cv2
    import mediapipe as mp
    import numpy as np
    import math

    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def main():
        with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                frame = cv2.flip(frame, 1)
                h, w, _ = frame.shape
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = hands.process(rgb)
                output = frame.copy()

                if results.multi_hand_landmarks:
                    hand_landmarks = results.multi_hand_landmarks[0]
                    mp_draw.draw_landmarks(output, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    lm = hand_landmarks.landmark
                    thumb = lm[4]
                    index = lm[8]
                    middle = lm[12]
                    ring = lm[16]
                    pinky = lm[20]
                    thumb_pos = (int(thumb.x * w), int(thumb.y * h))
                    index_pos = (int(index.x * w), int(index.y * h))
                    midpoint = ((thumb_pos[0] + index_pos[0]) // 2, (thumb_pos[1] + index_pos[1]) // 2)
                    cv2.circle(output, thumb_pos, 10, (255, 0, 255), -1)
                    cv2.circle(output, index_pos, 10, (255, 0, 255), -1)
                    cv2.line(output, thumb_pos, index_pos, (255, 255, 0), 2)
                    distance = int(math.hypot(index_pos[0] - thumb_pos[0], index_pos[1] - thumb_pos[1]))
                    {effect_body}

                cv2.putText(output, '{description}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
                cv2.imshow('{title}', output)
                if cv2.waitKey(1) == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()

    if __name__ == '__main__':
        main()
''')

face_template = textwrap.dedent('''
    import cv2
    import mediapipe as mp
    import numpy as np

    mp_face = mp.solutions.face_mesh
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def main():
        with mp_face.FaceMesh(max_num_faces=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as face_mesh:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                frame = cv2.flip(frame, 1)
                h, w, _ = frame.shape
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = face_mesh.process(rgb)
                output = frame.copy()

                if results.multi_face_landmarks:
                    landmarks = results.multi_face_landmarks[0]
                    mp_draw.draw_landmarks(output, landmarks, mp_face.FACEMESH_TESSELATION, mp_draw.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1))
                    points = [(int(p.x*w), int(p.y*h)) for p in landmarks.landmark]
                    {effect_body}

                cv2.putText(output, '{description}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
                cv2.imshow('{title}', output)
                if cv2.waitKey(1) == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()

    if __name__ == '__main__':
        main()
''')

pose_template = textwrap.dedent('''
    import cv2
    import mediapipe as mp
    import math

    mp_pose = mp.solutions.pose
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    def main():
        with mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.7) as pose:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                frame = cv2.flip(frame, 1)
                h, w, _ = frame.shape
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = pose.process(rgb)
                output = frame.copy()

                if results.pose_landmarks:
                    mp_draw.draw_landmarks(output, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                    lm = results.pose_landmarks.landmark
                    {effect_body}

                cv2.putText(output, '{description}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
                cv2.imshow('{title}', output)
                if cv2.waitKey(1) == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()

    if __name__ == '__main__':
        main()
''')

motion_template = textwrap.dedent('''
    import cv2
    import numpy as np

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    prev_frame = None

    def main():
        global prev_frame
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            output = frame.copy()

            if prev_frame is not None:
                diff = cv2.absdiff(prev_frame, gray)
                _, mask = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
                mask_color = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
                {effect_body}

            prev_frame = gray
            cv2.putText(output, '{description}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            cv2.imshow('{title}', output)
            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    if __name__ == '__main__':
        main()
''')

hand_effects = {
    '49_hand_scroll_control.py': 'angle = math.degrees(math.atan2(index_pos[1] - thumb_pos[1], index_pos[0] - thumb_pos[0])); cv2.putText(output, f"Scroll Angle: {int(angle)}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)',
    '50_hand_pause_player.py': 'if distance < 45:\n    cv2.putText(output, "Pause", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)\nelse:\n    cv2.putText(output, "Play", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)',
    '51_hand_brightness_slider.py': 'brightness = np.interp(index_pos[1], [0, h], [2.0, 0.5]); output = cv2.convertScaleAbs(output, alpha=brightness, beta=0); cv2.putText(output, f"Brightness: {brightness:.2f}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)',
    '52_hand_zoom_filter.py': 'zoom = np.interp(distance, [30, 180], [1.0, 2.2]); crop_w = int(w / zoom); crop_h = int(h / zoom); x1 = max(0, (w - crop_w)//2); y1 = max(0, (h - crop_h)//2); crop = output[y1:y1+crop_h, x1:x1+crop_w]; output = cv2.resize(crop, (w, h)); cv2.putText(output, f"Zoom: {zoom:.1f}x", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)',
    '53_hand_silhouette_overlay.py': 'mask = np.zeros_like(output); cv2.fillPoly(mask, [np.array([thumb_pos, index_pos, (index_pos[0], index_pos[1]+80), (thumb_pos[0], thumb_pos[1]+80)])], (0,255,0)); output = cv2.addWeighted(output, 0.7, mask, 0.3, 0);',
    '54_hand_shadow_effect.py': 'shadow = output.copy(); cv2.circle(shadow, (midpoint[0]+20, midpoint[1]+20), 80, (0,0,0), -1); output = cv2.addWeighted(output, 0.75, shadow, 0.25, 0);',
    '55_hand_sparkle_trail.py': 'for i in range(0, 360, 45): cv2.circle(output, (midpoint[0]+int(40*np.cos(np.radians(i))), midpoint[1]+int(40*np.sin(np.radians(i)))), 5, (255,255,0), -1)',
    '56_hand_ar_shield.py': 'cv2.circle(output, midpoint, 100, (255,255,0), 4); cv2.putText(output, "Shield Active", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)',
    '57_hand_emoji_reactions.py': 'finger_count = sum([thumb.x < lm[3].x, index.y < lm[6].y, middle.y < lm[10].y, ring.y < lm[14].y, pinky.y < lm[18].y]); reactions = ["😐", "😀", "😂", "😮", "🤩", "🙌"]; cv2.putText(output, reactions[min(finger_count,5)], (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,255), 2)',
    '58_hand_warp_window.py': 'radius = int(np.clip(distance, 60, 140)); mask = np.zeros((h, w), dtype=np.uint8); cv2.circle(mask, midpoint, radius, 255, -1); blurred = cv2.GaussianBlur(output, (31,31), 0); output = np.where(mask[:,:,None] == 255, output, blurred)',
}

face_effects = {
    '59_face_mask_sticker.py': 'nose = points[1]; chin = points[152]; left = points[234]; right = points[454]; overlay = output.copy(); cv2.rectangle(overlay, (left[0], left[1]-20), (right[0], chin[1]+20), (0,128,255), -1); output = cv2.addWeighted(output, 0.6, overlay, 0.4, 0)',
    '60_face_beard_filter.py': 'chin = points[152]; left = points[234]; right = points[454]; cv2.rectangle(output, (left[0], chin[1]), (right[0], chin[1]+40), (50,30,20), -1)',
    '61_face_mirror_glass.py': 'left_eye = points[33]; right_eye = points[263]; cv2.circle(output, left_eye, 40, (200,200,255), -1); cv2.circle(output, right_eye, 40, (200,200,255), -1)',
    '62_face_blend_filter.py': 'hsv = cv2.cvtColor(output, cv2.COLOR_BGR2HSV); hsv[:,:,1] = cv2.add(hsv[:,:,1], 50); output = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)',
    '63_face_landmark_graph.py': 'for i, point in enumerate(points[10:60:10], start=10): cv2.circle(output, point, 3, (0,255,255), -1); cv2.putText(output, f"P{i}", (point[0]+5, point[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1)',
    '64_face_pose_align.py': 'left = points[234]; right = points[454]; nose = points[1]; cv2.line(output, left, right, (255,0,0), 2); cv2.line(output, nose, (nose[0], nose[1]-80), (0,255,0), 2)',
    '65_face_color_pop.py': 'hsv = cv2.cvtColor(output, cv2.COLOR_BGR2HSV); mask = cv2.inRange(hsv, (0, 40, 40), (20, 255, 255)); gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY); gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR); output = np.where(mask[:,:,None] == 255, output, gray)',
    '66_face_symmetry_view.py': 'mid = w//2; left = output[:, :mid]; right = cv2.flip(left, 1); output[:, mid:] = right',
    '67_face_smile_meter.py': 'mouth_left = points[61]; mouth_right = points[291]; mouth_top = points[13]; mouth_bottom = points[14]; mouth_width = np.linalg.norm(np.array(mouth_left)-np.array(mouth_right)); mouth_height = np.linalg.norm(np.array(mouth_top)-np.array(mouth_bottom)); cv2.putText(output, f"Smile: {int(mouth_width/mouth_height)}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)',
    '68_face_glow_highlight.py': 'for idx in [10, 152, 234, 454]: cv2.circle(output, points[idx], 15, (0,255,255), -1)',
}

pose_effects = {
    '69_pose_squat_counter.py': 'hip = lm[24]; knee = lm[26]; ankle = lm[28]; angle = int(abs((knee.y-hip.y)/(ankle.y-knee.y+1e-6))*100); cv2.putText(output, f"Squat Depth: {angle}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)',
    '70_pose_yoga_assistant.py': 'left_shoulder = lm[11]; left_elbow = lm[13]; left_wrist = lm[15]; cv2.putText(output, f"LArm: {int(abs(left_shoulder.y-left_wrist.y)*100)}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)',
    '71_pose_gesture_fit.py': 'right_wrist = lm[16]\nright_index = lm[20]\nif right_wrist.y < right_index.y:\n    cv2.putText(output, "Lifted", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)',
    '72_pose_posture_alert.py': 'left_shoulder = lm[11]\nright_shoulder = lm[12]\ndiff = abs(left_shoulder.y - right_shoulder.y)\nif diff > 0.03:\n    cv2.putText(output, "Posture Alert", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)',
    '73_pose_jump_counter.py': 'nose = lm[0]; cv2.putText(output, f"Jump Y: {int(nose.y*100)}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)',
    '74_pose_balance_meter.py': 'left_hip = lm[23]; right_hip = lm[24]; imbalance = abs(left_hip.x-right_hip.x); cv2.putText(output, f"Balance: {int((1-imbalance)*100)}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)',
    '75_pose_reach_tracker.py': 'left_wrist = lm[15]; left_shoulder = lm[11]; reach = int(abs(left_wrist.x-left_shoulder.x)*100); cv2.putText(output, f"Reach: {reach}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)',
    '76_pose_sitstand_counter.py': 'hip = lm[23]; knee = lm[25]; cv2.putText(output, f"Hip-Knee: {int(abs(hip.y-knee.y)*100)}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)',
    '77_pose_dance_visualizer.py': 'for idx in [11, 12, 23, 24, 25, 26]: pt = (int(lm[idx].x*w), int(lm[idx].y*h)); cv2.circle(output, pt, 8, (255,0,255), -1)',
    '78_pose_angle_helper.py': 'left_knee = lm[26]; left_hip = lm[24]; left_ankle = lm[28]; cv2.line(output, (int(left_hip.x*w), int(left_hip.y*h)), (int(left_knee.x*w), int(left_knee.y*h)), (0,255,0), 2); cv2.line(output, (int(left_ankle.x*w), int(left_ankle.y*h)), (int(left_knee.x*w), int(left_knee.y*h)), (0,255,0), 2)',
}

motion_effects = {
    '79_motion_trail.py': 'trail = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR); output = cv2.addWeighted(output, 0.8, trail, 0.5, 0)',
    '80_motion_direction_overlay.py': 'contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);\nfor cnt in contours:\n    if cv2.contourArea(cnt) > 300:\n        x,y,wc,hc = cv2.boundingRect(cnt);\n        cv2.arrowedLine(output, (x+wc//2, y+hc//2), (x+wc//2, y), (0,255,0), 2)',
    '81_motion_magnifier.py': 'motion_area = cv2.bitwise_and(output, mask_color); mag = cv2.resize(motion_area, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR); output[0:mag.shape[0], 0:mag.shape[1]] = mag',
    '82_motion_frame_blend.py': 'blend = cv2.addWeighted(output, 0.7, mask_color, 0.3, 0); output = blend',
    '83_motion_heat_tracker.py': 'heat = cv2.applyColorMap(mask, cv2.COLORMAP_JET); output = cv2.addWeighted(output, 0.7, heat, 0.3, 0)',
    '84_motion_object_mask.py': 'output = cv2.bitwise_and(output, mask_color)',
    '85_motion_focus_crop.py': 'contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE);\nif contours:\n    c = max(contours, key=cv2.contourArea); x,y,wc,hc = cv2.boundingRect(c);\n    output = cv2.resize(output[y:y+hc, x:x+wc], (640,480))',
    '86_motion_strobe.py': 'if int(cv2.getTickCount() / cv2.getTickFrequency()) % 2 == 0: output = cv2.addWeighted(output, 0.5, mask_color, 0.5, 0)',
    '87_motion_blur_effect.py': 'blur = cv2.GaussianBlur(output, (0,0), sigmaX=15); output = np.where(mask[:,:,None] == 255, blur, output)',
    '88_motion_color_wave.py': 'hue = np.zeros_like(output); hue[:,:,0] = mask; color = cv2.applyColorMap(hue[:,:,0], cv2.COLORMAP_HSV); output = cv2.addWeighted(output, 0.7, color, 0.3, 0)',
}

def indent_effect(body, spaces):
    return body.replace('\n', '\n' + spaces)

for filename, description in projects:
    path = root / filename
    title = filename.replace('.py', '').replace('_', ' ').title()
    if filename in hand_effects:
        body = indent_effect(hand_effects[filename], ' ' * 16)
        content = hand_template.format(title=title, description=description, effect_body=body)
    elif filename in face_effects:
        body = indent_effect(face_effects[filename], ' ' * 16)
        content = face_template.format(title=title, description=description, effect_body=body)
    elif filename in pose_effects:
        body = indent_effect(pose_effects[filename], ' ' * 16)
        content = pose_template.format(title=title, description=description, effect_body=body)
    else:
        body = indent_effect(motion_effects[filename], ' ' * 12)
        content = motion_template.format(title=title, description=description, effect_body=body)
    path.write_text(content, encoding='utf-8')

readme_path = root / 'README.md'
readme = readme_path.read_text(encoding='utf-8')
section_header = '### 🧩 Additional Computer Vision Demos'
if section_header not in readme:
    section = '\n' + section_header + '\n| File | Description |\n|------|-------------|\n'
    for filename, description in projects:
        section += f'| `{filename}` | {description} |\n'
    readme_path.write_text(readme + section, encoding='utf-8')

print('Generated', len(projects), 'files and updated README.')
