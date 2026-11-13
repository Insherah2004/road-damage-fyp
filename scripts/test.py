import cv2
cap = cv2.VideoCapture(0)  # open webcam


while True:
    ret, frame = cap.read()  # read the frame
    
    if not ret:
        print("cannot read the frame")
        break
    
    cv2.imshow('my webcam', frame)
    
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        print('quitting...')
        break

cap.release()
cv2.destroyAllWindows()

