import numpy as np
import cv2
import glob

# Termination criteria for the iterative algorithm used by cornerSubPix
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)  # It tells the function to stop either after 30 iterations or when the corner position moves by less than 0.001 between iterations, whichever comes first

# Prepare object points (like (0,0,0), (1,0,0), (2,0,0), ..., assuming a checkerboard)

square_size = 22.0
checkerboard_size = (8, 11)   #  number of internal intersections where the corners of the squares meet in width and height, use 8,11
objp = np.zeros((checkerboard_size[0]*checkerboard_size[1], 3), np.float32)   # size 7 columns 6 rows shape - 42 x 3
objp[:,:2] = np.mgrid[0:checkerboard_size[0], 0:checkerboard_size[1]].T.reshape(-1, 2)* square_size    #  reshaped into a single array where each row contains the x and y coordinates of one corner (z always remain 0), becomes 42x3

# Arrays to store object points and image points from all the images
objpoints = []  # 3d point in real world space
imgpoints = []  # 2d points in image plane

images_path = r'path'

images = glob.glob(images_path)


# Step through the list and search for chessboard corners
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, checkerboard_size, None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        # Refine the corner positions
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, checkerboard_size, corners2, ret)
        display_size = (960, 540)  
        resized_img = cv2.resize(img, display_size)

        cv2.imshow('img', resized_img)
        cv2.waitKey(500)

cv2.destroyAllWindows()

# Camera calibration
if objpoints and imgpoints:  
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    np.savez('calibration_output.npz', ret=ret, mtx=mtx, dist=dist, rvecs=rvecs, tvecs=tvecs)

    # Print to stdout
    print("Camera Intrinsic matrix : \n")
    print(mtx)
    print("Distortion coefficients : \n")
    print(dist)
    # print("Translation Matrix : \n")
    # print(tvecs)
    # print("Rotation Matrix : \n")
    # print(rvecs)

    # Save the matrix and distortion coefficients to a file using:
    with open('calibration_parameters.txt', 'w') as f:
        f.write(f'Camera matrix:\n{mtx}\n')
        f.write(f'Distortion coefficients:\n{dist}\n')
        # f.write(f'Translation coefficients:\n{tvecs}\n')
        # f.write(f'Rotation coefficients:\n{rvecs}\n')
else:
    print("No points for calibration found. Make sure the images have detectable chessboard corners.")