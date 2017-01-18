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
import os
from makeNewDir import *

def changeToVOC(dataset):

    dirname, basename = os.path.split(dataset[:-1])
    dataset_voc = dirname + '/' + basename + '_VOC/'


    #Annotations
    destdir = dataset_voc + 'Annotations'
    srcdir = dataset + 'gt_xml/word'
    makedirs(os.path.dirname(destdir))
    os.symlink(srcdir, destdir)

    #ImageSets
    destdir = dataset_voc + 'ImageSets/Main'
    srcdir = dataset + 'gt_total_imgname_txt'
    makedirs(os.path.dirname(destdir))
    os.symlink(srcdir, destdir)

    #JPEGImages
    destdir = dataset_voc + 'JPEGImages'
    srcdir = dataset + 'img'
    makedirs(os.path.dirname(destdir))
    os.symlink(srcdir, destdir)


if __name__ == '__main__':
    # paras
    basedir = '/home/lili/datasets/VGG/'
    changeToVOC(basedir)
