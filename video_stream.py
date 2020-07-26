import cv2
import os

from constant import IP, PORT, USERNAME, PASSWORD

# cv2.startWindowThread()
# cap = cv2.VideoCapture(0)

# while(True):
#     # reading the frame
#     ret, frame = cap.read()
#     # displaying the frame
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         # breaking the loop if the user types q
#         # note that the video window must be highlighted!
#         break

# cap.release()
# cv2.destroyAllWindows()
# # the following is necessary on the mac,
# # maybe not on other platforms:
# cv2.waitKey(1)
# os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

# rtsp://admin:tien2020@192.168.100.9:554/onvif1
URL = 'rtsp://{}:{}@{}:{}/onvif1'.format(USERNAME, PASSWORD, IP, PORT)
print('Connecting to: ' + URL)

vcap = cv2.VideoCapture(
    "rtsp://admin:tien2020@192.168.100.9:554/onvif1", cv2.CAP_FFMPEG)

while(1):
    ret, frame = vcap.read()
    if ret == False:
        print("Frame is empty")
        break
    else:
        cv2.imshow('VIDEO', frame)
    cv2.waitKey(1)


# cam = cv2.VideoCapture(URL, cv2.CAP_FFMPEG)
