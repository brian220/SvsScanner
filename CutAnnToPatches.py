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
  def __init__(self, scan, currentAnn) :
    self.scan = scan
    self.ann = currentAnn
    self.annPointGroup = []
    self.imgIndex = 0
    self.pointTag = {}
    self.patchSize = 10

  def cutAnn(self):
    self.groupXY()
    self.pointTag = self.checkPointsInAnn()
    self.savePatchInAnn()

  def groupXY(self):
    for i in range(0, len(self.ann.coordinateX)):
        self.annPointGroup.append(point(float(self.ann.coordinateX[i]), float(self.ann.coordinateY[i])))
    self.annPointGroup.append(self.annPointGroup[0])

  # Find out if each point is in the Anngon, and use a tag True if it is, tag False if it is not
  def checkPointsInAnn(self):
    for i in range(self.ann.xMin, self.ann.xMax, self.patchSize):
      for j in range(self.ann.yMin, self.ann.yMax, self.patchSize):
        if isPointInAnn().isInAnn(point(i, j), self.annPointGroup):
          self.pointTag.update({(i, j) : True})
        else:
          self.pointTag.update({(i, j) : False})
    return self.pointTag

  def savePatchInAnn(self):
    showAnn().addAnnGraph(self.ann.coordinateX, self.ann.coordinateY)
    for i in range(self.ann.xMin, self.ann.xMax, self.patchSize):
      for j in range(self.ann.yMin, self.ann.yMax, self.patchSize):
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
