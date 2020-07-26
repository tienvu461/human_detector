import numpy as np
import cv2
import constant
import logging
import datetime
import time
import os

FPS_LIMIT = 0.5

IMG_PATH = "E:\python_prjs\human_detector\human_detector\captured_img"
LOGGER = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)
# LOGGER.setLevel(logging.DEBUG)


def run():
    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    capture = cv2.VideoCapture(constant.my_stream, cv2.CAP_FFMPEG)

    startTime = time.time()
    # capture = cv2.VideoCapture("vi_10.mp4")
    # the output will be written to output.avi
    # out = cv2.VideoWriter(
    #     'output.avi',
    #     cv2.VideoWriter_fourcc(*'MJPG'),
    #     15.,
    #     (640, 480))

    while True:
        start = datetime.datetime.now()
        # Capture frame-by-frame
        ret, frame = capture.read()

        nowTime = time.time()
        if ((nowTime - startTime)) > FPS_LIMIT:
            # resizing for faster detection
            frame = cv2.resize(frame, (640, 360))
            # using a greyscale picture, also for faster detection
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

            # detect people in the image
            # returns the bounding boxes for the detected objects
            boxes, weights = hog.detectMultiScale(
                frame, winStride=(8, 8), padding=(8, 8))
            LOGGER.debug("boxes = {}".format(boxes))
            LOGGER.debug("weights = {}".format(weights))
            boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
            for (xA, yA, xB, yB) in boxes:
                # display the detected boxes in the colour picture
                cv2.rectangle(frame, (xA, yA), (xB, yB),
                              (0, 255, 0), 2)
            # cv2.imwrite(index + 1,frame)
            # Write the output video
            # out.write(frame.astype('uint8'))
            # Display the resulting frame
            LOGGER.info("detection took: {}s".format(
                (datetime.datetime.now() - start).total_seconds()))
            # break
            try:
                if weights[0][0] > 0.5:
                    cv2.imshow('frame', frame)
                    cv2.imwrite(os.path.join(
                        IMG_PATH, str(time.time()) + ".jpg"), frame)
            except:
                print('a')

            startTime = time.time()  # reset time

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    capture.release()
    # and release the output
    # out.release()
    # finally, close the window
    cv2.destroyAllWindows()
    cv2.waitKey(1)
