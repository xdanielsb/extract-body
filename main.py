""" This is the launcher of the application."""
from  logic.extract import *
if __name__ == "__main__":
    print("The application has started.")
    pathReal = "assets/images/color_image.jpg"
    pathTemp = "assets/images/depth_image_colored.jpg"
    e = Extract( pathReal, pathTemp)
    # e.showImage(e.imgReal)
    # e.histogram(e.imgReal)
    res = e.removeBlue( e.imgTemp)
    e.showImage( res )
    
