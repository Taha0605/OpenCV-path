import numpy as np
import cv2

image = cv2.imread("Edge Detection/tiger.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_blur = cv2.GaussianBlur(src=image, ksize=(3,3), sigmaX=0, sigmaY=0)

'''
###################### Sobel Edge Detection ####################

# A sobel kernel is [-1 0 1] which is the gradient vector in X-direction. Its transpose is for the Y-direction
#                   [-2 0 2]
#                   [-1 0 1]


sobel_X = cv2.Sobel(src=image_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # X-direction, vertical edges
sobel_Y = cv2.Sobel(src=image_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Y-direction, horizontal edges
sobel_XY = cv2.Sobel(src=image_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # X and Y directions

cv2.imshow("Vertical", sobel_X)
cv2.imshow("Horizontal", sobel_Y)
cv2.imshow("Both", sobel_XY)

cv2.waitKey(0)
#################################################################
'''
######################## Canny Edge Detection ############################3

## here we blur the image first, find the gradient intensity from sobel, perform non-maximum suppression and then thresholding
# non-maximum suppression- if the gradient intensity maximum is greater than the maximum of the neigbouring pixels, its okay, otherwise it is made 0
# hysteresis threshold- upper threshold for strong edges, lower threshold for weaker edges, anything in between is checked if it is connected to a strong edge and only then it is okay

edges = cv2.Canny(image=image_blur, threshold1=100, threshold2=200)

cv2.imshow('Canny', edges)
cv2.waitKey(0)




 

cv2.destroyAllWindows()