import cv2

img_grayscale = cv2.imread('firstImage/test.jpg', 0) # 0 or cv2.IMG_GRAYSCALE is the variable

cv2.imshow('grayscale image', img_grayscale)

cv2.waitKey(0) #0 means that the window will close after a key is pressed only, otherwise it indicates the time in milliseconds before window is destroyed

cv2.destroyAllWindows()

cv2.imwrite('grayscale.jpg', img_grayscale)