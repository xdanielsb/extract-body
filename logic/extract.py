""" Class responsible to extract the body given
    the temperature image."""
import cv2 
from matplotlib import pyplot as plt
import numpy as np

class Extract:
    def __init__( self, pathReal , pathTemp ):
        self.imgReal = self.readImage( pathReal)
        self.imgTemp = self.readImage( pathTemp )

    def readImage(self, path):
        return cv2.imread( path, 1)

    def showImage(self, img):
        cv2.imshow("Image" , img)
        cv2.waitKey(0)

    def histogram( self, img):
        bins = 256
        range_scale = [0,254]
        nivel_transparencia = 0.5
        plt.hist(img.ravel(),bins,range_scale, label="histogram", alpha=nivel_transparencia);
        plt.legend(loc='upper right')
        plt.show()

    def removeBlue(self, img):
        lower = np.array([0,0,0])  #-- Lower range --
        upper = np.array([127,127,127])  #-- Upper range --
        mask = cv2.inRange(img, lower, upper)
        res = cv2.bitwise_and(img, img, mask= mask)  #-- Contains pixels having the gray color--
        return res
