"""
This program is used to store patches which have all their 4 angles' coordinates are in the annotation polygon
"""
import sys
sys.path.append("../Read_xml.py")
sys.path.append("../PointInPoly")
sys.path.append("../ShowAnnPart")
import Read_xml
from PointInPoly import point, isInPoly, pointLieRight
from ShowAnnPart import addPolygonGraph, addPatchGraph, showAnnGraph
import openslide
from openslide import open_slide # http://openslide.org/api/python/
from PIL import Image
import os

dirImg = r'C:\Users\nctu\Desktop\svs_scanner\svs_image'
dirFolder = r'C:\Users\nctu\Desktop\ScanAnnotation\inpoly'
valid_images = ['.tif']
patchSize = 10

def scanAnnotations():
  annlist = Read_xml.read_xml("patient_004_node_4.xml")
  scan = openScan()
  for  ann in annlist:
      polyPointGroup = getPolyPoints(ann)
      pointTag = tagPointInPoly(ann, polyPointGroup)
      savePatchInsideRegions(ann, pointTag, scan)

def openScan():
  for f in os.listdir(dirImg):
     ext = os.path.splitext(f)[1]
     if ext.lower() not in valid_images:
       continue
     currPath = os.path.join(dirImg,f)
     print(currPath)
     scan = openslide.OpenSlide(currPath)
  return scan

#get the points of annotation polygon
def getPolyPoints(ann):
   polyXGroup = dealWithPolyGroup(ann.coordinateX)
   polyYGroup = dealWithPolyGroup(ann.coordinateY)
   polyPointGroup = groupXY(polyXGroup, polyYGroup)
   return polyPointGroup

def dealWithPolyGroup(polyGroup):
  polyGroup = [float(number) for number in polyGroup]
  # It is a polygon so we add the first point to the end to make a closed graph
  polyGroup.append(polyGroup[0])
  return polyGroup
 
def groupXY(polyXGroup, polyYGroup):
  polyPointGroup = []
  for i in range(0, len(polyXGroup)):
      polyPointGroup.append(point(polyXGroup[i], polyYGroup[i]))
  return polyPointGroup

# Find out if each point is in the polygon, and use a tag True if it is, tag False if it is not
def tagPointInPoly(ann, polyPointGroup):
  pointTag = {}
  for i in range(ann.border[0], ann.border[1], patchSize):
    for j in range(ann.border[2], ann.border[3], patchSize):
      if isInPoly(point(i, j), polyPointGroup):
        pointTag.update({(i, j) : True})
      else:
        pointTag.update({(i, j) : False})
  return pointTag

def savePatchInsideRegions(ann, pointTag, scan):
  imgIndex = 0
  annImg = addPolygonGraph(ann.coordinateX, ann.coordinateY)
  for i in range(ann.border[0], ann.border[1], patchSize):
    for j in range(ann.border[2], ann.border[3], patchSize):
      if isFourAnglesInPoly(i, j, pointTag):
        addPatchGraph(annImg, i, j, patchSize)
        savePatchFromSlide(i, j, imgIndex, scan)
        imgIndex += 1
  showAnnGraph(annImg)

def isFourAnglesInPoly(i, j, pointTag):
  inPoly = False
  if pointTag.get((i, j)) and pointTag.get((i + patchSize, j)) and pointTag.get((i , j + patchSize)) and pointTag.get((i + patchSize, j + patchSize)):
     inPoly = True
  return inPoly

def savePatchFromSlide(i, j, imgIndex, scan):
  img  = scan.read_region((i,j), 0 , (patchSize, patchSize))
  img.save(str(dirFolder)+ '\\' + str(imgIndex) + ".png")

scanAnnotations()
