
dirFolder = r'C:\Users\nctu\Desktop\ScanAnnotation\inAnn'

class SavePatchInAnn(object):
  def __init__(self, scan, currentAnn, currentSaveIndex):
    self.scan = scan
    self.ann = currentAnn
    self.saveIndex = currentSaveIndex

  def savePatch(self):
    for i in range(self.ann.xMin, self.ann.xMax, self.ann.patchSize):
      for j in range(self.ann.yMin, self.ann.yMax, self.ann.patchSize):
        if self.ann.patchInAnn.get((i, j)):
          self.savePatchFromSlide(i, j)

  def savePatchFromSlide(self, i, j):
    img  = self.scan.read_region((i,j), 0 , (self.ann.patchSize, self.ann.patchSize))
    img.save(str(dirFolder)+ '\\' + str(self.saveIndex) + ".png")
    self.saveIndex += 1

  def updateSaveIndex(self):
      return self.saveIndex
