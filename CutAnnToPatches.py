"""
This program is used to store patches which have all their 4 angles' coordinates are in the annotation Anngon
"""
import sys
sys.path.append("../IsPointInAnn")
sys.path.append("../ShowAnn")
from IsPointInAnn import point, isPointInAnn
from ShowAnn import showAnn
import openslide
from openslide import open_slide # http://openslide.org/api/python/
from PIL import Image
dirFolder = r'C:\Users\nctu\Desktop\ScanAnnotation\inAnn'

class cutAnnToPatches(object):
  def __init__(self, currentAnn, scan):
    self.scan = scan
    self.ann = currentAnn
    self.imgIndex = 0
    self.AnnXGroup = []
    self.AnnYGroup = []
    self.AnnPointGroup = []
    self.pointTag = {}
    self.patchSize = 10

  def cutAnn(self):
    AnnPointGroup = self.getAnnPoints()
    self.pointTag = self.checkPointsInAnn()
    self.savePatchInAnn()

  #get the points of annotation polygon
  def getAnnPoints(self):
     self.AnnXGroup = self.dealWithAnnGroup(self.ann.coordinateX)
     self.AnnYGroup = self.dealWithAnnGroup(self.ann.coordinateY)
     self.AnnPointGroup = self.groupXY()
     return self.AnnPointGroup

  def dealWithAnnGroup(self, AnnGroup):
    AnnGroup = [float(number) for number in AnnGroup]
    # It is a Ann polygon so we add the first point to the end to make a closed graph
    AnnGroup.append(AnnGroup[0])
    return AnnGroup

  def groupXY(self):
    for i in range(0, len(self.AnnXGroup)):
        self.AnnPointGroup.append(point(self.AnnXGroup[i], self.AnnYGroup[i]))
    return self.AnnPointGroup

  # Find out if each point is in the Anngon, and use a tag True if it is, tag False if it is not
  def checkPointsInAnn(self):
    for i in range(self.ann.border[0], self.ann.border[1], self.patchSize):
      for j in range(self.ann.border[2], self.ann.border[3], self.patchSize):
        if isPointInAnn().isInAnn(point(i, j), self.AnnPointGroup):
          self.pointTag.update({(i, j) : True})
        else:
          self.pointTag.update({(i, j) : False})
    return self.pointTag

  def savePatchInAnn(self):
    showAnn().addAnnGraph(self.ann.coordinateX, self.ann.coordinateY)
    for i in range(self.ann.border[0], self.ann.border[1], self.patchSize):
      for j in range(self.ann.border[2], self.ann.border[3], self.patchSize):
        if self.isFourAnglesInAnn(i, j):
          showAnn().addPatchGraph(i, j, self.patchSize)
          self.savePatchFromSlide(i, j)
          self.imgIndex += 1
    showAnn().showAnnGraph()

  def isFourAnglesInAnn(self, i, j):
    inAnn = False
    if self.pointTag.get((i, j))\
       and self.pointTag.get((i + self.patchSize, j))\
       and self.pointTag.get((i , j + self.patchSize))\
       and self.pointTag.get((i + self.patchSize, j + self.patchSize)):
       inAnn = True
    return inAnn

  def savePatchFromSlide(self, i, j):
    img  = self.scan.read_region((i,j), 0 , (self.patchSize, self.patchSize))
    img.save(str(dirFolder)+ '\\' + str(self.imgIndex) + ".png")
