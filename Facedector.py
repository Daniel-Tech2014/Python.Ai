import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap= cv2.VideoCapture(0)
if not cap.isOpend():
    print("Error: Could not open camera")
    exit()
while True:
    ret, frame = cap.read()
    if  not ret:
     print("Error: Failed to capture image")
     break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces =face_cascade.detectMultiscale(gray, ScaleFactor=1.1, mineNeighbors=5, minisize=(30,30))
    for (x,y,w,h) in faces:
        cv2.rectangle (frame, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow('Face Detection press q to quit', frame)
    if cv2.waitkey(1) & 0xFF == ord('q'):
       break
cap.release()
cv2.destroyAllWindows()























