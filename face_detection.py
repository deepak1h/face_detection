import cv2

face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
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
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 200), 2)

    cv2.imshow('output detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()