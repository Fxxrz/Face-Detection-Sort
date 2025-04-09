# Face Detection Filter for Images

This Python script filters `.jpg` images in a folder based on face detection (using [MediaPipe](https://github.com/google/mediapipe)) and file size. Images that contain a detected face and fall within the defined size limits are copied to a target folder.

## Features

- Select source and target folders via a simple GUI (Tkinter)
- Face detection using MediaPipe
- Progress display with `tqdm`
- Filters images based on minimum and maximum file size
- Automatically copies valid images

## Requirements

- Python 3.7 or higher

### Python Dependencies

Install the required packages with:

```bash
pip install -r requirements.txt
```

**Required packages:**

- `mediapipe`
- `pillow`
- `numpy`
- `tqdm`

Alternatively:

```bash
pip install mediapipe pillow numpy tqdm
```

## Usage

1. Run the script:

```bash
python FaceDetectionSort.py
```

2. A dialog window will open asking you to select the **source folder** that contains the images.
3. Then, select the **target folder** where the filtered images should be copied.
4. The script will process all `.jpg` images:
   - Skips images that are below or above the defined size threshold
   - Detects faces with a configurable confidence threshold (default: `0.75`)
   - Displays progress and status in the console

## Configurable Parameters

You can change these at the top of the `main.py` file:

```python
FACE_DETECTION_THRESHOLD = 0.75  # Confidence threshold for face detection
MIN_FILE_SIZE_KB = 100           # Minimum file size in KB
MAX_FILE_SIZE_MB = 15            # Maximum file size in MB
```
