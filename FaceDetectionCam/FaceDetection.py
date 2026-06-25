#Face Detection Projects Using OpenCV Python Project 
import cv2

face_capture = cv2.CascadeClassifier("C:/Users/Hp/AppData/Local/Programs/Python/Python314/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)


while True :
    ret , video_info = video_capture.read()
    col = cv2.cvtColor(video_info,cv2.COLOR_BGR2GRAY)

    faces = face_capture.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    #creating rectangular Box 
    for (x,y,w,h) in faces:
        cv2.rectangle(video_info,(x,y),(x+w,y+h),(0,255,0),2)

    if not ret:
        print("Frame not received")
        break

    cv2.imshow("Face Detection CAM ",video_info) 
    if cv2.waitKey(10) == ord("a"): #This is for closeing the video using char a
        break

    if cv2.getWindowProperty("Face Detection CAM ", cv2.WND_PROP_VISIBLE) < 1:
        break

video_capture.release()
cv2.destroyAllWindows()
