# Face Mesh Viewer

A real-time face landmark tracker built with Python, OpenCV and MediaPipe. It reads video from your webcam, detects facial landmarks (including refined eye and lip landmarks), and draws each point on a live mirrored preview.

## Features

- Live webcam capture with a mirrored (selfie-style) view
- Detects the full MediaPipe face mesh, with refined landmarks around the eyes and lips
- Draws every landmark as a green dot on the video feed
- Reads the screen resolution with PyAutoGUI, ready for future cursor-control features
- Press `q` to quit

## How It Works

1. OpenCV captures each frame from the default webcam (`VideoCapture(0)`).
2. The frame is flipped horizontally and converted from BGR to RGB.
3. MediaPipe's `FaceMesh` processes the frame and returns normalized landmark coordinates (0.0 to 1.0).
4. Each landmark is scaled to pixel coordinates using the frame width and height.
5. A small circle is drawn at each point, and the annotated frame is shown in a window.

## Requirements

- Python 3.8 to 3.11
- A working webcam
- Python packages:
  - `opencv-python`
  - `mediapipe`
  - `pyautogui`

## Installation

```bash
git clone https://github.com/William2716057/faceMesh.git
cd faceMesh
pip install opencv-python mediapipe pyautogui
```

## Usage

```bash
python face_mesh.py
```

A window titled **Face Mesh** will open showing your webcam feed with the landmarks overlaid. Press **q** to close it.

## Project Structure

```
.
├── face_mesh.py   # main script
└── README.md
```

## Configuration

| Setting | Where | Description |
|---|---|---|
| Camera index | `cv2.VideoCapture(0)` | Change `0` to use a different webcam |
| Refined landmarks | `FaceMesh(refine_landmarks=True)` | Adds detailed eye and lip (iris) landmarks |
| Dot colour / size | `cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)` | BGR colour and radius of each landmark dot |

## Notes

- This script uses the `mp.solutions` API, which is available in older MediaPipe releases. If you get an attribute error on a newer version, install an earlier one: `pip install mediapipe==0.10.14`.
- On Linux, `pyautogui` may need an X display and extra packages such as `python3-tk` and `python3-dev`.
- `pyautogui` and the screen size are currently unused, and are included as groundwork for controlling the mouse with head or eye movement.

## Ideas for Future Work

- Track iris landmarks to move the mouse cursor with eye movement
- Blink detection for click actions
- Head pose estimation
- Save landmark data to CSV for analysis
