"""
Draw the graph that include the annotation part and patches part
"""
import matplotlib.pyplot as plt

def addAnnGraph(AnnXGroup, AnnYGroup):
  AnnPoints = []
  for i in range(0, len(AnnXGroup)):
     AnnPoints.append((AnnXGroup[i], AnnYGroup[i]))
  AnnGraph = plt.Polygon(AnnPoints, fill=None, edgecolor='r')
  annImg = plt.subplot(111)
  annImg.add_patch(AnnGraph)
  return annImg

def addPatchGraph(annImg, i, j, patch_size):
  print (i, j)
  patchPoints = [(i,j), (i + patch_size, j), (i + patch_size, j + patch_size), (i, j + patch_size)]
  patch = plt.Polygon(patchPoints, fill=None, edgecolor='b')
  annImg.add_patch(patch)

def showAnnGraph (annImg):
  annImg.plot()
  plt.show()
