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

class point (object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

def pointLieRight(testPoint, polyPoint1, polyPoint2):
  lieRight = False
  if testPoint.y > min(polyPoint1.y, polyPoint2.y) and  testPoint.y <= max(polyPoint1.y, polyPoint2.y) and ( testPoint.x >= polyPoint1.x or testPoint.x >= polyPoint2.x):
    if (polyPoint2.x - polyPoint1.x) == 0:
        lieRight = True
    else:
      a = (polyPoint2.y - polyPoint1.y) / (polyPoint2.x - polyPoint1.x)
      b = polyPoint1.y - a * polyPoint1.x
      if  testPoint.x > ( testPoint.y - b) / a:
        lieRight = True
  return lieRight

def dealWithPolyGroup(polyGroup):
  polyGroup = [float(number) for number in polyGroup]
  polyGroup.append(polyGroup[0])
  return polyGroup

def pointInPoly(testPoint, polyXGroup, polyYGroup):
  inPoly = False
  polyXGroup = dealWithPolyGroup(polyXGroup)
  polyYGroup = dealWithPolyGroup(polyYGroup)
  for i in range(0, len(polyXGroup) - 1):
      polyPoint1 = point(polyXGroup[i], polyYGroup[i])
      polyPoint2 = point(polyXGroup[i + 1], polyYGroup[i + 1])
      if (pointLieRight(testPoint, polyPoint1, polyPoint2)):
        inPoly = not inPoly
  return inPoly

print (pointInPoly(point(3,3), polyXGroup, polyYGroup))
print (pointInPoly(point(3,10), polyXGroup, polyYGroup))
print (pointInPoly(point(10,10), polyXGroup, polyYGroup))
print (pointInPoly(point(4,8), polyXGroup, polyYGroup))
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
