#! /usr/bin/python
'''add some files for ssd
from1:
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
from2:
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
from3:
   prefiles
   --create_data.sh
   --labelmap.prototxt
   --ssd_detect.ipynb
   --ssd_detect.py
   --ssd_pascal.py

add:
   XX_ssd(the train/val/test/trainval.txt are different from the train.txt above)
   --train.txt, val.txt, test.txt(optional), trainval.txt(optional)
   --train_name_size.txt, val_name_size.txt, ...
   --create_data.sh
   --labelmap.prototxt
   --ssd_detect_XX.ipynb
   --ssd_detect_XX.py
   --ssd_pascal_XX.py
'''

import os
import glob
from PIL import Image
from makeNewDir import *


def addToSSD(dataset):

    dirname, basename = os.path.split(dataset[:-1])
    dataset_voc = dirname + '/' + basename + '_VOC/'
    dataset_ssd = dirname + '/' + basename + '_SSD/'

    # make the destdir
    makedirs(dataset_ssd)

    # train.txt, val.txt, test.txt, trainval.txt
    txtlist = glob.glob(dataset_voc + 'ImageSets/Main/*.txt')
    for eachtxt in txtlist:
        with open(eachtxt, 'r') as f:
            imglist = f.readlines()
        dest_txt = dataset_ssd + os.path.basename(eachtxt)
        with open(dest_txt, 'w') as f:
            for eachimg in imglist:
                eachimg = eachimg.strip('\n')
                f.write('%s/JPEGImages/%s.jpg %s/Annotations/%s.xml\n'
                        % (basename, eachimg, basename, eachimg))

    # train_name_size.txt, val_name_size.txt, ...
    txtlist = glob.glob(dataset_voc + 'ImageSets/Main/*.txt')
    img_dir = dataset_voc + 'JPEGImages/'
    for eachtxt in txtlist:
        with open(eachtxt, 'r') as f:
            imglist = f.readlines()
        txtname = os.path.splitext(os.path.basename(eachtxt))[0]
        dest_txt = dataset_ssd + txtname + '_name_size.txt'
        with open(dest_txt, 'w') as f:
            for eachimg in imglist:
                eachimg = eachimg.strip('\n')
                img = Image.open(img_dir + eachimg + '.jpg')
                if len(img.getbands()) < 3:
                    print img_dir + eachimg + '.jpg:' + str(len(img.getbands()))
                width, height = img.size
                f.write('%s %d %d\n' % (eachimg, height, width))

if __name__ == '__main__':
    # paras
    dataset = '/home/lili/codes/makeVocDatasets/datasets/ICDAR2013/'
    addToSSD(dataset)
