"""
This program is used to store patches which have all their 4 angles' coordinates are in the annotation Anngon
"""
import sys
sys.path.append("../IsPointInAnn")
from IsPointInAnn import point, isPointInAnn
import openslide
from openslide import open_slide # http://openslide.org/api/python/
from PIL import Image

class GetPatchInAnn(object):
  def __init__(self, currentAnn) :
    self.ann = currentAnn
    self.annPointGroup = []
    self.pointInAnn = {}

  def getPatch(self):
    self.groupXY()
    self.checkPointsInAnn()
    self.checkPatchInAnn()

  def groupXY(self):
    for i in range(0, len(self.ann.coordinateX)):
        self.annPointGroup.append(point(float(self.ann.coordinateX[i]), float(self.ann.coordinateY[i])))
    self.annPointGroup.append(self.annPointGroup[0])

  # Find out if each point is in the Annotation, and tag True if it is, tag False if it is not
  def checkPointsInAnn(self):
    for i in range(self.ann.xMin, self.ann.xMax, self.ann.patchSize):
      for j in range(self.ann.yMin, self.ann.yMax, self.ann.patchSize):
        if isPointInAnn().isInAnn(point(i, j), self.annPointGroup):
          self.pointInAnn.update({(i, j) : True})
        else:
          self.pointInAnn.update({(i, j) : False})

  #Find out if a patch is in annotation, and tag True if it is, tag False if it is not
  def checkPatchInAnn(self):
    for i in range(self.ann.xMin, self.ann.xMax, self.ann.patchSize):
      for j in range(self.ann.yMin, self.ann.yMax, self.ann.patchSize):
        if self.isFourAnglesInAnn(i, j):
          self.ann.patchInAnn.update({(i, j) : True})
        else:
          self.ann.patchInAnn.update({(i, j) : False})

  def isFourAnglesInAnn(self, i, j):
    inAnn = False
    if self.pointInAnn.get((i, j))\
       and self.pointInAnn.get((i + self.ann.patchSize, j))\
       and self.pointInAnn.get((i , j + self.ann.patchSize))\
       and self.pointInAnn.get((i + self.ann.patchSize, j + self.ann.patchSize)):
       inAnn = True
    return inAnn
