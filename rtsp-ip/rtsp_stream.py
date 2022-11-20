# ---------------------------- #
# Real Time Streaming Protocol #
# Python Automation & Security #
# Auth: Ky1o P (cywf) -------- #
# Date: Nov 20, 2022 --------- #
# ---------------------------- #

import cv2 

video = cv2.VideoCapture("rtsp://<user_name>:<password>@<ip_address>:554/Streaming/Channels/401")

while True:
    _,frame = video.read()      # read from the video capture object
    cv2.imshow("RTSP",frame)    # use 'imshow' method to display the stream
    k = cv2.waitKey(1)          # provides us with a delay
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()