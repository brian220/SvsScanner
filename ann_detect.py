"""
This program is used to find out if a point is in the irregular polygon or not
and then we can find out if a patch is in the annotation part
method:
Point-In-Polygon Algorithm — Determining Whether A Point Is Inside A Complex Polygon
source: http://alienryderflex.com/polygon/
"""

import sys
sys.path.append("../Read_xml.py")
import Read_xml
import openslide
from openslide import open_slide # http://openslide.org/api/python/
import numpy as np
from PIL import Image
import math
import os

dir_folder = r'C:\Users\nctu\Desktop\svs_scanner\inpoly'
patch_size = 50
polyX = [2, 2, 8, 8, 5]
polyY = [12, 2, 9, 10, 10]

def inpoly(x, y, polyX, polyY):
  pass_node = False
  polyX = [float(x) for x in polyX]
  polyY = [float(y) for y in polyY]
  polyX.append(polyX[0])
  polyY.append(polyY[0])
  for i in range(0, len(polyX) - 1):
      # point will cross the line y = a * x + b, a is slope, b is y - a * x
      if y > min(polyY[i], polyY[i + 1]) and y <= max(polyY[i], polyY[i + 1]) and (x >= polyX[i] or x >= polyX[i + 1]):
        a = (polyY[i + 1] - polyY[i]) / (polyX[i + 1] - polyX[i])
        b = polyY[i] - a * polyX[i]
        if x > (y - b) / a:
            pass_node = not pass_node

  return pass_node


#print (inpoly(1, 1, polyX, polyY))
#print (inpoly(2, 10, polyX, polyY))
#print (inpoly(3, 7, polyX, polyY))
#print (inpoly(3, 9, polyX, polyY))
print (inpoly(3, 10, polyX, polyY))
#print (inpoly(3, 10, polyX, polyY))
"""
def ann_detect():
  annlist = Read_xml.read_xml("patient_004_node_4.xml")
  polyX = annlist[0].coordinateX
  polyY = annlist[0].coordinateY
  # find out if each point is in the polygon, and use a tag to record in the dictionary
  patch_dict = {}
  for  ann in annlist:
    for i in range(ann.border[0], ann.border[1], patch_size):
      for j in range(ann.border[2], ann.border[3], patch_size):
        if inpoly(i, j, polyX, polyY):
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
