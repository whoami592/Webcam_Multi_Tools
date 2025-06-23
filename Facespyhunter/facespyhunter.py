import cv2
import pyfiglet
from rich.console import Console
import os
import sys

# Initialize Rich Console for styled output
console = Console()

def print_banner():
    """Display the ASCII art banner with tool name and coder credit."""
    banner = pyfiglet.figlet_format("FaceSpyHunter 2025", font="slant")
    console.print(banner, style="bold green")
    console.print("Coded by Pakistani Ethical Hacker Mr. Sabaz Ali Khan", style="bold cyan")
    console.print("Ethical Hacking Tool for Educational Purposes Only", style="bold yellow")
    console.print("="*60, style="bold magenta")

def detect_faces_image(image_path):
    """Detect faces in a provided image using OpenCV Haar Cascade."""
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    if face_cascade.empty():
        console.print("[ERROR] Failed to load Haar Cascade classifier.", style="bold red")
        return

    # Read the image
    if not os.path.exists(image_path):
        console.print(f"[ERROR] Image file {image_path} not found.", style="bold red")
        return
    image = cv2.imread(image_path)
    if image is None:
        console.print("[ERROR] Failed to load image.", style="bold red")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the result
    console.print(f"[INFO] Detected {len(faces)} face(s) in the image.", style="bold blue")
    cv2.imshow('FaceSpyHunter - Image Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def detect_faces_webcam():
    """Detect faces in real-time using webcam feed."""
    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    if face_cascade.empty():
        console.print("[ERROR] Failed to load Haar Cascade classifier.", style="bold red")
        return

    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        console.print("[ERROR] Failed to access webcam.", style="bold red")
        return

    console.print("[INFO] Starting webcam face detection. Press 'q' to quit.", style="bold blue")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            console.print("[ERROR] Failed to capture frame.", style="bold red")
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('FaceSpyHunter - Webcam Detection', frame)

        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

def main():
    """Main function to run the FaceSpyHunter tool."""
    print_banner()
    
    while True:
        console.print("\n[FaceSpyHunter 2025 Menu]", style="bold green")
        console.print("1. Detect Faces in Image", style="bold white")
        console.print("2. Detect Faces via Webcam", style="bold white")
        console.print("3. Exit", style="bold white")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            image_path = input("Enter the path to the image file: ")
            detect_faces_image(image_path)
        elif choice == '2':
            detect_faces_webcam()
        elif choice == '3':
            console.print("[INFO] Exiting FaceSpyHunter 2025. Stay ethical!", style="bold yellow")
            sys.exit(0)
        else:
            console.print("[ERROR] Invalid choice. Please select 1, 2, or 3.", style="bold red")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[INFO] Program interrupted by user. Exiting safely.", style="bold yellow")
        sys.exit(0)
    except Exception as e:
        console.print(f"[ERROR] An unexpected error occurred: {str(e)}", style="bold red")
        sys.exit(1)

# Disclaimer: This tool is for educational purposes only. Unauthorized use of face detection or recognition
# technologies may violate privacy laws. Always obtain consent and use ethically.
# Advanced face recognition (e.g., identifying individuals) would require libraries like face_recognition
# and proper ethical/legal frameworks, which are not implemented here.
