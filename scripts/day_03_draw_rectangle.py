import cv2

img = cv2.imread('../images/image03.jpg')

if img is None:
    print('could not read image')
else:
    
    
    #cv2.rectangle(img, (320,300),(450,430),(0,0,255),3)
    
    #cv2.putText(img, "pothole", (320,280), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
    
    cv2.rectangle(img, (300,160), (450,300), (255, 0, 0), 3)
    cv2.putText(img, 'pothole', (305, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
   
    
    cv2.imshow('image with text and rectangle', img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()