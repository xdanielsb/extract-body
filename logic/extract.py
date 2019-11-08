""" Class responsible to extract the body given
    the temperature image."""
import cv2
from matplotlib import pyplot as plt
import numpy as np

class Extract:
    def __init__( self, pathReal , pathTemp  ):
        self.imgReal = self.readImage( pathReal )
        self.imgTemp = self.readImage( pathTemp )
        self.nameWindow = 'ImageW1'

    def readImage(self, path, tt=1):
        return cv2.imread( path, tt)

    def togray( self, img ):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray

    def showImage(self, img):
        cv2.namedWindow(self.nameWindow,cv2.WINDOW_NORMAL)
        cv2.resizeWindow(self.nameWindow, 300, 700)
        cv2.imshow(self.nameWindow , img)
        cv2.waitKey(0)

    def histogram( self, img):
        bins = 256
        range_scale = [0,254]
        nivel_transparencia = 0.5
        plt.hist(img.ravel(),bins,range_scale, label="histogram", alpha=nivel_transparencia);
        plt.legend(loc='upper right')
        plt.show()

    def canny( self, img):
        img = togray( img )
        res = cv2.Canny( img ,480,500)
        return res

    def removeBlue(self, img):
        lower = np.array([0,30,255])
        upper = np.array([255,255,255])
        mask = cv2.inRange(img, lower, upper)
        res = cv2.bitwise_and(img, img, mask= mask)  #-- Contains pixels having the gray color--
        # res = cv2.bitwise_or(img, img, mask= mask)  #-- Contains pixels having the gray color--
        return res
