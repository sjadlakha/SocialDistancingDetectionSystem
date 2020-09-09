import cv2
import sys
import numpy as np

# Path to Trained xml haar_cascade File

bodyCascadeClassifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_upperbody.xml')

videoStream = cv2.VideoCapture(0)

while True:
    ret, frame = videoStream.read()

    # Preprocessing

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    k = cv2.waitKey(1)

    bodies = bodyCascadeClassifier.detectMultiScale(gray,
            scaleFactor = 1.1,
            minNeighbors = 3)
    
    # Extracting boundary rectangles

    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # display Footage

    cv2.imshow('Bodies Detected', frame)

    # End detection on "esc" key press
    if k%256 == 27:
        break

videoStream.release()
cv2.destroyAllWindows()

