#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ICIAR2018 - Grand Challenge on Breast Cancer Histology Images
https://iciar2018-challenge.grand-challenge.org/home/
"""
import sys
sys.path.append("../Scan_svs.py")
import Scan_svs
import openslide
from openslide import open_slide # http://openslide.org/api/python/
import os

dir_img = r'C:\Users\nctu\Desktop\svs_scanner\svs_image'
cut_folder = r'C:\Users\nctu\Desktop\svs_scanner\cut_image'

valid_images = ['.svs']
"""
Use Openslide to scan a svs file in a folder
There are three functions can use
"""
def scan_file():
  scriptpath = os.path.dirname(__file__)
  xml_filename = os.path.join(scriptpath, "patient_004_node_4.xml")
  for f in os.listdir(dir_img):
     ext = os.path.splitext(f)[1]
     if ext.lower() not in valid_images:
         continue
     curr_path = os.path.join(dir_img,f)
     print(curr_path)

     # open scan
     scan = openslide.OpenSlide(curr_path)
     current_level = 0
     (orig_w, orig_h) = scan.level_dimensions[current_level]
     d_factor = scan.level_downsamples[current_level]
     Scan_svs.scan_detail(scan, orig_w, orig_h, d_factor)
     Scan_svs.show_region(scan,  65865, 23331, 1728, 1632, d_factor, current_level)
     Scan_svs.scan_rectangle(scan, 65865, 23331, 1728, 1632, 0)
     #Scan_svs.scan_whole(scan, orig_w, orig_h, d_factor, current_level)
     scan.close

scan_file()

 #ann 0
 #Scan_svs.show_region(scan,  53672, 26724, 1824, 1856, d_factor, current_level)
 #Scan_svs.scan_rectangle(scan, 53672, 26724, 1824, 1856, 0)
 #ann 1
 #Scan_svs.show_region(scan,  54055, 34853, 2304, 2784, d_factor, current_level)
 #Scan_svs.scan_rectangle(scan, 54055, 34853, 2304, 2784, 0)
 #ann 2
 #Scan_svs.show_region(scan,  59336, 41669, 1824, 2208, d_factor, current_level)
 #Scan_svs.scan_rectangle(scan, 59336, 41669, 1824, 2208, 0)
