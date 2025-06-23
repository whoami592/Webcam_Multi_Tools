import cv2
import pyfiglet
from rich.console import Console

# Initialize Rich console for styled output
console = Console()

# Create banner with pyfiglet
banner = pyfiglet.figlet_format("FacePhantom Pro", font="slant")
console.print(banner, style="bold green")
console.print("Coded by Pakistani Ethical Hacker Mr Sabaz Ali Khan", style="bold cyan")
console.print("A face recognition tool for ethical hacking purposes", style="bold yellow")

def detect_faces(image_path):
    try:
        # Load the pre-trained Haar Cascade classifier for face detection
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Read the input image
        image = cv2.imread(image_path)
        if image is None:
            console.print("[ERROR] Could not load image. Please check the file path.", style="bold red")
            return
        
        # Convert image to grayscale for face detection
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        if len(faces) == 0:
            console.print("[INFO] No faces detected in the image.", style="bold yellow")
            return
        
        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Save the output image with detected faces
        output_path = "output_with_faces.jpg"
        cv2.imwrite(output_path, image)
        console.print(f"[SUCCESS] Detected {len(faces)} face(s). Output saved to {output_path}", style="bold green")
        
    except Exception as e:
        console.print(f"[ERROR] An error occurred: {str(e)}", style="bold red")

if __name__ == "__main__":
    console.print("\nWelcome to FacePhantom Pro!", style="bold magenta")
    image_path = input("Enter the path to the image for face detection: ")
    detect_faces(image_path)
    console.print("Thank you for using FacePhantom Pro by Mr Sabaz Ali Khan!", style="bold cyan")
