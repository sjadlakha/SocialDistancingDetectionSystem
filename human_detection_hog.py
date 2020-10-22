import cv2
from paths import paths
import numpy as np

def detect(frame):
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    bounding_box_cordinates, weights = HOGCV.detectMultiScale(
        frame, winStride=(4, 4), padding=(8, 8), scale=1.03)
    
    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return frame

def humanDetector():
    video = cv2.VideoCapture(paths['video_source'])

    while True:
        check, frame = video.read()
        frame = cv2.resize(frame, (720, 480))
        frame = detect(frame)

        key = cv2.waitKey(1)
        if key % 256 == 27:
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    

    humanDetector()

