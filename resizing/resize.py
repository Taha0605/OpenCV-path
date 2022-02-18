import cv2

image = cv2.imread('resizing/test.jpg', 1)
cv2.imshow('Original Image', image)
height, width, channels = image.shape
print('{}, {}'.format(width, height))

upheight = height + 500
upwidth  = width + 500
upsize = (upwidth, upheight)
resized_up = cv2.resize(image, upsize, interpolation= cv2.INTER_LINEAR)

downheight = height - 100
downwidth = width - 100
downsize = (downwidth, downheight)
resized_down = cv2.resize(image, downsize, interpolation= cv2.INTER_LINEAR) 

# using a scaling method
# scale_down_x, scale_down_y = 1.5, 1.2 say
# resized_down = cv2.resize(image, None, fx=scale_down_x, fy=scale_down_y, interpolation= cv2.INTER_LINEAR) 

cv2.imshow('Image resized UP', resized_up)
cv2.imshow('Image resized DOWN', resized_down)
cv2.waitKey(0)
cv2.destroyAllWindows()



