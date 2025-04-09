# main.py

import os
import shutil
from tkinter import Tk, filedialog
from PIL import Image
import numpy as np
import mediapipe as mp
from tqdm import tqdm

# Konfigurationsvariablen
FACE_DETECTION_THRESHOLD = 0.75  # Testweise niedriger Schwellwert
MIN_FILE_SIZE_KB = 100  # Mindestgröße (in KB)
MAX_FILE_SIZE_MB = 15  # Maximalgröße (in MB)

# Funktion zur Auswahl eines Ordners
def select_folder(prompt):
    root = Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    return filedialog.askdirectory(title=prompt)

# Funktion zur Gesichtserkennung mit Mediapipe
def detect_faces(image_path, threshold):
    mp_face_detection = mp.solutions.face_detection
    with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=threshold) as face_detection:
        try:
            # Bild öffnen und in Numpy-Array konvertieren
            image = Image.open(image_path).convert("RGB")
            image_array = np.array(image)

            # Gesichtserkennung ausführen
            results = face_detection.process(image_array)
            if results.detections:
                # Ausgabe der Detektionen zur Diagnose
                print(f"Detektionen in {os.path.basename(image_path)}: {len(results.detections)}")
                for detection in results.detections:
                    print(f"Wahrscheinlichkeit: {detection.score[0]}")
                return True  # Gesichter erkannt
        except Exception as e:
            print(f"Fehler beim Verarbeiten von {image_path}: {e}")
    return False  # Keine Gesichter erkannt

# Funktion zur Verarbeitung der Bilder
def process_images(source_folder, target_folder):
    # Alle JPG-Bilder im Ordner finden
    image_files = [f for f in os.listdir(source_folder) if f.lower().endswith('.jpg')]

    # Fortschrittsanzeige
    print("Starte die Verarbeitung...")
    with tqdm(total=len(image_files), desc="Bilder verarbeitet") as progress:
        for image_file in image_files:
            image_path = os.path.join(source_folder, image_file)

            # Prüfe die Dateigröße
            file_size_kb = os.path.getsize(image_path) / 1024
            if file_size_kb < MIN_FILE_SIZE_KB or file_size_kb > MAX_FILE_SIZE_MB * 1024:
                progress.write(f"Überspringe {image_file} (Größe nicht geeignet)")
                progress.update(1)
                continue

            # Gesichtserkennung durchführen
            if detect_faces(image_path, FACE_DETECTION_THRESHOLD):
                target_path = os.path.join(target_folder, image_file)
                shutil.copy2(image_path, target_path)  # Kopiere das Bild
                progress.write(f"Gesicht erkannt: {image_file}")
            else:
                progress.write(f"Kein Gesicht: {image_file}")

            progress.update(1)

# Hauptprogramm
def main():
    print("Bitte wähle den Quellordner aus.")
    source_folder = select_folder("Quellordner auswählen")
    if not source_folder:
        print("Kein Quellordner ausgewählt. Beende das Programm.")
        return

    print("Bitte wähle den Zielordner aus.")
    target_folder = select_folder("Zielordner auswählen")
    if not target_folder:
        print("Kein Zielordner ausgewählt. Beende das Programm.")
        return

    process_images(source_folder, target_folder)
    print("Verarbeitung abgeschlossen.")

if __name__ == "__main__":
    main()