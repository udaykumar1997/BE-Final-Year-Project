import cv2
import numpy as np
import argparse

from skimage.filters import threshold_otsu
from skimage import measure
from skimage.measure import regionprops
from skimage.transform import resize

import pdb

import matplotlib.pyplot as plt

def get_rectangles(contours):
  rectangles = []
  for contour in contours:
    epsilon = 0.04*cv2.arcLength(contour,True)
    hull = cv2.convexHull(contour)
    approx = cv2.approxPolyDP(hull,epsilon ,True)
    if (len(approx) == 4 and cv2.isContourConvex(approx)):
        rectangles.append(approx)

  return rectangles


parser = argparse.ArgumentParser(description='Extract roses')
parser.add_argument('--input', help="The input file for processing")
args = parser.parse_args()

print("Reading file:", args.input)
frame = cv2.imread(args.input)

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
lower_red = np.array([100,100,100]) 
upper_red = np.array([179,255,255]) 

# Here we are defining range of red color in HSV 
# This creates a mask of red coloured  
# objects found in the frame 
mask = cv2.inRange(hsv, lower_red, upper_red) 

# The bitwise and of the frame and mask is done so  
# that only the red coloured objects are highlighted  
# and stored in res 

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

res = cv2.bitwise_and(gray,gray, mask=mask) 

res = cv2.GaussianBlur(res, (11,11), 0)

kernel = np.ones((11,11),np.uint8)
res = cv2.morphologyEx(res, cv2.MORPH_CLOSE, kernel)

# This displays the frame, mask  
# and res which we created in 3 separate windows. 
cv2.imshow('frame',frame) 
cv2.imshow('mask',mask) 
cv2.imshow('res',res) 

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows() 

#-------------------- Thresholding -------------------#
thresh = threshold_otsu(res)
thresh_res = res > thresh

flow = thresh_res
labs_flow = measure.label(flow)

# Roses should be between 3% and 20% of the width of image
# Height should be between 2% and 20%

object_dimensions = (0.02*flow.shape[0], 0.20*flow.shape[0], 0.03*flow.shape[1], 0.2*flow.shape[1])
min_height, max_height, min_width, max_width = object_dimensions

objs = []

mask = np.ones((frame.shape[0], frame.shape[1], 1), dtype=np.uint8)
hulls,hierarchy = cv2.findContours(res,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
for index, contour in zip(range(len(hulls)), hulls):
	cv2.drawContours(mask, contour, -1, (0, 0, 128), 5 )

for regs in regionprops(labs_flow):
	y0, x0, y1, x1 = regs.bbox
	reg_height = y1 - y0
	reg_width = x1 - x0

	if reg_height > min_height and reg_height < max_height and reg_width > min_width and reg_width < max_width:

			roi = frame[y0:y1, x0:x1]

			# Resize the selected objects to 28X28
			res_obj = resize(roi, (28, 28))

			cv2.imshow('Object',res_obj) 
			cv2.waitKey(0) & 0xFF
			cv2.destroyAllWindows() 

			res_flat = res_obj.flatten()

			# Add to list of objects
			objs.append(res_flat)

rose_only = cv2.bitwise_and(frame, frame, mask=mask)

# present the image to screen
cv2.imshow('Processed image', rose_only)
if cv2.waitKey(0) == 9:
	cv2.destroyAllWindows()

