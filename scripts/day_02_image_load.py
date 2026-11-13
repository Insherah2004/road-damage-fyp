import cv2

image = cv2.imread('../images/image01.jpg') # loading image 

if image is None:
    print('cant read image')
else:    
    print(image.shape)

cv2.imshow('image_01', image)

resized = cv2.resize(image, (640, 480))
cv2.imshow('resized', resized)

crop = image[100:300, 200:400]
cv2.imshow('cropped', crop)

cv2.waitKey(0)
cv2.destroyAllWindows()