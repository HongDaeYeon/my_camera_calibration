import cv2 as cv
import numpy as np

# Load calibration results
K = np.array([[944.53574431, 0, 345.32015375],
              [0, 876.31371825, 644.90248486],
              [0, 0, 1]])
dist_coeff = np.array([9.49929521e-02, 3.11662831e+00, -3.88910029e-02, -4.50227023e-03, -4.06874417e+01])

# Open the video file
video = cv.VideoCapture("chessboard.avi")
map1, map2 = None, None
while True:
    valid, img = video.read()
    if not valid:
        break
    
    if map1 is None or map2 is None:
        map1, map2 = cv.initUndistortRectifyMap(K, dist_coeff, None, None, (img.shape[1], img.shape[0]), cv.CV_32FC1)
    
    img_rectified = cv.remap(img, map1, map2, interpolation=cv.INTER_LINEAR)
    
    cv.imshow("Rectified", img_rectified)
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()
