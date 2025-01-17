import cv2
video=cv2.VideoCapture(1)
while True:
    bol,frame=video.read()
    cv2.imshow('video',frame)
    if cv2.waitKey(1)&0xFF==ord('d'):
        break
video.release()
cv2.destroyAllWindows()