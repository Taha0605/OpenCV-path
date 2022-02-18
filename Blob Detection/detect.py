# import numpy as np
# import cv2

# image = cv2.imread('Blob Detection/hubble.jpg', cv2.IMREAD_GRAYSCALE)
# detector = cv2.SimpleBlobDetector()

# keypoints = detector.detect(image)

# marked_image = cv2.drawKeypoints(image, keypoints, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# cv2.imshow("Keypoints", marked_image)
# cv2.waitKey(0)

# Standard imports
import cv2
import numpy as np;

# Read image
im = cv2.imread("Blob Detection/blob.jpg", cv2.IMREAD_GRAYSCALE)

# Set up the detector with default parameters.
detector = cv2.ORB_create()

# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
