import cv2
import pyfiglet
from rich.console import Console

# Initialize Rich console for styled output
console = Console()

# Create banner with pyfiglet
banner = pyfiglet.figlet_format("GhostFace Tracker", font="slant")
attribution = "Coded by Pakistani Ethical Hacker Mr Sabaz Ali Khan"

# Print banner and attribution
console.print(banner, style="bold green")
console.print(attribution, style="bold cyan")
console.print("Starting real-time face tracking... Press 'q' to quit.\n", style="italic yellow")

# Load pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Check if classifier loaded successfully
if face_cascade.empty():
    console.print("[ERROR] Failed to load Haar Cascade classifier.", style="bold red")
    exit(1)

# Initialize video capture from default webcam
video_capture = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not video_capture.isOpened():
    console.print("[ERROR] Failed to open webcam.", style="bold red")
    exit(1)

# Main loop for face tracking
while True:
    # Read frame from video capture
    ret, frame = video_capture.read()
    if not ret:
        console.print("[ERROR] Failed to capture frame.", style="bold red")
        break

    # Convert frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            "GhostFace",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

    # Display the frame with detected faces
    cv2.imshow('GhostFace Tracker', frame)

    # Break loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
video_capture.release()
cv2.destroyAllWindows()

console.print("\nGhostFace Tracker terminated.", style="bold magenta")
