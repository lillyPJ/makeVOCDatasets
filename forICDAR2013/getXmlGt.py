#! /usr/bin/python
'''get the xml gt from the txt gt:
from: XXX.txt(one file for each image)
     xmin,ymin,xmax,ymax,label
     xmin,ymin,xmax,ymax,label
to: XXX.xml(one file for each image)
    VOC format
'''
import os
import glob
from PIL import Image
from makeNewDir import *

def getXmlFromTxtGt(src_img_dir, src_txt_dir, tgt_xml_dir):
    # get img_basenames(100.jpg) and img_names (100)
    img_Lists = glob.glob(src_img_dir + '*.jpg')
    img_basenames = []
    for item in img_Lists:
        img_basenames.append(os.path.basename(item))
    img_names = []
    for item in img_basenames:
        temp1, temp2 = os.path.splitext(item)
        img_names.append(temp1)

    # write xml file
    for img in img_names:
        # open image file and the crospronding txt file
        im = Image.open((src_img_dir + img + '.jpg'))
        width, height = im.size
        gt = open(src_txt_dir + 'gt_' + img + '.txt').read().splitlines()  # change the name of gt file

        #write into xml file
        makedirs(tgt_xml_dir)

        xml_file = open((tgt_xml_dir + img + '.xml'), 'w')
        xml_file.write('<annotation>\n')
        xml_file.write('    <folder>text</folder>\n')        # change the dataset name
        xml_file.write('    <filename>' + str(img) + '.jpg' + '</filename>\n')
        xml_file.write('    <size>\n')
        xml_file.write('        <width>' + str(width) + '</width>\n')
        xml_file.write('        <height>' + str(height) + '</height>\n')
        xml_file.write('        <depth>3</depth>\n')
        xml_file.write('    </size>\n')

        # write the region of text on xml file
        for img_each_label in gt:
            spt = img_each_label.split(' ')                    # ICDAR2011-' ', ICDAR2013-' '
            xml_file.write('    <object>\n')
            xml_file.write('        <name>text</name>\n')      # change the label name
            xml_file.write('        <pose>Unspecified</pose>\n')
            xml_file.write('        <truncated>0</truncated>\n')
            xml_file.write('        <difficult>0</difficult>\n')
            xml_file.write('        <bndbox>\n')
            xml_file.write('            <xmin>' + str(spt[0]) + '</xmin>\n')
            xml_file.write('            <ymin>' + str(spt[1]) + '</ymin>\n')
            xml_file.write('            <xmax>' + str(spt[2]) + '</xmax>\n')
            xml_file.write('            <ymax>' + str(spt[3]) + '</ymax>\n')
            xml_file.write('        </bndbox>\n')
            xml_file.write('    </object>\n')
        xml_file.write('</annotation>')

if __name__ == '__main__':
    # paras: image dir and txt dir
    basedir = '/home/lili/codes/makeVocDatasets/datasets/ICDAR2011/'
    # precess all dirs(train, val, test, tranval)
    dirs = glob.glob(basedir + 'img/*')
    for each in dirs:
        eachdir = os.path.basename(each)
        src_img_dir = basedir + 'img/' + eachdir + '/'
        src_txt_dir = basedir + 'gt_txt/' + eachdir + '/'
        tgt_xml_dir = basedir + 'gt_xml/' + eachdir + '/'
        getXmlFromTxtGt(src_img_dir, src_txt_dir, tgt_xml_dir)

