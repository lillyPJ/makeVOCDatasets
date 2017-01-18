#! /usr/bin/python
'''change to VOC format directory
from:
   XX
   --img
     --train/val/test/trainval
       --XXX.jpg
   --gt_xml
     --train/val/test/trainval
       --XXX.xml
   --gt_total_imgname_txt
     --train.txt
     --val.txt
     --test.txt(optional)
     --trainval.txt(optional)
to:
   XX_VOC
   --Annotations
     --XXX.xml
   --ImageSets
     --Main
       --train.txt
       --val.txt
       --test.txt(optional)
       --trainval.txt(optional)
   --JPEGImages
     --XXX.jpg
'''
import glob
import shutil
from makeNewDir import *


def changeToVOC(dataset):

    dirname, basename = os.path.split(dataset[:-1])
    dataset_voc = dirname + '/' + basename + '_VOC/'


    #Annotations
    destdir = dataset_voc + 'Annotations/'
    makedirs(destdir)
    srcdirs = glob.glob(dataset + 'gt_xml/*')
    for eachdir in srcdirs:
        for filename in glob.glob(os.path.join(eachdir, '*.*')):
            shutil.copy(filename, destdir)

    #ImageSets
    destdir = dataset_voc + 'ImageSets/Main/'
    makedirs(destdir)
    srcdirs = glob.glob(dataset + 'gt_total_imgname_txt/*')
    for filename in srcdirs:
        shutil.copy(filename, destdir)

    #JPEGImages
    destdir = dataset_voc + 'JPEGImages/'
    makedirs(destdir)
    srcdirs = glob.glob(dataset + 'img/*')
    for eachdir in srcdirs:
        for filename in glob.glob(os.path.join(eachdir, '*.*')):
            shutil.copy(filename, destdir)

if __name__ == '__main__':
    # paras
    dataset = '/home/lili/codes/makeVocDatasets/datasets/ICDAR2011/'
    changeToVOC(dataset)
