import cv2
import os
import time
from datetime import datetime
import argparse

def print_banner():
    banner = """
    ╔════════════════════════════════════════════╗
    ║          SilentCam Capturer v2.0           ║
    ║ Coded by Pakistani Ethical Hacker          ║
    ║         Mr. Sabaz Ali Khan                 ║
    ╚════════════════════════════════════════════╝
    """
    print(banner)

def create_output_directory():
    output_dir = "Captured_Images"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def capture_image(camera, output_dir):
    try:
        ret, frame = camera.read()
        if ret:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(output_dir, f"capture_{timestamp}.jpg")
            cv2.imwrite(filename, frame)
            print(f"[+] Image saved: {filename}")
        else:
            print("[-] Failed to capture image")
    except Exception as e:
        print(f"[-] Error capturing image: {e}")

def main():
    parser = argparse.ArgumentParser(description="SilentCam Capturer by Mr. Sabaz Ali Khan")
    parser.add_argument("--interval", type=int, default=5, help="Interval between captures in seconds")
    args = parser.parse_args()

    print_banner()
    output_dir = create_output_directory()
    
    # Initialize webcam (0 is usually the default camera)
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("[-] Error: Could not open camera")
        return
    
    try:
        print(f"[*] Capturing images every {args.interval} seconds. Press Ctrl+C to stop")
        while True:
            capture_image(camera, output_dir)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\n[*] Stopping capture")
    except Exception as e:
        print(f"[-] Unexpected error: {e}")
    finally:
        camera.release()
        print("[*] Camera released")

if __name__ == "__main__":
    main()