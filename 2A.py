import cv2

def foto(sumber):
    cv2.imwrite('hasil/nuur.png', sumber)

cap = cv2.VideoCapture(1)
while(True):
    ret, frame = cap.read() 
    cv2.imshow('WebCam',frame)
    if cv2.waitKey(1) == ord('Q'):
        break
    elif cv2.waitKey(1) == ord('K'):
        foto(frame)
