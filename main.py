#!/usr/bin/env python3
""" This is the launcher of the application."""
from  logic.extract import *
from  logic.util import *
import numpy as np
if __name__ == "__main__":
    print("The application has started. (Ctrl+z to finish)")
    kwargs = {}
    kwargs["pathReal"] = "assets/images/color_image_bonus.jpg"
    kwargs["pathTemp"] = "assets/images/depth_image_colored.jpg"
    kwargs["pathDepthI"] = "assets/images/depth_image.png"
    kwargs["mCamera"]  = "assets/calibration/K_depth_intrinsic.npy"
    kwargs["mTrans"]   = "assets/calibration/T_color_to_depth_extrinsic.npy"

    #Create instance  in charge to extract body
    try:
        ext = ExtractorBody(**kwargs)
        bodies = ext.extract( )
    except Exception as inst:
        print(type(inst))
        print(inst)

    #Create instance  util in charge to help to sdisplay visualization
    util = Util()
    util.showImage( bodies )
