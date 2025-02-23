import cv2
from ultralytics import YOLO

# Load YOLO model

model = YOLO("yolo12n.pt") # Pretrained YOLOv12 model (COCO classes) and you can use custom dataset make it manual and train the data

# model = YOLO("yolov8n.pt")
# model = YOLO("yolo11n.pt")   
tracking = False
tracker = None

def select_object(event, x, y, flags, param):
    global tracking, tracker, bbox, frame
    if event == cv2.EVENT_LBUTTONDOWN:
        bbox = cv2.selectROI("Select Object", frame, fromCenter=False)
        tracker = cv2.TrackerCSRT_create()  # Choose the tracking algorithm
        tracker.init(frame, bbox)
        tracking = True

# Initialize video capture
cap = cv2.VideoCapture(0)  # 1 if i use external Camera
cv2.namedWindow("Live Tracking")
cv2.setMouseCallback("Live Tracking", select_object)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO model on the frame
    results = model(frame)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # If tracking, update the tracker
    if tracking:
        success, bbox = tracker.update(annotated_frame)
        if success:
            x, y, w, h = [int(v) for v in bbox]
            cv2.rectangle(annotated_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        else:
            cv2.putText(annotated_frame, "Tracking Failed!", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Show live feed
    cv2.imshow("Live Tracking", annotated_frame)

    # Break on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()