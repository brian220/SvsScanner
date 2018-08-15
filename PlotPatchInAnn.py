"""
Draw the graph that include the annotation part and patches part
"""
import matplotlib.pyplot as plt

class PlotPatchInAnn(object):
  def __init__(self, currentAnn):
    self.annImg = plt.subplot(111)
    self.ann = currentAnn

  def plotPatch(self):
    self.addAnnGraph()
    for i in range(self.ann.xMin, self.ann.xMax, self.ann.patchSize):
      for j in range(self.ann.yMin, self.ann.yMax, self.ann.patchSize):
        if self.ann.patchInAnn.get((i, j)):
          self.addPatchGraph(i, j)
    self.showAnnGraph()

  def addAnnGraph(self):
    AnnPoints = []
    for i in range(0, len(self.ann.coordinateX)):
       AnnPoints.append((self.ann.coordinateX[i], self.ann.coordinateY[i]))
    AnnGraph = plt.Polygon(AnnPoints, fill = None, edgecolor = 'r')
    self.annImg.add_patch(AnnGraph)

  def addPatchGraph(self, i, j):
    print (i, j)
    patchPoints = [(i,j), (i + self.ann.patchSize, j), (i + self.ann.patchSize, j + self.ann.patchSize), (i, j + self.ann.patchSize)]
    patch = plt.Polygon(patchPoints, fill = None, edgecolor = 'b')
    self.annImg.add_patch(patch)

  def showAnnGraph (self):
    self.annImg.plot()
    plt.show()
