import numpy as np
import cv2
from sklearn.feature_extraction import img_to_graph

img = cv2.imread('Background_Whitener/CloseupKeychain.jpg')
img_grayscale = cv2.imread('Background_Whitener/CloseupKeychain.jpg', 0)

thresh = 150
maxValue = 255
th, dst = cv2.threshold(img_grayscale, thresh, maxValue, cv2.THRESH_BINARY)

temp = np.stack((dst,)*3, axis=-1)
cv2.imshow("ThreshGray", temp)
overlay = cv2.addWeighted(img, 1.25, temp, 0.2, 0)
cv2.imshow("IMAGE", overlay)

thresh = 250
th2, dst2 = cv2.threshold(overlay, thresh, maxValue, cv2.THRESH_BINARY)
cv2.imshow("Litmus Test", dst2)

cv2.imwrite("Background_Whitener/FixedBackground2.jpg", overlay)

cv2.waitKey(0)
cv2.destroyAllWindows()