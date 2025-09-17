import numpy as np
import supervision as sv
from ultralytics import YOLO

SOURCE_VIDEO_PATH = "/app/videos/sample3.mp4"
TARGET_VIDEO_PATH = "result.mp4"

model = YOLO("yolov8n.pt")
box_annotator = sv.BoxAnnotator()

def process_frame(frame: np.ndarray, frame_index: int) -> np.ndarray:
    results = model(frame)[0]
    detections = sv.Detections.from_ultralytics(results)
    annotated_frame = box_annotator.annotate(
        scene=frame.copy(),
        detections=detections
    )
    return annotated_frame

print(f"Processing video from '{SOURCE_VIDEO_PATH}' and saving to '{TARGET_VIDEO_PATH}'...")
sv.process_video(
    source_path=SOURCE_VIDEO_PATH,
    target_path=TARGET_VIDEO_PATH,
    callback=process_frame
)

print("Video processing complete.")
