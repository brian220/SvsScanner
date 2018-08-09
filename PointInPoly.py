"""
This program is used to find out if a point is in the irregular polygon or not
method:
Point-In-Polygon Algorithm — Determining Whether A Point Is Inside A Complex Polygon
source: http://alienryderflex.com/polygon/
"""
dir_folder = r'C:\Users\nctu\Desktop\ScanAnnotation\inpoly'
patch_size = 50

class point (object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

def isInPoly(testPoint, polyPointGroup):
  inPoly = False
  for i in range(0, len(polyPointGroup) - 1):
      if (pointLieRight(testPoint, polyPointGroup[i], polyPointGroup[i+1])):
        inPoly = not inPoly
  return inPoly
  
def pointLieRight(testPoint, polyPoint1, polyPoint2):
  lieRight = False
  if testPoint.y > min(polyPoint1.y, polyPoint2.y) and  testPoint.y <= max(polyPoint1.y, polyPoint2.y) and ( testPoint.x >= polyPoint1.x or testPoint.x >= polyPoint2.x):
    if (polyPoint2.x - polyPoint1.x) == 0:
        lieRight = True
    else:
      a = (polyPoint2.y - polyPoint1.y) / (polyPoint2.x - polyPoint1.x)
      b = polyPoint1.y - a * polyPoint1.x
      if  testPoint.x > ( testPoint.y - b) / a:
        lieRight = True
  return lieRight
