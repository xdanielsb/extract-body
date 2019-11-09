import cv2

class Util:
    WHITE = (255,255,255)
    NAME_WINDOW = 'IMG_SHOW'
    def __init__(self):
        pass

    def readImage(self, path, tt=1):
        return cv2.imread( path, tt)

    def showImage(self, img):
        cv2.namedWindow(self.NAME_WINDOW,cv2.WINDOW_NORMAL)
        cv2.resizeWindow(self.NAME_WINDOW, 300, 700)
        cv2.imshow(self.NAME_WINDOW , img)
        cv2.waitKey(0)

    def togray( self, img ):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray

    def getHistogram( self, img):
        bins = 256
        range_scale = [0,254]
        nivel_transparencia = 0.5
        plt.hist(img.ravel(),bins,range_scale, label="histogram", alpha=nivel_transparencia);
        plt.legend(loc='upper right')
        plt.show()

    def applyCanny( self, img):
        img = togray( img )
        res = cv2.Canny( img ,480,500)
        return res

    def fillContour( self, img, contours, i):
        cv2.drawContours(img, contours, i , self.WHITE, -1)

    def removeBlue(self, img):
        lower = np.array([0,30,255])
        upper = np.array([255,255,255])
        mask = cv2.inRange(img, lower, upper)
        res = cv2.bitwise_and(img, img, mask= mask)
        return res

    def applyThresh(self, im, mi=100, ma=255):
        if( len(im.shape) == 3):
            _, thr= cv2.threshold(self.togray( im ) ,mi,ma,cv2.THRESH_BINARY)
        else:
            _, thr= cv2.threshold(im  ,mi,ma,cv2.THRESH_BINARY)
        return thr

    def getContours( self,img ):
        if( len(img.shape) == 3):
            (_, contours, _) = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        else:
            (contours,_) = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours
