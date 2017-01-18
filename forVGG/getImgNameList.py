#! /usr/bin/python
'''get the image name list for each folder(train, val, test, trainval)
   save as txt file.
'''

import os
import glob
from makeNewDir import *

def getImgNameList(basedir, tgt_imgname_dir):
    # make new dirs
    makedirs(tgt_imgname_dir)

    # precess all dirs(train, val, test, tranval)
    dirs = glob.glob(basedir + 'img/*')
    tgt_imgname_txt = tgt_imgname_dir + 'train.txt'
    f = open(tgt_imgname_txt, 'w')
    for each in dirs:
        eachdir = os.path.basename(each)
        src_img_dir = basedir + 'img/' + eachdir + '/'
        # tgt_imgname_txt = tgt_imgname_dir + eachdir + '.txt'
        imglist = glob.glob(src_img_dir + '*.jpg')
        imgnames = []
        for img in imglist:
            imgname = eachdir + '/' + os.path.splitext(os.path.basename(img))[0]
            imgnames.append(imgname)
        f.writelines(["%s\n" % item for item in imgnames])
    f.close()

if __name__ == '__main__':
    basedir = '/home/lili/datasets/VGG/'
    tgt_imgname_dir = basedir + 'gt_total_imgname_txt' + '/'
    getImgNameList(basedir, tgt_imgname_dir)

