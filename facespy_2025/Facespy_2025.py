import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime
import csv

# Banner display
print("""
============================================================
          FaceSpy 2025 - Advanced Face Recognition
============================================================
Coded by: Pakistani Ethical Hacker Mr. Sabaz Ali Khan
============================================================
""")

# Function to load known face encodings from a directory
def load_known_faces(known_faces_dir):
    known_face_encodings = []
    known_face_names = []
    for filename in os.listdir(known_faces_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(known_faces_dir, filename)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_face_encodings.append(encodings[0])
                known_face_names.append(os.path.splitext(filename)[0])
    return known_face_encodings, known_face_names

# Function to log recognized faces to a CSV file
def log_recognition(name):
    with open('recognition_log.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([name, timestamp])

# Main function
def main():
    # Create directory for known faces if it doesn't exist
    known_faces_dir = 'known_faces'
    if not os.path.exists(known_faces_dir):
        os.makedirs(known_faces_dir)
        print("Created 'known_faces' directory. Please add images of known individuals.")
        return

    # Load known faces
    known_face_encodings, known_face_names = load_known_faces(known_faces_dir)
    if not known_face_encodings:
        print("No known faces found in 'known_faces' directory. Please add images.")
        return

    # Initialize webcam
    video_capture = cv2.VideoCapture(0)
    if not video_capture.isOpened():
        print("Error: Could not open webcam.")
        return

    # Create CSV log file if it doesn't exist
    if not os.path.exists('recognition_log.csv'):
        with open('recognition_log.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Name', 'Timestamp'])

    print("Starting FaceSpy 2025... Press 'q' to quit.")

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Convert the image from BGR (OpenCV) to RGB (face_recognition)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find all faces and face encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Loop through each face found in the frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            
            # Find the best match
            if len(face_distances) > 0:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index] and face_distances[best_match_index] < 0.6:
                    name = known_face_names[best_match_index]
                    log_recognition(name)

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Draw a label with the name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting frame
        cv2.imshow('FaceSpy 2025', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
