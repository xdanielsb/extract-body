""" This is the launcher of the application."""
from  logic.extract import *
from  logic.util import *
import numpy as np
if __name__ == "__main__":
    print("The application has started.")
    kwargs = {}
    kwargs["pathReal"] = "assets/images/color_image.jpg"
    kwargs["pathTemp"] = "assets/images/depth_image_colored.jpg"
    kwargs["mCamera"]  = "assets/calibration/K_depth_intrinsic.npy"
    kwargs["mTrans"]   = "assets/calibration/T_color_to_depth_extrinsic.npy"

    #Create instance  in charge to extract body
    ext = ExtractorBody(**kwargs)
    bodies = ext.extract( )

    #Create instance in charge to display visualization
    util = Util()
    util.showImage( bodies )
