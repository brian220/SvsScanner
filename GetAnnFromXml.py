"""
This program is used for read an annotation xml File and store in class Annotation
"""
import sys
sys.path.append("../Annotation")
from Annotation import Annotation
import xml.etree.cElementTree as ET
import os.path
import math

class GetAnnFromXml(object):
  def __init__(self, fileName):
      self.tree = ET.ElementTree(file = fileName)
      self.annList = []
      self.annIndex = 0
      pass

  def readXml(self):
    for elem in self.tree.iter("Annotation"):
       if(elem.get("Type") != "None"):
         curAnn = Annotation()
         self.updateAnnInformation(elem, curAnn)
         self.getAnnCoordinate(elem, curAnn)
         self.computeBorder(curAnn)
         self.storeAnn(curAnn)
    return self.annList

  def updateAnnInformation(self, elem, curAnn):
    curAnn.name = elem.get("Name")
    curAnn.type = elem.get("Type")
    curAnn.index = self.annIndex
    curAnn.partOfGroup = elem.get("PartOfGroup")
    self.annIndex += 1

  def getAnnCoordinate(self, elem, curAnn):
    for coor_elem in elem.iter("Coordinate"):
      X = coor_elem.get("X")
      Y = coor_elem.get("Y")
      curAnn.coordinateX.append(int(float(X)))
      curAnn.coordinateY.append(int(float(Y)))

  def computeBorder(self, curAnn):
      curAnn.xMin = min(curAnn.coordinateX)
      curAnn.xMax = max(curAnn.coordinateX)
      curAnn.yMin = min(curAnn.coordinateY)
      curAnn.yMax = max(curAnn.coordinateY)

  def storeAnn(self, curAnn):
      self.annList.append(curAnn)
