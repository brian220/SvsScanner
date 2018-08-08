#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ICIAR2018 - Grand Challenge on Breast Cancer Histology Images
"""
import sys
sys.path.append("../Read_xml.py")
import Read_xml
import openslide
from matplotlib import pyplot as plt
from scipy.misc import imsave, imresize
from openslide import open_slide # http://openslide.org/api/python/
import numpy as np
from PIL import Image
import math
import os

dir_img = r'C:\Users\nctu\Desktop\svs_scanner\svs_image'
cut_folder = r'C:\Users\nctu\Desktop\svs_scanner\cut_image'
ann_folder = r'C:\Users\nctu\Desktop\svs_scanner\ann_image'

valid_images = ['.tif']

"""
Show the detail information of the scan
"""
def scan_detail(scan, orig_w, orig_h, d_factor):
    print ("Level count:" + str(scan.level_count))
    print ("dimensions:" + str(scan.level_dimensions))
    print ("Current dimension:(%d, %d)" % (orig_w, orig_h))
    print ("Down sample factor:%f" % (d_factor))

"""
Store a particular part of slide into show_region.png (without cut in to block)
"""
def show_region(scan, x, y, width, height, d_factor, cur_level):
   img = scan.read_region((int(x * d_factor), int(y * d_factor)), cur_level, (width, height))
   img.save("region_slide.png")

"""
Use Openslide to read the annotation part and cut the part
into the little blocks (size: 200 * 200)
The scan is under level 0
"""
def scan_rectangle(scan, x, y, width, height, ann_index):
    patch_size = 200
    print ("Patch size:" + str(patch_size))
    filename = 0
    whole_img =  Image.new('RGBA',(width, height))
    for w in range(x, x + width, patch_size):
      for h in range(y, y + height, patch_size):
        img = scan.read_region((w , h), 0, ( patch_size ,  patch_size))
        img.save(str(ann_folder)+ '\\' + str(filename) + ".png")
        whole_img.paste(img, (w, h))
        filename += 1

    whole_img.save("ann" + str(ann_index) + ".png")

"""
Use Openslide read_region to read the scan in the little block
Show the scan image in the folder \cut_image
Combine the images together and store in myimg.png
"""
def scan_whole(scan, orig_w, orig_h, d_factor, current_level):
    patch_size = 1000
    print ("Patch size:" + str(patch_size))
    whole_img =  Image.new('RGBA',(orig_w, orig_h))
    filename = 0
    for w in range(0, orig_w, patch_size):
      for h in range(0, orig_h, patch_size):

        patch_width = patch_size
        patch_height = patch_size

        if w + patch_size > orig_w:
          patch_width = orig_w - w
        if h + patch_size > orig_h:
          patch_height = orig_h - h

        img = scan.read_region((int(w * d_factor), int(h * d_factor)), current_level, (patch_width , patch_height))
        whole_img.paste(img, (w, h))
        #img.save(str(cut_folder)+ '\\' + str(filename) + ".png")
        filename += 1

      whole_img.save("whole_slide.png")

"""
(Not used recently)
Cut the xml's annotation parts in the svs file and store in the folder /ann_image
at level 0
"""
def scan_annocation(scan, xml_filename):
  annlist = Read_xml.read_xml(xml_filename)
  for index, ann in enumerate(annlist):
    #print (ann.border[0], ann.border[2], ann.box[0] , ann.box[1])
    img = scan.read_region((ann.border[0], ann.border[2]), 0, (ann.border[1] - ann.border[0], ann.border[3] - ann.border[2]))
    img.save(str(ann_folder)+ '\\' + str(index) + ".png")
