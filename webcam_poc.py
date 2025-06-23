import cv2
import time
import datetime

# Banner function to display credit
def display_banner():
    banner = """
    ╔════════════════════════════════════════════╗
    ║    ZeroDay Webcam Proof of Concept (PoC)    ║
    ║ Coded by Pakistani Ethical Hacker          ║
    ║ Mr. Sabaz Ali Khan                         ║
    ║ For Educational and Ethical Purposes Only  ║
    ╚════════════════════════════════════════════╝
    """
    print(banner)

# Main function to access webcam
def webcam_poc():
    # Display banner
    display_banner()

    # Initialize webcam (0 is default camera)
    cap = cv2.VideoCapture(0)

    # Check if webcam opened successfully
    if not cap.isOpened():
        print("[-] Error: Could not access webcam. Ensure it is connected and not in use.")
        return

    print("[+] Webcam accessed successfully. Press 'q' to quit or 's' to save a snapshot.")

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # If frame is read correctly
            if ret:
                # Add text overlay with credit
                cv2.putText(
                    frame,
                    "PoC by Mr. Sabaz Ali Khan",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),  # Green text
                    2,
                )

                # Display the frame
                cv2.imshow("ZeroDay Webcam PoC", frame)

                # Handle key presses
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    print("[+] Exiting PoC.")
                    break
                elif key == ord('s'):
                    # Save snapshot with timestamp
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"snapshot_{timestamp}.jpg"
                    cv2.imwrite(filename, frame)
                    print(f"[+] Snapshot saved as {filename}")

            else:
                print("[-] Error: Failed to capture frame.")
                break

    except Exception as e:
        print(f"[-] An error occurred: {str(e)}")

    finally:
        # Release webcam and close windows
        cap.release()
        cv2.destroyAllWindows()
        print("[+] Webcam released and resources cleaned up.")

if __name__ == "__main__":
    webcam_poc()