import cv2
import os

def video_to_frames(video_path, output_folder):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open video
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Couldn't open the video file.")
        return

    frame_num = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Save each frame as an image
        frame_name = os.path.join(output_folder, f'frame_{frame_num:04d}.jpg')
        cv2.imwrite(frame_name, frame)
        frame_num += 1

    cap.release()
    print(f"Extracted {frame_num} frames and saved to {output_folder}")

# Example usage
video_path = r"path"
output_folder = r"path"
video_to_frames(video_path, output_folder)
