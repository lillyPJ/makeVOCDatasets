#! /usr/bin/python
'''get the image name list for each folder(train, val, test, trainval)
   save as txt file.
'''

import os
import glob

# paras
basedir = '/home/lili/codes/makeVocDatasets/datasets/boat5/'
tgt_imgname_dir = basedir + 'gt_total_imgname_txt' + '/'

# make new dirs
try:
    os.makedirs(tgt_imgname_dir)
except OSError:
    if not os.path.isdir(tgt_imgname_dir):
        raise

# precess all dirs(train, val, test, tranval)
dirs = glob.glob(basedir + 'img/*')
for each in dirs:
    eachdir = os.path.basename(each)
    src_img_dir = basedir + 'img/' + eachdir + '/'
    tgt_imgname_txt = tgt_imgname_dir + eachdir + '.txt'
    imglist = glob.glob(src_img_dir + '*.jpg')
    imgnames = []
    for img in imglist:
        imgname = os.path.splitext(os.path.basename(img))[0]
        imgnames.append(imgname)
    with open(tgt_imgname_txt, 'w') as f:
        f.writelines(["%s\n" % item for item in imgnames])

