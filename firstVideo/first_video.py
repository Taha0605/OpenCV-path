import cv2
vid_capture = cv2.VideoCapture('firstVideo/earthrotate.mp4')
# ret, frame = vid_capture.read()
# cv2.imshow('Frame', frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
######################### Reading a Video #########################


if vid_capture.isOpened() == False:
    print("Error opening the file")
else:
    fps = vid_capture.get(5)
    print('Frame Rate::{}'.format(fps))
    frame_count = vid_capture.get(7)
    print('Frame Count::{}'.format(frame_count))

while vid_capture.isOpened():
    ret, frame = vid_capture.read()
    if ret==True:
        cv2.imshow('Frame', frame)
        key = cv2.waitKey(20)
        if key == ord('q'):
            break
    else:
        break

vid_capture.release()
cv2.destroyAllWindows()



######################### Writing to a Video #########################


# getting original video dimensions

# width = int(vid_capture.get(3))
# height = int(vid_capture.get(4))
# size = (width, height)
# fps=20

# output = cv2.VideoWriter('firstVideo/earthrotateByMe.mp4', cv2.VideoWriter_fourcc(*'XVID'), 5, size) # ('M','J','P','G') arguments for an avi output

# while vid_capture.isOpened():
#     ret,frame = vid_capture.read()
#     if ret == True:
#         output.write(frame)
#     else:
#         print('Stream Disconnected')
#         break

# vid_capture.release()
# output.release()

