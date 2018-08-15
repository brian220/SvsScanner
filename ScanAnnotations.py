import sys
sys.path.append("../GetAnnFromXml")
sys.path.append("../GetPatchInAnn")
sys.path.append("../SavePatchInAnn")
sys.path.append("../PlotPatchInAnn")
from GetAnnFromXml import GetAnnFromXml
from GetPatchInAnn import GetPatchInAnn
from SavePatchInAnn import SavePatchInAnn
from PlotPatchInAnn import PlotPatchInAnn
import openslide
from openslide import open_slide # http://openslide.org/api/python/

sysFilePath = r'C:\Users\nctu\Desktop\svs_scanner\svs_image\patient_004_node_4.tif'
xmlFilePath = "patient_004_node_4.xml"

class ScanAnnotations(object):
  def __init__(self, sysFilePath, xmlFilePath):
      getAnn = GetAnnFromXml(xmlFilePath)
      self.annList = getAnn.readXml()
      self.scan = openslide.OpenSlide(sysFilePath)
      self.currentSaveIndex = 0

  def scanAnnotations(self):
    for  currentAnn in self.annList:
      self.getPatchInAnnotation(currentAnn)
      self.savePatchInAnnotation(self.scan, currentAnn, self.currentSaveIndex)
      self.plotPatchInAnnotation(currentAnn)

  def getPatchInAnnotation(self, ann):
    annGet = GetPatchInAnn(ann)
    annGet.getPatch()

  def savePatchInAnnotation(self, scan, ann, saveIndex):
    annSave = SavePatchInAnn(scan, ann, saveIndex)
    annSave.savePatch()
    self.currentSaveIndex = annSave.updateSaveIndex()

  def plotPatchInAnnotation(self, ann):
    annShow = PlotPatchInAnn(ann)
    annShow.plotPatch()

test = ScanAnnotations(sysFilePath, xmlFilePath)
test.scanAnnotations()
