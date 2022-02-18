import numpy as np
import cv2

image = cv2.imread("Transformations/transport.png")

height, width = image.shape[:2]

image_copy = image.copy()
pointA = (200,80)
pointB = (450,80)

cv2.line(image_copy, pointA, pointB, (0, 0, 255), thickness = 3)

cv2.imshow("Line", image_copy)
cv2.waitKey(0)

#################### Rotating an image ######################

rotation_matrix = cv2.getRotationMatrix2D(center=(width/2,height/2), angle=45, scale=1)

rotated_matrix = cv2.warpAffine(image, rotation_matrix, dsize=(width, height))

#################### Translating an image ###################

# get tx and ty values for translation
# you can specify any value of your choice
tx, ty = width / 4, height / 4

# create the translation matrix using tx and ty, it is a NumPy array 
translation_matrix = np.array([
    [1, 0, tx],
    [0, 1, ty]
], dtype=np.float32)

# apply the translation to the image
translated_image = cv2.warpAffine(src=image, M=translation_matrix, dsize=(width, height))


cv2.imshow("Original image", image)
cv2.imshow("Rotated Image", rotated_matrix)
cv2.imshow("Translated Image", translated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()