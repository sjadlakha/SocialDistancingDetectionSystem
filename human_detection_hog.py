import cv2
import sys
import imutils
import numpy as np

def detect(frame):
    HOGCV = cv2.HOGDescriptor()
    HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    bounding_box_cordinates, weights = HOGCV.detectMultiScale(
        frame, winStride=(4, 4), padding=(8, 8), scale=1.03)
    
    person = 1
    for x, y, w, h in bounding_box_cordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f'person {person}', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        person += 1
    
    # cv2.putText(frame, 'Status : Detecting ', (40, 40),
    #             cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0), 2)
    # cv2.putText(frame, f'Total Persons : {person-1}',
    #             (40, 70), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 0, 0), 2)
    # cv2.imshow('output', frame)

    return frame

def humanDetector():
    video = cv2.VideoCapture(
        '/Users/sahajadlakha/Documents/DEV_ZONE/SocialDistancingDetectionSystem/Data/pedestrians.avi')

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

# optimisation will be using haarcascade file