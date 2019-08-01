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

data = []

# Worked on:
'''
python3.5 ./segmentation_2.py --input ./dataset/2019-05-04-115147.png
python3.5 ./segmentation_2.py --input ./dataset/2019-05-04-114702.png
python3.5 ./segmentation_2.py --input ./dataset/2019-05-04-113838.png
'''

parser = argparse.ArgumentParser(description='Extract roses')
parser.add_argument('--input', help="The input file for processing")
args = parser.parse_args()

print("Reading file:", args.input)
frame = cv2.imread(args.input)
img = frame.copy()

blurred_frame = cv2.GaussianBlur(frame, (25, 25), .5)
hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

#-- Working HSV ----------------------
lower_green = np.array([10,125,20])
upper_green = np.array([30,255,100])

print("Lower green:", lower_green)
print("Lower green:", upper_green)

mask = cv2.inRange(hsv, lower_green, upper_green)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    area = cv2.contourArea(contour)
    x,y,w,h = cv2.boundingRect(contour)

    # draw a red 'nghien' rectangle
    if (30000.0 > area > 300.0):
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)
        print("Area:", area)

        roi = img[y:y+h, x:x+w]
        roi = cv2.resize(roi, (256, 256))
        data.append(roi)
    else:
        print("Skipping contour",(x,y,w,h),"with area", area)

data = np.asarray(data)
np.savez("test_data", data)

cv2.imshow("Frame", frame)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
