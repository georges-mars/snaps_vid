import cv2

def capture_frames(video_path, output_path, frame_interval=30):
    """
    Capture frames from a video and save them as images.

    Parameters:
        video_path (str): Path to the input video file.
        output_path (str): Path to the directory where images will be saved.
        frame_interval (int): Number of frames to skip before capturing the next frame. try messing around with this
    """
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video file opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Create the output directory if it doesn't exist
    import os
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Initialize variables
    frame_count = 0

    # Loop through the frames
    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # Break the loop if we reached the end of the video
        if not ret:
            break

        # Capture frames at the specified interval
        if frame_count % frame_interval == 0:
            # Save the frame as an image
            image_path = os.path.join(output_path, f"frame_{frame_count}.png")
            cv2.imwrite(image_path, frame)

        frame_count += 1

    # Release the video capture object
    cap.release()

    print(f"Frames captured: {frame_count}")
    print(f"Images saved to: {output_path}")

if __name__ == "__main__":
    # Specify the path to the input video file
    video_path = "C:\\Users\\mars\\OneDrive\\Pictures\\Camera Roll\\WIN_20231003_10_29_09_Pro.mp4"

    # Specify the path to the output directory
    output_path = "C:\\Users\\mars\\OneDrive\\Desktop\\trial"

    # Capture frames from the video
    capture_frames(video_path, output_path)
