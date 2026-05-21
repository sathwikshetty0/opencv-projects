import cv2
import os

print("--- Image Stitching Panorama ---")
print("Press 's' to capture a frame.")
print("Press 'p' to process and stitch captured frames.")
print("Press 'q' to quit.")

cap = cv2.VideoCapture(0)
captured_frames = []

# Check if pre-existing test files 1.png, 2.png, 3.png exist
test_files = ["1.png", "2.png", "3.png"]
all_exist = all(os.path.exists(f) for f in test_files)

if all_exist:
    print("\nFound local test files: 1.png, 2.png, 3.png. Running auto-stitch...")
    images = [cv2.imread(f) for f in test_files]
    stitcher = cv2.Stitcher.create()
    status, stitched = stitcher.stitch(images)
    
    if status == cv2.Stitcher_OK:
        print("Stitching successful! Displaying stitched image. Press key to continue to live cam...")
        cv2.imshow("Stitched Test Panorama", stitched)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"Stitching failed on test files. Error code: {status}")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Show live view
    display_frame = frame.copy()
    cv2.putText(display_frame, f"Captured Frames: {len(captured_frames)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.imshow("Live Panorama Camera", display_frame)

    key = cv2.waitKey(1)
    if key == ord('s'):
        captured_frames.append(frame.copy())
        print(f"Frame {len(captured_frames)} captured.")
    elif key == ord('p'):
        if len(captured_frames) < 2:
            print("You need to capture at least 2 frames before stitching.")
        else:
            print("Stitching captured frames... please wait.")
            stitcher = cv2.Stitcher.create()
            status, stitched = stitcher.stitch(captured_frames)
            
            if status == cv2.Stitcher_OK:
                cv2.imshow("Result Panorama", stitched)
                print("Stitch Successful! Saved as panorama_result.png")
                cv2.imwrite("panorama_result.png", stitched)
            else:
                print(f"Stitch failed. Error code: {status}")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
