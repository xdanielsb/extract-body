""" This is the launcher of the application."""
from  logic.extract import *
import numpy as np
if __name__ == "__main__":
    print("The application has started.")
    pathReal = "assets/images/color_image.jpg"
    pathTemp = "assets/images/depth_image_colored.jpg"
    e = Extract( pathReal, pathTemp)

    im = e.imgTemp
    img = im.copy()
    _, thr= cv2.threshold(e.togray( im ) ,100,255,cv2.THRESH_BINARY)
    (_, contours, _) = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    possible_contours = []
    for i in range( 0, len(contours)):
        areaC  = cv2.contourArea( contours[i] )
        if( areaC > 150000):
            white = (255, 255, 255)
            cv2.drawContours(im, contours, i , white, -1)
            rows, cols , _= im.shape
            add, npixels = 0, 0
            for row in range( rows ):
                for col in range( cols ):
                    if(sum(im[row][col]) == 255*3):
                        add += img[row][col][0]
                        npixels += 1
            if( add > 50 ):
                possible_contours.append( contours[i])

    trans = np.load('assets/calibration/T_color_to_depth_extrinsic.npy')
    print( trans )
    # choose possible bodies
    imr = e.imgReal
    rows, cols, _ = imr.shape
    for row in range( rows ):
        for col in range( cols ):
            pass


    e.showImage( im )
