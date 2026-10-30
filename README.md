Hand Gesture Recognition System

 Overview
A real-time hand gesture recognition application developed using Python, OpenCV and MediaPipe.

The application uses a webcam to detect hand movements, track hand landmarks and recognize predefined gestures. The recognized gesture is displayed on the screen in real time.

 Features
- Real-time hand detection using a webcam.
- Hand landmark tracking using MediaPipe.
- Recognition of predefined hand gestures.
- Live display of recognized gestures.
- Visual hand landmark connections.

Technologies Used
- Python
- OpenCV
- MediaPipe

 Supported Gestures
| Gesture | Output |
|---|---|
| Open Palm | Stop |
| Fist | No |
| Thumbs Up | Yes |
| Peace Sign | Peace |
| Index Finger Up | Hello |

Installation
Install the required libraries:
pip install opencv-python mediapipe

How to Run
1. Clone this repository.
2. Install the required dependencies.
3. Connect a webcam.
4. Run the Python application:
python gesture_to_text.py
5. Show hand gestures in front of the webcam.
6. Press `q` to close the application.

How It Works
The application captures webcam frames using OpenCV and processes them through MediaPipe Hands. MediaPipe detects 21 hand landmarks. The application analyzes the relative positions of finger landmarks to identify predefined gestures.

Limitations
- Currently supports a limited set of predefined gestures.
- Recognition is based on simplified landmark-position rules.
- It is not a complete sign language translation system.

