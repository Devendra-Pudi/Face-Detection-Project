from ultralytics import YOLO
import os
import requests
from PIL import Image
from functools import lru_cache

MODEL_LINK = (
    "https://github.com/akanametov/yolov8-face/releases/download/v0.0.0/yolov8l-face.pt"
)
MODEL_PATH = "yolov8l-face.pt"
MAX_OUTPUT = 10


def check_and_download_model():
    if os.path.exists(MODEL_PATH):
        return MODEL_PATH
    response = requests.get(MODEL_LINK, timeout=60)
    with open(MODEL_PATH, "wb") as f:
        f.write(response.content)
    return MODEL_PATH


model = YOLO(check_and_download_model())


def adjust_box(b, image_shape, margin=10):
    x1, y1, x2, y2 = b
    x1 = max(0, x1 - margin)
    y1 = max(0, y1 - margin)
    x2 = min(image_shape[0], x2 + margin)
    y2 = min(image_shape[1], y2 + margin)
    return (int(x1), int(y1), int(x2), int(y2))


@lru_cache(maxsize=None)
def predict(path):
    results = model.predict(path)
    orimg = Image.open(path)
    return results, orimg


def detect_faces(image, box_margin=0):
    faces = []
    results, orimg = predict(image)
    for box in results[0].boxes:
        coords = box.xyxy[0]
        coords = adjust_box(coords, orimg.size, margin=box_margin)
        crop = orimg.crop(coords)
        crop = crop.resize((512, 512))
        faces.append(crop)
    return faces
