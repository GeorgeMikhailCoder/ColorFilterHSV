import cv2
from time import sleep
import numpy as np


def nothing(*arg):
    pass
if __name__ == '__main__':
    cameraSource = 'http://homecam:15243@192.168.43.1:8080/video'
    cameraSource =0
    video_capture = cv2.VideoCapture(cameraSource)

    cv2.namedWindow("settings")
    cv2.createTrackbar('h1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
    cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
    cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
    cv2.createTrackbar('v2', 'settings', 255, 255, nothing)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Camera offline. Next frame in 10 sec")
            sleep(10)
            print("Try to accept next frame")
        else:
            cv2.imshow("frame",frame)
            hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV )

            h1 = cv2.getTrackbarPos('h1', 'settings')
            s1 = cv2.getTrackbarPos('s1', 'settings')
            v1 = cv2.getTrackbarPos('v1', 'settings')
            h2 = cv2.getTrackbarPos('h2', 'settings')
            s2 = cv2.getTrackbarPos('s2', 'settings')
            v2 = cv2.getTrackbarPos('v2', 'settings')

            hsv_min = np.array((h1, s1, v1), np.uint8)
            hsv_max = np.array((h2, s2, v2), np.uint8)
            thresh = cv2.inRange(hsvFrame, hsv_min, hsv_max)


            cv2.imshow("win", thresh)

            if cv2.waitKey(1) & 0xFF == 27:
                break



