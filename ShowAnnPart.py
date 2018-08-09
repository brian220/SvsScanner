"""
Draw the graph that include the annotation part and patches part
"""
import matplotlib.pyplot as plt
#class showAnnPart(object):

def addPolygonGraph(polyXGroup, polyYGroup):
  polygonPoints = []
  for i in range(0, len(polyXGroup)):
     polygonPoints.append((polyXGroup[i], polyYGroup[i]))
  polygon = plt.Polygon(polygonPoints, fill=None, edgecolor='r')
  annImg = plt.subplot(111)
  annImg.add_patch(polygon)
  return annImg

def addPatchGraph(annImg, i, j, patch_size):
  print (i, j)
  patchPoints = [(i,j), (i + patch_size, j), (i + patch_size, j + patch_size), (i, j + patch_size)]
  patch = plt.Polygon(patchPoints, fill=None, edgecolor='b')
  annImg.add_patch(patch)

def showAnnGraph (annImg):
  annImg.plot()
  plt.show()
