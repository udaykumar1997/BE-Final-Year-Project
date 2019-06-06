import cv2
import io
import random
import sys
from io import StringIO
import glob
import numpy as np

#old_stdout= sys.stdout
#sys.stdout = buf = StringIO()

# Returns true if two rectangles overlap 
def doOverlap(t1, t2):
    rect1_x1 = t1[0] 
    rect1_x2 = t1[2]
    rect1_y1 = t1[1]
    rect1_y2 = t1[3]

    rect2_x1 = t2[0] 
    rect2_x2 = t2[2]
    rect2_y1 = t2[1]
    rect2_y2 = t2[3]

    if (rect1_x1 <= rect2_x1 <= rect1_x2 or rect1_x1 <= rect2_x2 <= rect1_x2):
        if (rect1_y1 <= rect2_y1 <= rect1_y2 or rect1_y1 <= rect2_y2 <= rect1_y2):
            return True

    if (rect2_x1 <= rect1_x1 <= rect2_x2 or rect2_x1 <= rect1_x2 <= rect2_x2):
        if (rect2_y1 <= rect1_y1 <= rect2_y2 or rect2_y1 <= rect1_y2 <= rect2_y2):
            return True

    return False; 

def checkAllOverlap(l_bbs, rect):
    for bb in l_bbs:
        print("Checked BB", bb)
        print("Return overlap check:", doOverlap(bb, rect))
        if doOverlap(bb, rect):
            break
    else:
        print("No overlap rect", rect)
        return True

    return False

def genRandRect(l_bbs, inp_rect):

    max_h = 480
    max_w = 720

    res = False

    while( not res ):
        x1, y1, x2, y2 = inp_rect 
        h = y2 - y1 
        w = x2 - x1 

        y3 = random.randint(0, max_h-h)
        x3 = random.randint(0, max_w-w)
        y4 = y3 + h
        x4 = x3 + w

        rect = (x3, y3, x4, y4)
        print("Random rect:", rect)

        res = checkAllOverlap(l_bbs, rect)

    return rect

debug = False
size = 256

data = []
labs = []

for imname in glob.glob("dataset/*.png"):

    print("Processing image:", imname)
    img = cv2.imread(imname)

    with io.open(imname.replace(".png", ".txt")) as fd:
        annot = fd.read()
    annot = annot.split('\n')
    len_annot = int(annot[0])

    bb_list = []
    for ind in range(len_annot):
        x1, y1, x2, y2 = [int(cord) for cord in annot[ind + 1].split()]
        bb_list.append([x1, y1, x2, y2])
        cv2.rectangle(img, (x1,y1), (x2, y2), (0,255,0),2)

        roi = img[y1:y2, x1:x2]
        roi = cv2.resize(roi, (size, size))

        data.append(roi)
        labs.append(1)

    if debug:
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    neg_bb_list = []
    for bbs in bb_list:
        print("\n\n\n")

        x3, y3, x4, y4 = genRandRect(bb_list, bbs)
        neg_rect = [str(val) for val in (x3, y3, x4, y4)]
        neg_bb_list.append(neg_rect)
        cv2.rectangle(img, (x3, y3), (x4, y4), (0, 0 ,255),2)

        roi = img[y3:y4, x3:x4]
        roi = cv2.resize(roi, (size, size))

        data.append(roi)
        labs.append(0)


    if debug:
        cv2.imshow("Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    with io.open(imname.replace(".png", "_neg.txt"), "w") as fd:
        fd.write(str(len_annot) + '\n')
        for ind in range(len_annot):
            fd.write(" ".join(neg_bb_list[ind]))
        fd.write('\n')

data =np.asarray(data)
labs =np.asarray(labs)

np.savez("proc_data", data=data, labels=labs)

#sys.stdout = old_stdout
#print("Content of buffer:\n", buf.getvalue())
