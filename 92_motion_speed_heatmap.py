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
    
    heatmap = np.zeros_like(prev_frame, dtype=np.float32)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Calculate absolute difference
        diff = cv2.absdiff(prev_gray, gray)
        _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
        
        # Add to heatmap
        heatmap[thresh > 0] += 5.0
        # Decay heatmap slightly
        heatmap -= 0.5
        heatmap = np.clip(heatmap, 0, 255)
        
        # Convert heatmap to BGR representation
        heatmap_uint8 = heatmap.astype(np.uint8)
        color_heatmap = cv2.applyColorMap(heatmap_uint8[:, :, 0], cv2.COLORMAP_JET)
        
        output = cv2.addWeighted(frame, 0.7, color_heatmap, 0.3, 0)
        
        prev_gray = gray

        cv2.putText(output, 'Motion Speed Heatmap - Move to generate heat patterns', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(output, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.imshow('Motion Speed Heatmap', output)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
