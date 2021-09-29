import cv2
cap = cv2.VideoCapture("foto/regis.mp4")

while(True):
    ret, frame = cap.read() 
    cv2.imshow('frame',frame)
    cv2.waitKey(25)