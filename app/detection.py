from ultralytics import YOLO

# Load model sekali saja
model = YOLO("yolov8n.pt")

def detect_vehicles(frame):
    results = model(frame)

    return results