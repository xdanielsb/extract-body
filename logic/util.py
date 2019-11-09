"""
    Class in charge of provide some Utilitary functions.
"""

import cv2

class Util:
    WHITE = (255,255,255)
    NAME_WINDOW = 'IMG_SHOW'
    def __init__(self):
        pass

    def readImage(self, path, tt=1):
        """
            Read an image given a path
            tt, mean if you want to read in {color, black}
        """
        return cv2.imread( path, tt)

    def showImage(self, img):
        """
            Display an image in the screen, until
            the user press a key.
        """
        cv2.namedWindow(self.NAME_WINDOW,cv2.WINDOW_NORMAL)
        cv2.resizeWindow(self.NAME_WINDOW, 300, 700)
        cv2.imshow(self.NAME_WINDOW , img)
        cv2.waitKey(0)

    def togray( self, img ):
        """
            Change an image to gray scale
        """
        if( len(img.shape) == 2): return img
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray

    def getHistogram( self, img):
        """
            Function that help me to get the histogram
            Phantom code, at the end, useful to spot some
            futures at the begining, distribution of color
        """
        bins = 256
        range_scale = [0,254]
        nivel_transparencia = 0.5
        plt.hist(img.ravel(),bins,range_scale, label="histogram", alpha=nivel_transparencia);
        plt.legend(loc='upper right')
        plt.show()

    def applyCanny( self, img):
        """
            Function to apply canny filter
        """
        img = togray( img )
        res = cv2.Canny( img ,480,500)
        return res

    def fillContour( self, img, contours, i):
        """
            Given a contour, an an image fill that contour with white color
            in the image
        """
        cv2.drawContours(img, contours, i , self.WHITE, -1)

    def removeBlue(self, img):
        """
            Function that helps to remove a certain gama of
            colors. Phantom code now.
        """
        lower = np.array([0,30,255])
        upper = np.array([255,255,255])
        mask = cv2.inRange(img, lower, upper)
        res = cv2.bitwise_and(img, img, mask= mask)
        return res

    def applyThresh(self, im, mi=100, ma=255):
        """
            Function that helps to apply a thresh.
        """
        if( len(im.shape) == 3):
            _, thr= cv2.threshold(self.togray( im ) ,mi,ma,cv2.THRESH_BINARY)
        else:
            _, thr= cv2.threshold(im  ,mi,ma,cv2.THRESH_BINARY)
        return thr

    def getContours( self,img ):
        """
            Function that helps to get the contours
        """
        if( len(img.shape) == 3):
            (_, contours, _) = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        else:
            (contours,_) = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours
