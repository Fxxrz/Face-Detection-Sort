# Gesichtserkennungs-Filter für Bilder

Dieses Python-Skript filtert `.jpg`-Bilder in einem Ordner basierend auf Gesichterkennung (mit [MediaPipe](https://github.com/google/mediapipe)) sowie Dateigröße. Bilder, in denen ein Gesicht erkannt wird und die innerhalb definierter Größenbeschränkungen liegen, werden in einen Zielordner kopiert.

## Features

- Auswahl von Quell- und Zielordner über eine einfache GUI (Tkinter)
- Gesichtserkennung mit MediaPipe
- Fortschrittsanzeige mit `tqdm`
- Filterung von Bildern nach minimaler und maximaler Dateigröße
- Automatisches Kopieren erkannter Bilder

## Voraussetzungen

- Python 3.7 oder höher

### Python-Abhängigkeiten

Installiere die benötigten Pakete mit:

```bash
pip install -r requirements.txt
```

**Benötigte Pakete:**

- `mediapipe`
- `pillow`
- `numpy`
- `tqdm`

Alternativ:

```bash
pip install mediapipe pillow numpy tqdm
```

## Nutzung

1. Starte das Skript:

```bash
FaceDetectionSort.py
```

2. Es öffnet sich ein Dialogfenster zur Auswahl des **Quellordners**, der Bilder enthalten soll.
3. Danach wählst du den **Zielordner**, in den gefilterte Bilder kopiert werden.
4. Das Skript verarbeitet alle `.jpg`-Bilder:
   - Überspringt Bilder unter oder über gesetzten schwellwert
   - Erkennt Gesichter mit einem konfigurierbaren Schwellenwert (Standard: `0.75`)
   - Gibt Fortschritt und Status in der Konsole aus

## Konfigurierbare Parameter

Diese kannst du direkt im Code (oben in `main.py`) anpassen:

```python
FACE_DETECTION_THRESHOLD = 0.75  # Schwellwert für Gesichtserkennung
MIN_FILE_SIZE_KB = 100           # Mindestgröße (in KB)
MAX_FILE_SIZE_MB = 15            # Maximalgröße (in MB)
```
