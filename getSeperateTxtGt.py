#! /usr/bin/env python
'''change the gt file format:
from: train.txt(one file for all images)
     XXX.jpg x1 y1 x2 y2 x3 y3 x4 y4
     XXX.jpg x1 y1 x2 y2 x3 y3 x4 y4
to: XXX.txt(one file for each image)
    xmin,ymin,xmax,ymax,label
'''

# load libs
import os
import cv2
import glob
import numpy as np
from makeNewDir import *

# papras
srcdir = '/home/lili/codes/makeVocDatasets/datasets/boat5/gt_total_txt/'
destdir = os.path.split(srcdir[:-1])[0] + '/gt_txt/'

# read input gtdirname, make output gtdir
in_gtdirnames = glob.glob(srcdir + '*.txt')
for gtdir in in_gtdirnames:
    dirname = os.path.splitext(os.path.basename(gtdir))[0]

    makedirs(destdir + dirname)

# read input gtfiles, make output seperate gtfiles
for gtname in in_gtdirnames:
    outdir = destdir + os.path.splitext(os.path.basename(gtname))[0] + '/'
    # read input
    with open(gtname, 'r') as f:
        lines = f.readlines()
    imgnames = []
    points = []
    for line in lines:
        templist = line.split(' ')
        imgnames.append(templist[0])
        point = np.array([int(x) for x in templist[1:9]])
        point = point.reshape([4, 1, 2])
        box = cv2.boundingRect(point)
        pt = [box[0], box[1], box[0] + box[2], box[1] + box[3]]
        ptstr = ','.join(str(x) for x in pt) + ',boat5'
        points.append(ptstr)
    # write output
    for img,xy in zip(imgnames, points):
        txtname = outdir + os.path.splitext(img)[0] + '.txt'
        with open(txtname, 'w') as f:
            f.write(xy)





