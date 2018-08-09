"""
This program is used to find out if a point is in the irregular polygon or not
and then we can find out if a patch is in the annotation part
method:
Point-In-Polygon Algorithm — Determining Whether A Point Is Inside A Complex Polygon
source: http://alienryderflex.com/polygon/
"""

import sys
sys.path.append("../Read_xml.py")
sys.path.append("../PointInPoly")
sys.path.append("../ShowAnnPart")
import Read_xml
from PointInPoly import point, pointInPoly, pointLieRight
from ShowAnnPart import addPolygonGraph, addPatchGraph, showAnnGraph
import openslide
from openslide import open_slide # http://openslide.org/api/python/
import numpy as np
from PIL import Image
import math
import os

dir_img = r'C:\Users\nctu\Desktop\svs_scanner\svs_image'
dir_folder = r'C:\Users\nctu\Desktop\ScanAnnotation\inpoly'
valid_images = ['.tif']
patch_size = 10

def fourPointsInPoly(i, j, pointInPolytag):
  inPoly = False
  if pointInPolytag.get((i, j)) and pointInPolytag.get((i + patch_size, j)) and pointInPolytag.get((i , j + patch_size)) and pointInPolytag.get((i + patch_size, j + patch_size)):
     inPoly = True
  return inPoly

# save the region that is all in the polygon
def saveInsideRegions(ann, pointInPolytag, scan):
  imgIndex = 0
  if ann.index == 0:
    annImg = addPolygonGraph(ann.coordinateX, ann.coordinateY)
  for i in range(ann.border[0], ann.border[1], patch_size):
    for j in range(ann.border[2], ann.border[3], patch_size):
      if fourPointsInPoly(i, j, pointInPolytag):
        if ann.index == 0:
          addPatchGraph(annImg, i, j, patch_size)
        img  = scan.read_region((i,j), 0 , (patch_size, patch_size))
        img.save(str(dir_folder)+ '\\' + str(imgIndex) + ".png")
        imgIndex += 1
  if ann.index == 0:
    showAnnGraph(annImg)

# find out if each point is in the polygon, and use a tag to record in the dictionary
def tagInPoly(ann, polyPointGroup):
  pointInPolytag = {}
  for i in range(ann.border[0], ann.border[1], patch_size):
    for j in range(ann.border[2], ann.border[3], patch_size):
      if pointInPoly(point(i, j), polyPointGroup):
        pointInPolytag.update({(i, j) : True})
      else:
        pointInPolytag.update({(i, j) : False})
  return pointInPolytag

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
   return polyPointGroup

def openScan():
  for f in os.listdir(dir_img):
     ext = os.path.splitext(f)[1]
     if ext.lower() not in valid_images:
       continue
     curr_path = os.path.join(dir_img,f)
     print(curr_path)
     # open scan
     scan = openslide.OpenSlide(curr_path)
  return scan

def scanAnnotations():
  annlist = Read_xml.read_xml("patient_004_node_4.xml")
  scan = openScan()
  for  ann in annlist:
      polyPointGroup = getPolyPoints(ann)
      pointInPolytag = tagInPoly(ann, polyPointGroup)
      saveInsideRegions(ann, pointInPolytag, scan)

scanAnnotations()
