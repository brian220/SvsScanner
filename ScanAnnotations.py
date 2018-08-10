import sys
sys.path.append("../CutAnnToPatches")
sys.path.append("../GetAnnFromXml")
from CutAnnToPatches import cutAnnToPatches
from GetAnnFromXml import getAnnFromXml
import openslide
from openslide import open_slide # http://openslide.org/api/python/

sysFilePath = r'C:\Users\nctu\Desktop\svs_scanner\svs_image\patient_004_node_4.tif'
xmlFilePath = "patient_004_node_4.xml"

class scanAnnotations(object):
  def __init__(self, sysFilePath, xmlFilePath):
      getAnn = getAnnFromXml(xmlFilePath)
      self.annList = getAnn.readXml()
      self.scan = openslide.OpenSlide(sysFilePath)

  def scanAnnotations(self):
    for  currentAnn in self.annList:
        ann = cutAnnToPatches( self.scan, currentAnn)
        ann.cutAnn()

test = scanAnnotations(sysFilePath, xmlFilePath)
test.scanAnnotations()
