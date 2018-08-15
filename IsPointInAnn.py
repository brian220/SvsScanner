"""
This program is used to find out if a point is in the irregular Anngon or not
method:
Point-In-Anngon Algorithm — Determining Whether A Point Is Inside A Complex Anngon
source: http://alienryderflex.com/Anngon/
"""
class point (object):
  def __init__(self, x, y):
    self.x = x
    self.y = y

class isPointInAnn(object):
  def __init__(self):
      pass

  def isInAnn(self, testPoint, annPointGroup):
    inAnn = False
    for i in range(0, len(annPointGroup) - 1):
        # If there are odd number of lines line in the left of the points,
        # then the point is in in the annotation
        if (self.pointLieRight(testPoint, annPointGroup[i], annPointGroup[i+1])):
          inAnn = not inAnn
    return inAnn

  # Check if the point is lying right of the line(annPoint1 - annPoint2)
  def pointLieRight(self, testPoint, annPoint1, annPoint2):
    lieRight = False
    if min(annPoint1.y, annPoint2.y) < testPoint.y <= max(annPoint1.y, annPoint2.y)\
       and ( testPoint.x >= annPoint1.x or testPoint.x >= annPoint2.x):

      if (annPoint2.x - annPoint1.x) == 0:
          lieRight = True
      else:
        a = (annPoint2.y - annPoint1.y) / (annPoint2.x - annPoint1.x)
        b = annPoint1.y - a * annPoint1.x
        if  testPoint.x > ( testPoint.y - b) / a:
          lieRight = True
    return lieRight
