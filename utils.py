import numpy as np
import argparse

def rotate(image, times):
    return np.rot90(image, times)

def get_inputs():
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--input_video", type=str, required=False,
		help="path to input video")
	ap.add_argument("-f", "--input_folder", type=str, required=False,
		help="path to folder images")
	ap.add_argument("-o", "--output", type=str, required=True,
		help="path to output directory of cropped faces")
	ap.add_argument("-s", "--skip", type=int, default=5,
		help="# of frames to skip before applying face detection")
	ap.add_argument("-v", "--verbose", type=int, default=0,
		help="set True to print the saved images in console")
	return vars(ap.parse_args())
