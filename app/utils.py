import cv2

def resize_frame(frame, width=1280):
    height = int(frame.shape[0] * (width / frame.shape[1]))
    return cv2.resize(frame, (width, height))