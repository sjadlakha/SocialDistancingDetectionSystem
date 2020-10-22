import cv2
import os
import math

person_cascade = cv2.CascadeClassifier(
    os.path.join('/Users/sahajadlakha/Documents/DEV_ZONE/SocialDistancingDetectionSystem/Data/haarcascade_fullbody_copy.xml'))

cap = cv2.VideoCapture(
    '/Users/sahajadlakha/Documents/DEV_ZONE/SocialDistancingDetectionSystem/Data/vid.mp4')
# cap=cv2.VideoCapture(0)
while True:
    r, frame = cap.read()
    if r:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        rects = person_cascade.detectMultiScale(gray_frame)

        for (x, y, w, h) in rects:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Calculating the minimum distance between the rectangles 
        if len(rects) >= 2:
            md = []
            for (x1,y1,w1,h1) in rects:
                pt1 = (x1+w1/2, y1+h1/2)
                for (x2,y2,w2,h2) in rects:
                    if x1!=x2 and y1!=y2 and w1!=w2 and h1!=h2:
                        pt2 = (x2+w2/2, y2+h2/2)
                        d = math.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
                        print(d)
                        md.append(d)
            if len(md) > 0:
                print(md, min(md), len(rects))


        cv2.imshow("Video", frame)
    k = cv2.waitKey(1)
    if k % 256 == 27:  # Exit condition
        break

cap.release()
cv2.destroyAllWindows()
