import cv2
import os
import math
from paths import paths

def minimumDistance(rects, m):
    if len(rects) >= 2:
        md = []
        for (x1, y1, w1, h1) in rects:
            pt1 = (x1+w1/2, y1+h1/2)
            for (x2, y2, w2, h2) in rects:
                if x1 != x2 and y1 != y2 and w1 !=w2 and h1 != h2:
                    pt2 = (x2+w2/2, y2+h2/2)
                    d = math.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
                    md.append(d)
        if len(md) > 0:
            if min(md) < m:
                print("People are not following social distancing")
                


def humanDetection(minD):
    person_cascade = cv2.CascadeClassifier(
        os.path.join(paths['full_body_haarcascade_file']))

    cap = cv2.VideoCapture(
        paths['video_source'])
    while True:
        r, frame = cap.read()
        if r:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            rects = person_cascade.detectMultiScale(gray_frame)

            for (x, y, w, h) in rects:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            print(minD)
            minimumDistance(rects, minD)

            
            cv2.imshow("Video", frame)
        k = cv2.waitKey(1)
        if k%256 == 27:  # Exit condition
            break

    cap.release()
    cv2.destroyAllWindows()
