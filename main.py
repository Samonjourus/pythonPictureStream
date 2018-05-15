#import numpy as np
import cv2

vis = cv2.VideoCapture(0);

while(vis.isOpened()):
    s, img = vis.read();

    if s:
        cv2.imwrite("feed.jpeg",img);
        cv2.namedWindow('display',cv2.WINDOW_AUTOSIZE);
        cv2.imshow('display',img);
        cv2.waitKey(1);
    else:
        break
vis.release();
cv2.destroyAllWindows();
