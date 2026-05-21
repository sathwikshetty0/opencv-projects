import cv2

cap = cv2.VideoCapture(0)

trackers = {}
colors = {
    "CSRT": (255, 0, 0), # Blue
    "KCF": (0, 255, 0),  # Green
    "MIL": (0, 0, 255)   # Red
}

init_bbox = None

print("Press 's' to select object to track with CSRT, KCF, and MIL trackers.")
print("Press 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # If trackers are initialized, update all of them
    if len(trackers) > 0:
        for name, tracker in list(trackers.items()):
            success, bbox = tracker.update(frame)
            if success:
                x, y, w, h = [int(v) for v in bbox]
                cv2.rectangle(frame, (x, y), (x + w, y + h), colors[name], 2)
                cv2.putText(frame, name, (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.45, colors[name], 1)
            else:
                cv2.putText(frame, f"{name}: FAILED", (10, 80 + list(colors.keys()).index(name)*25),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.55, colors[name], 2)

    # Info overlay
    cv2.putText(frame, "Trackers: CSRT(Blue) | KCF(Green) | MIL(Red)", (15, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2)
    cv2.putText(frame, "Press 's' to select target. 'q' to quit.", (15, 55),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (200, 200, 200), 1)

    cv2.imshow("Multi-Tracker Benchmark", frame)

    key = cv2.waitKey(1)
    if key == ord('s'):
        init_bbox = cv2.selectROI("Multi-Tracker Benchmark", frame, fromCenter=False, showCrosshair=True)
        if init_bbox[2] > 0 and init_bbox[3] > 0:
            # Recreate/Re-initialize all trackers
            trackers = {
                "CSRT": cv2.TrackerCSRT_create(),
                "KCF": cv2.TrackerKCF_create(),
                "MIL": cv2.TrackerMIL_create()
            }
            
            for name, tracker in trackers.items():
                tracker.init(frame, init_bbox)
            
            print("All three trackers (CSRT, KCF, MIL) initialized successfully.")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
