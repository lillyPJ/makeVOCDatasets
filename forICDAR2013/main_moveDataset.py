#! /usr/bin/python
'''move datasets and prepare for ssd training
'''
import os
import shutil
import glob
from makeNewDir import *

# paras
basedir = '/home/lili/codes/makeVocDatasets/datasets/'
dataset = 'ICDAR2013'

# (rename)move ICDAR2011_VOC/* to /home/lili/datasets/VOC/VOCdevkit/
src_dir = basedir + dataset + '_VOC'
dest_dir = '/home/lili/datasets/VOC/VOCdevkit/' + dataset
if not os.path.exists(dest_dir):
    shutil.copytree(src_dir, dest_dir)

# move ICDAR2011_SSD/* to /home/lili/codes/ssd/caffe-ssd/data/ICDAR2011/
src_dir = basedir + dataset + '_SSD'
dest_dir = '/home/lili/codes/ssd/caffe-ssd/data/' + dataset + '/'
makedirs(dest_dir)
filelist = glob.glob(src_dir + '/*')
for each in filelist:
    shutil.copy(each, dest_dir)

# move prefiles/create_data.sh, labelmap.prototxt to /home/lili/codes/ssd/caffe-ssd/data/ICDAR2011/
#dest_dir = '/home/lili/codes/ssd/caffe-ssd/data/' + dataset

shutil.copy('./prefiles/create_data.sh', dest_dir)
shutil.copy('./prefiles/labelmap.prototxt', dest_dir)

# (rename)move prefiles/ssd_pascal.py to /home/lili/codes/ssd/caffe-ssd/examples/ssd/
dest_file = '/home/lili/codes/ssd/caffe-ssd/examples/ssd/ssd_pascal_' + dataset + '.py'
shutil.copy('./prefiles/ssd_pascal.py', dest_file)

# (rename)move prefiles/ssd_detect.py, ssd_detect.ipynb to /home/lili/codes/ssd/caffe-ssd/examples
dest_file1 = '/home/lili/codes/ssd/caffe-ssd/examples/ssd_detect_' + dataset + '.py'
dest_file2 = '/home/lili/codes/ssd/caffe-ssd/examples/ssd_detect_' + dataset + '.ipynb'
shutil.copy('./prefiles/ssd_detect.py', dest_file1)
shutil.copy('./prefiles/ssd_detect.ipynb', dest_file2)