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

def pointInPoly(testPoint, polyPointGroup):
  inPoly = False
  for i in range(0, len(polyPointGroup) - 1):
      if (pointLieRight(testPoint, polyPointGroup[i], polyPointGroup[i+1])):
        inPoly = not inPoly
  return inPoly

def groupXY(polyXGroup, polyYGroup):
  polyPointGroup = []
  for i in range(0, len(polyXGroup)):
      polyPointGroup.append(point(polyXGroup[i], polyYGroup[i]))
  return polyPointGroup

def dealWithPolyGroup(polyGroup):
  polyGroup = [float(number) for number in polyGroup]
  polyGroup.append(polyGroup[0])
  return polyGroup

def getPolyPoints(ann):
   polyXGroup = dealWithPolyGroup(ann.coordinateX)
   polyYGroup = dealWithPolyGroup(ann.coordinateY)
   polyPointGroup = groupXY(polyXGroup, polyYGroup)

# find out if each point is in the polygon, and use a tag to record in the dictionary
def tagInPoly(ann, polyPointGroup):
    pointInPolytag = {}
    for i in range(ann.border[0], ann.border[1], patch_size):
      for j in range(ann.border[2], ann.border[3], patch_size):
        if inpoly(point(i, j), polyPointGroup):
          pointInPolytag.update({(i, j) : True})
        else:
          pointInPolytag.update({(i, j) : False})
    return pointInPolytag

def fourPointsInPoly(i, j, pointInPolytag):
  inPoly = False
  if patch_dict.get((i, j)) and patch_dict.get((i + patch_size, j)) and
     patch_dict.get((i , j + patch_size)) and patch_dict.get((i + patch_size, j + patch_size)):
     inpoly = True
  return inPoly

# save the region that is all in the polygon
def saveInsideRegions():
  imgIndex = 0
    for i in range(ann.border[0], ann.border[1], patch_size):
      for j in range(ann.border[2], ann.border[3], patch_size):
        if fourPointsInPoly(i, j, pointInPolytag):
           img  = open.read_region((i,j), 0 , (patch_size, patch_size))
           img.save(dir_folder + str(imgIndex) + ".png")
           imgIndex += 1

def scanAnnotations():
  annlist = Read_xml.read_xml("patient_004_node_4.xml")
  for  ann in annlist:
      polyPointGroup = getPolyPoints(ann)
      pointInPolytag = tagInPoly(ann, polyPointGroup)
      saveInsideRegions()
