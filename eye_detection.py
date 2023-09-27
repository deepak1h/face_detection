import cv2  
  
face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye = cv2.CascadeClassifier('haarcascade_eye.xml')  
# capture from a camera 
cap = cv2.VideoCapture(0)
while True:  
    ret, frame = cap.read()  
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Check if the frame was successfully captured
    if not ret:
        break
  
    faces = face.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(35, 35)
    )
  
    for (x,y,w,h) in faces:  
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)  
        rec_eye = gray[y:y+h, x:x+w] 
        col_eye = frame[y:y+h, x:x+w] 
  
        # Detects eyes of different sizes
        eyes = eye.detectMultiScale(rec_eye)  
  
        #draw rectangle
        for (ex,ey,ew,eh) in eyes: 
           cv2.rectangle(col_eye,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 
  
    # Display an image in a window 
    cv2.imshow('eye detection',frame) 
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
