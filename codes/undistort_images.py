import cv2
import glob
import os
import numpy as np

with np.load('calibration_output.npz') as X:
    mtx, dist = [X[i] for i in ('mtx','dist')]

input_directory = r"pathtoyourimages"
output_directory = r"[athforundistortedimages"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

images = glob.glob(os.path.join(input_directory, '*.jpg'))  

for idx, fname in enumerate(images):
    img = cv2.imread(fname)
    h, w = img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]

    output_fname = os.path.join(output_directory, f'undistorted_{idx}.jpg')
    cv2.imwrite(output_fname, dst)

print(f"Undistorted images are saved to {output_directory}")
