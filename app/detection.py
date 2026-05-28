from ultralytics import YOLO

model = YOLO("yolov8n.pt")

# Kendaraan yang ingin dideteksi
VEHICLE_CLASSES = [2, 3, 5, 7]
# car, motorcycle, bus, truck


def detect_vehicles(frame):

    results = model(frame)

    filtered_boxes = []

    for result in results:

        boxes = result.boxes

        for box in boxes:

            cls = int(box.cls[0])

            conf = float(box.conf[0])

            if cls in VEHICLE_CLASSES and conf > 0.5:
                filtered_boxes.append(box)

    annotated_frame = results[0].plot()

    return annotated_frame, filtered_boxes