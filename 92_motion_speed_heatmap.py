import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def main():
    ret, prev_frame = cap.read()
    if not ret:
        return
    prev_frame = cv2.flip(prev_frame, 1)
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    
    # Initialize high precision floating point heatmap buffer
    heatmap = np.zeros_like(prev_frame, dtype=np.float32)
    colormap_mode = cv2.COLORMAP_JET

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        diff = cv2.absdiff(prev_gray, gray)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        
        # Accumulate motion intensity
        heatmap[thresh > 0] += 8.0
        # Decay motion trace gradually
        heatmap -= 0.8
        heatmap = np.clip(heatmap, 0, 255)
        
        # Apply colormap mapping
        heatmap_uint8 = heatmap.astype(np.uint8)
        color_heatmap = cv2.applyColorMap(heatmap_uint8[:, :, 0], colormap_mode)
        
        # Blend original frame and the heatmap colors
        output = cv2.addWeighted(frame, 0.65, color_heatmap, 0.35, 0)
        
        prev_gray = gray

        # Elegant HUD top bar
        cv2.rectangle(output, (0, 0), (w, 45), (30, 30, 30), -1)
        cv2.putText(output, 'Motion Speed Heatmap - Move fast to paint heatmap traces', (15, 28), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 255, 255), 1, cv2.LINE_AA)
        cv2.putText(output, 'Press q to quit, m to toggle colormap', (w - 320, 28), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.52, (255, 255, 255), 1, cv2.LINE_AA)

        cv2.imshow('Motion Speed Heatmap', output)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('m'):
            # Toggle between JET and HOT colormaps
            if colormap_mode == cv2.COLORMAP_JET:
                colormap_mode = cv2.COLORMAP_HOT
            else:
                colormap_mode = cv2.COLORMAP_JET

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
