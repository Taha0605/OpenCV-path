import cv2

src1 = cv2.imread('Masking/grayscale.jpg')
src2 = cv2.imread('Masking/transport.png')

src2 = cv2.resize(src2, src1.shape[1::-1])

something = cv2.inRange()
final_image = cv2.bitwise_and(src1, src2)

cv2.imshow("SRC1", src1)
cv2.imshow("SRC2", src2)

cv2.imshow('Added Images', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()