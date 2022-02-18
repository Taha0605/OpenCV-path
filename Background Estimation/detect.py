import numpy as np

import cv2

cap = cv2.VideoCapture('Background Estimation/video.mp4')

frameIDs = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)
print('Size of frameIDs: {}'.format(frameIDs.shape))

frames=[]
for fid in frameIDs:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    # print('Size of frame: {}'.format(frame.shape))
    frames.append(frame)

medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)

cv2.imshow("Background", medianFrame)
cv2.waitKey(0)

# Reset frame number to 0
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

# Convert background to grayscale
grayMedianFrame = cv2.cvtColor(medianFrame, cv2.COLOR_BGR2GRAY)

# Loop over all frames
ret = True
while(ret):

  # Read frame
  ret, frame = cap.read()
  # Convert current frame to grayscale
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  # Calculate absolute difference of current frame and 
  # the median frame
  dframe = cv2.absdiff(frame, grayMedianFrame)
  # Treshold to binarize
  th, dframe = cv2.threshold(dframe, 30, 255, cv2.THRESH_BINARY)
  # Display image
  cv2.imshow('frame', dframe)
  cv2.waitKey(20)

# Release video object
cap.release()

# Destroy all windows
cv2.destroyAllWindows()
