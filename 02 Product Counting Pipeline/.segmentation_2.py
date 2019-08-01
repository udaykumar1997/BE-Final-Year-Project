# @Author: uday
# @Date:   2019
# @Email:  udaykumar.1997@gmail.com
# @Last modified by:   uday
# @Last modified time: 2019
# @License: apache-2.0
# @Copyright: #
#  Copyright 2019 Uday Kumar Adusumilli
#
#  Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at
#
#	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.



import cv2
import numpy as np
import argparse

from skimage.filters import threshold_otsu
from skimage import measure
from skimage.measure import regionprops
from skimage.transform import resize

import pdb

def get_rectangles(contours):
  rectangles = []
  for contour in contours:
    epsilon = 0.01*cv2.arcLength(contour,True)
    hull = cv2.convexHull(contour)
    approx = cv2.approxPolyDP(hull,epsilon ,True)
    rectangles.append(approx)

  return rectangles


parser = argparse.ArgumentParser(description='Extract roses')
parser.add_argument('--input', help="The input file for processing")
args = parser.parse_args()

print("Reading file:", args.input)
frame = cv2.imread(args.input)

blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

lower_red = np.array([100,40,100])
upper_red = np.array([179,255,255])

mask = cv2.inRange(hsv, lower_red, upper_red)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

vc=0
oc=0

for contour in contours:
    area = cv2.contourArea(contour)
    rectContour = get_rectangles([contour])
#    print (" -area: ",area, " -contour: ", contour," -rectContour: ", get_rectangles([contour]))
    if (area > 0.5):
        cv2.drawContours(frame, rectContour, -1, (0, 255, 0), 3)
        print("Processing contour",rectContour,"with area", area)
        vc=vc+1
    else:
        print("Skipping contour",rectContour,"with area", area)
        oc=oc+1
print("vc ",vc," oc ", oc)
cv2.imshow("Frame", frame)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
