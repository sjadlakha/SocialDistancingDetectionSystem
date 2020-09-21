import cv2
import os


person_cascade = cv2.CascadeClassifier(
    os.path.join('/Users/sahajadlakha/Documents/DEV_ZONE/SocialDistancingDetectionSystem/Data/haarcascade_fullbody_copy.xml'))
# person_cascade = cv2.CascadeClassifier(
#     os.path.join('/Users/sahajadlakha/Documents/DEV_ZONE/SocialDistancingDetectionSystem/Data/pedestrain.xml'))
cap = cv2.VideoCapture(
    '/Users/sahajadlakha/Documents/DEV_ZONE/SocialDistancingDetectionSystem//Data/pedestrians.avi')
# cap=cv2.VideoCapture(0)
while True:
    r, frame = cap.read()
    if r:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        rects = person_cascade.detectMultiScale(gray_frame)

        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("Video", frame)
    k = cv2.waitKey(1)
    if k%256 == 27:  # Exit condition
        break

cap.release()
cv2.destroyAllWindows()

# part left is to calculate the distance between people!
