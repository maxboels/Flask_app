import cv2


img = cv2.imread("opencv/hearth.jpg", 1)
print(img.shape)
img = cv2.resize(img, (0,0), fx=0.1, fy=0.1)

# BGR default
cv2.imshow('Image', img)
cv2.waitKey(0) #wait infinate amount of time with 0
cv2.destroyAllWindows()




















