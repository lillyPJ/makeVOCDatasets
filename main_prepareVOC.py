#! /usr/bin/python
'''change the dataset to VOC format
'''

from getXmlGt import *
from getImgNameList import *
from changeToVOC import *

basedir = '/home/lili/codes/makeVocDatasets/datasets/coco/'
# 1. get xml_gt
dirs = glob.glob(basedir + 'img/*')
for each in dirs:
    eachdir = os.path.basename(each)
    src_img_dir = basedir + 'img/' + eachdir + '/'
    src_txt_dir = basedir + 'gt_txt/' + eachdir + '/'
    tgt_xml_dir = basedir + 'gt_xml/' + eachdir + '/'
    getXmlFromTxtGt(src_img_dir, src_txt_dir, tgt_xml_dir)

# 2. get imgnames
tgt_imgname_dir = basedir + 'gt_total_imgname_txt' + '/'
getImgNameList(basedir, tgt_imgname_dir)

# 3. change to VOC format
changeToVOC(basedir)