import numpy as np
import cv2

image = cv2.imread("Filtering/wood.jpg")

# filter = np.array([ #image remains identical
#     [0, 0, 0],
#     [0, 1, 0],
#     [0, 0, 0]
# ], np.float32)

filter = np.ones((5,5), np.float32)/25 #normalized blurring

filter = np.array([ #sharpens the image
    [0, -1, 0],
    [-1,  5, -1],
    [0, -1, 0]
])

# blurred_image = cv2.blur(src=image, ksize=(5,5))
gaussian_blurred = cv2.GaussianBlur(src=image, ksize=(5,5), sigmaX= 0, sigmaY=0)

bilateral_filter = cv2.bilateralFilter(src=image, d=9, sigmaColor=75, sigmaSpace=75) #blurs but also keeps the edges sharp

filtered_image = cv2.filter2D(src=image, ddepth=-1, kernel=filter)

cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered_image)
cv2.imshow('Gaussian Image', gaussian_blurred)
cv2.imshow('Bilateral Filtered', bilateral_filter)


cv2.waitKey(0)
cv2.destroyAllWindows()