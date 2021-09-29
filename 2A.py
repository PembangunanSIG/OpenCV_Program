import cv2
cap = cv2.VideoCapture(0)

def webcam():
    while(True):
        ret, frame = cap.read() 
        cv2.imshow('WebCam',frame)
        cv2.waitKey(1)
        return frame

webcam()