""" Class responsible to extract the body given
    the temperature image."""
import cv2
from matplotlib import pyplot as plt
import numpy as np
from .util import Util

class ExtractorBody:

    MIN_AREA_BODY  = 150000
    SUM_RGB_WHITE  = 255 * 3
    RED_THRESH     = 50
    DEPTH_SCALE    = 0.001
    RED_IDX        = 0
    BLUE_IDX       = 1

    def __init__( self, **kwargs ):
        self.util = Util()
        self.imgReal = self.util.readImage( kwargs["pathReal"] )
        self.imgTemp = self.util.readImage( kwargs["pathTemp"] )
        self.imgTempCopy = self.imgTemp.copy()
        self.mCamera = np.load(kwargs["mCamera"])
        self.mTrans = np.load(kwargs["mTrans"])
        self.rows, self.cols, _ = self.imgReal.shape
        self.mPre = np.dot( self.mCamera, self.mTrans)

    def undistort( self, img, dx=0, dy=0):
        for row in range( self.rows ):
            for col in range( self.cols ):
                aux = np.array([row, col, 0, 1])
                res = np.dot( self.mPre, aux)
                res = np.multiply( res, self.DEPTH_SCALE)
                res = res.astype(int)
                img[res[self.RED_IDX]+dx][res[self.BLUE_IDX]+dy] = img[row][col]

    def getAvgSumRedPixels( self, img):
        add, npixels =0., 0
        for row in range( self.rows ):
            for col in range( self.cols ):
                if(sum(img[row][col]) == self.SUM_RGB_WHITE): continue
                add += self.imgTempCopy[row][col][self.RED_IDX]
                npixels += 1
        avg = add / npixels
        return avg

    def cleanValuesNotInSelectedRegion( self):
        for row in range( self.rows ):
            for col in range( self.cols ):
                if(sum(self.imgTemp[row][col]) == self.SUM_RGB_WHITE): continue
                self.imgReal[row][col] = self.util.WHITE

    def selectValidBodies( self, contours ):
        possible_bodies = []
        for i in range( 0, len(contours)):
            area  = cv2.contourArea( contours[i] )
            if( area > self.MIN_AREA_BODY):
                imgCopy = self.imgTemp.copy()
                self.util.fillContour(imgCopy, contours, i)
                avg = self.getAvgSumRedPixels( self.imgTemp)
                if( avg > self.RED_THRESH ):
                    self.util.fillContour(self.imgTemp, contours, i)
                    possible_bodies.append(i)
        if( len(possible_bodies)):
            self.cleanValuesNotInSelectedRegion()
        return possible_bodies

    def extract( self ):
        self.undistort(self.imgReal)
        self.undistort(self.imgTemp,15, -10)
        th = self.util.applyThresh(self.imgTemp)
        contours = self.util.getContours( th )
        _ = self.selectValidBodies( contours )
        return self.imgReal
