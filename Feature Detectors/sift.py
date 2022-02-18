import numpy as np
import cv2 as cv

#SIFT implementation
ori = cv.imread('Feature Detectors/eiffel.jpg', 1)
img = ori.copy()
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
sift = cv.SIFT_create()
kp, des = sift.detectAndCompute(gray,None)
img=cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('Original',ori) 
cv.imshow('SIFT', img)
cv.waitKey(0)

#SURF implementation
# img = ori.copy()
# surf = cv.xfeatures2d.SURF_create()
# kp, des = surf.detectAndCompute(img,None)
# img2 = cv.drawKeypoints(img,kp,None,(255,0,0),4)
# cv.imshow('SURF', img2)
# cv.waitKey(0)

#BRIEF implementation
# img = ori.copy()
# star = cv.xfeatures2d.StarDetector_create()
# brief = cv.xfeatures2d.BriefDescriptorExtractor_create()
# kp = star.detect(img,None)
# kp, des = brief.compute(img, kp)
# print( brief.descriptorSize() )
# print( des.shape )
# img2 = cv.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)
# cv.imshow('BRIEF', img2)
# cv.waitKey(0)

#ORB implementation 
img = ori.copy()
orb = cv.ORB_create(nfeatures=200)
kp = orb.detect(img, None)
kp, des = orb.compute(img, kp)
img2 = cv.drawKeypoints(img, kp, None, color=(0, 255, 0), flags=0)
cv.imshow('ORB', img2)
cv.waitKey(0)

cv.destroyAllWindows()