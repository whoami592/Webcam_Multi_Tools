import cv2
import tkinter as tk
from PIL import Image, ImageTk
import os
import time
from datetime import datetime

class WebcamXploitPro:
    def __init__(self, root):
        self.root = root
        self.root.title("Webcam Xploit Pro")
        self.root.geometry("800x600")
        
        # Initialize webcam
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Could not open webcam.")
            exit()
        
        # Create directory for saving images
        self.save_dir = "captured_images"
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        
        # Banner
        self.banner_text = (
            "Webcam Xploit Pro\n"
            "Coded by Pakistani Ethical Hacker Mr. Sabaz Ali Khan\n"
            "For Educational and Ethical Use Only"
        )
        self.banner_label = tk.Label(
            root, text=self.banner_text, font=("Arial", 14, "bold"), fg="green", bg="black"
        )
        self.banner_label.pack(pady=10)
        
        # Camera feed label
        self.camera_feed = tk.Label(root)
        self.camera_feed.pack(pady=10)
        
        # Buttons
        self.capture_button = tk.Button(
            root, text="Capture Image", command=self.capture_image, font=("Arial", 12)
        )
        self.capture_button.pack(pady=5)
        
        self.start_button = tk.Button(
            root, text="Start Feed", command=self.start_feed, font=("Arial", 12)
        )
        self.start_button.pack(pady=5)
        
        self.stop_button = tk.Button(
            root, text="Stop Feed", command=self.stop_feed, font=("Arial", 12), state=tk.DISABLED
        )
        self.stop_button.pack(pady=5)
        
        self.status_label = tk.Label(
            root, text="Status: Stopped", font=("Arial", 10), fg="red"
        )
        self.status_label.pack(pady=5)
        
        self.running = False
        self.update_camera()
    
    def capture_image(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                image_path = os.path.join(self.save_dir, f"capture_{timestamp}.jpg")
                cv2.imwrite(image_path, frame)
                self.status_label.config(
                    text=f"Image saved: {image_path}", fg="green"
                )
            else:
                self.status_label.config(text="Error: Could not capture image", fg="red")
    
    def start_feed(self):
        if not self.running:
            self.running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.status_label.config(text="Status: Running", fg="green")
            self.update_camera()
    
    def stop_feed(self):
        if self.running:
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            self.status_label.config(text="Status: Stopped", fg="red")
    
    def update_camera(self):
        if self.running:
            ret, frame = self.cap.read()
            if ret:
                # Convert frame to RGB for Tkinter
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Resize frame to fit window
                frame_resized = cv2.resize(frame_rgb, (640, 480))
                # Convert to PIL Image
                image = Image.fromarray(frame_resized)
                photo = ImageTk.PhotoImage(image=image)
                self.camera_feed.config(image=photo)
                self.camera_feed.image = photo
        self.root.after(10, self.update_camera)
    
    def on_closing(self):
        self.running = False
        if self.cap.isOpened():
            self.cap.release()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = WebcamXploitPro(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()