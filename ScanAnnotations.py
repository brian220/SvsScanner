import sys
sys.path.append("../CutAnnToPatches")
sys.path.append("../Read_xml")
from CutAnnToPatches import cutAnnToPatches
from Read_xml import read_xml
import openslide
from openslide import open_slide # http://openslide.org/api/python/

sysFilePath = r'C:\Users\nctu\Desktop\svs_scanner\svs_image\patient_004_node_4.tif'
xmlFilePath = "patient_004_node_4.xml"

class scanAnnotations(object):
  def __init__(self, sysFilePath, xmlFilePath):
      self.annlist = read_xml(xmlFilePath)
      self.scan = openslide.OpenSlide(sysFilePath)

  def scanAnnotations(self):
    for  currentAnn in self.annlist:
        ann = cutAnnToPatches(currentAnn, self.scan)
        ann.cutAnn()

test = scanAnnotations(sysFilePath, xmlFilePath)
test.scanAnnotations()
