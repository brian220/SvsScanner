"""
This program is used to find out if a point is in the irregular polygon or not
and then we can find out if a patch is in the annotation part
method:
Point-In-Polygon Algorithm — Determining Whether A Point Is Inside A Complex Polygon
source: http://alienryderflex.com/polygon/
"""

import sys
#sys.path.append("../Read_xml.py")
#import Read_xml
import openslide
from openslide import open_slide # http://openslide.org/api/python/
import numpy as np
from PIL import Image
import math
import os

dir_folder = r'C:\Users\nctu\Desktop\svs_scanner\inpoly'
patch_size = 50
polyXGroup = [2, 2, 8, 8, 5]
polyYGroup = [12, 2, 9, 10, 10]

def inpoly(x, y, polyXGroup, polyYGroup):
  pointInPoly = False
  polyXGroup = [float(xInPoly) for xInPoly in polyXGroup]
  polyYGroup = [float(yInPoly) for yInPoly in polyYGroup]
  polyXGroup.append(polyXGroup[0])
  polyYGroup.append(polyYGroup[0])
  for i in range(0, len(polyXGroup) - 1):
      # point will cross the line y = a * x + b, a is slope, b is y - a * x
      if y > min(polyYGroup[i], polyYGroup[i + 1]) and y <= max(polyYGroup[i], polyYGroup[i + 1]) and (x >= polyXGroup[i] or x >= polyXGroup[i + 1]):
        if (polyXGroup[i + 1] - polyXGroup[i]) == 0:
            pointInPoly = not pointInPoly
        else:
          a = (polyYGroup[i + 1] - polyYGroup[i]) / (polyXGroup[i + 1] - polyXGroup[i])
          b = polyYGroup[i] - a * polyXGroup[i]
          if x > (y - b) / a:
            pointInPoly = not pointInPoly

  return pointInPoly

"""
def ann_detect():
  annlist = Read_xml.read_xml("patient_004_node_4.xml")
  polyXGroup = annlist[0].coordinateX
  polyYGroup = annlist[0].coordinateY
  # find out if each point is in the polygon, and use a tag to record in the dictionary
  patch_dict = {}
  for  ann in annlist:
    for i in range(ann.border[0], ann.border[1], patch_size):
      for j in range(ann.border[2], ann.border[3], patch_size):
        if inpoly(i, j, polyXGroup, polyYGroup):
          patch_dict.update({(i, j) : True})
        else:
          patch_dict.update({(i, j) : False})

 # save the region that is all in the polygon
   index = 0
   for ann in annlist:
     for i in range(ann.border[0], ann.border[1], patch_size):
       for j in range(ann.border[2], ann.border[3], patch_size):
         if patch_dict.get((i, j)) && patch_dict.get((i + patch_size, j)) &&
            patch_dict.get((i , j + patch_size)) && patch_dict.get((i + patch_size, j + patch_size)):
            img  = open.read_region((i,j), 0 , (patch_size, patch_size))
            img.save(dir_folder + str(index) + ".png")
            index += 1
"""
