# import
import os
import sys
import cv2
from pathlib import Path

# path
current_path = Path(os.getcwd())
sys.path.insert(0, current_path)

# --- zone coordinate selector ---

# Replace with the path to your video file
video_path = f"{current_path}/videos/finance_20251001_1000_1001.mp4"

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Read the first frame
ret, frame = cap.read()
if not ret:
    print("Error: Could not read frame.")
    cap.release()
    exit()

# Function to get coordinates on mouse click
coordinates = []
def get_coords(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates.append([x, y])
        print(f"Added coordinate: ({x}, {y})")

# Display the frame and let the user click to get coordinates
cv2.imshow("Select Area", frame)
cv2.setMouseCallback("Select Area", get_coords)
print("Click on the image to select the vertices of your polygon.")
print("Press any key to close the window and see the coordinates.")
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()

print("\n--- Your polygon coordinates ---")
print("np.array([")
for coord in coordinates:
    print(f"    [{coord[0]}, {coord[1]}],")
print("])")

print("\nCopy and paste these coordinates into your main script.")