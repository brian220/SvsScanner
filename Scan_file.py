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
There are 5 functions can use (detailed of them is in Scan_svs.py):
1. scan_detail
2. show_region
3. scan_rectangle
4. scan_whole
5. scan_annocation
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
     #Scan_svs.scan_whole(scan, orig_w, orig_h, d_factor, current_level)
     scan.close

scan_file()
