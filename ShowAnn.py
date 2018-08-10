"""
Draw the graph that include the annotation part and patches part
"""
import matplotlib.pyplot as plt

class showAnn(object):
  def __init__(self):
      self.annImg = plt.subplot(111)

  def addAnnGraph(self, AnnXGroup, AnnYGroup):
    AnnPoints = []
    for i in range(0, len(AnnXGroup)):
       AnnPoints.append((AnnXGroup[i], AnnYGroup[i]))
    AnnGraph = plt.Polygon(AnnPoints, fill=None, edgecolor='r')
    self.annImg.add_patch(AnnGraph)

  def addPatchGraph(self, i, j, patch_size):
    print (i, j)
    patchPoints = [(i,j), (i + patch_size, j), (i + patch_size, j + patch_size), (i, j + patch_size)]
    patch = plt.Polygon(patchPoints, fill=None, edgecolor='b')
    self.annImg.add_patch(patch)

  def showAnnGraph (self):
    self.annImg.plot()
    plt.show()
