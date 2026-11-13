import cv2

cap = cv2.VideoCapture('../videos/road.mp4')

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('../outputs/out.mp4', cv2.VideoWriter_fourcc(*'mp4v'),fps, (width,height))

while True:
    ret, frame = cap.read()
    if not ret:
        print('cannot read the frame')
        break
    cv2.rectangle(frame,(100,100),(300,250),(0,0,255), 3)
    out.write(frame)
    
cap.release()
out.release()