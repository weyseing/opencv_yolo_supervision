import argparse
import numpy as np
import supervision as sv
from ultralytics import YOLO

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

def main(source_video_path: str):
    target_video_path = "result.mp4"
    print(f"Processing video from '{source_video_path}' and saving to '{target_video_path}'...")
    sv.process_video(
        source_path=source_video_path,
        target_path=target_video_path,
        callback=process_frame
    )
    print("Video processing complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("video_path", type=str, help="The path to the source video mp4 file")
    args = parser.parse_args()
    
    main(args.video_path)