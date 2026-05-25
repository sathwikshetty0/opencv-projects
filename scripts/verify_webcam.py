import cv2
import sys

def main():
    print("Verifying webcam accessibility with OpenCV...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video device index 0.")
        sys.exit(1)
        
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame from video device.")
        cap.release()
        sys.exit(1)
        
    print(f"Success! Camera resolution: {frame.shape[1]}x{frame.shape[0]}")
    cap.release()
    sys.exit(0)

if __name__ == '__main__':
    main()
