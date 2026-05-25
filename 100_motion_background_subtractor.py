import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def main():
    # Create MOG2 Background Subtractor
    backSub = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        
        # Apply the background subtractor to get foreground mask
        fgMask = backSub.apply(frame)
        
        # Isolate foreground pixels on BGR frame
        foreground = cv2.bitwise_and(frame, frame, mask=fgMask)
        
        cv2.putText(foreground, 'Background Subtraction - MOG2 Model', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        cv2.putText(foreground, 'Press q to quit', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        
        # Display the result mask and the extracted foreground
        cv2.imshow('FG Mask', fgMask)
        cv2.imshow('Foreground Extract', foreground)
        
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
