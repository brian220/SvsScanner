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

def isInAnn(testPoint, AnnPointGroup):
  inAnn = False
  for i in range(0, len(AnnPointGroup) - 1):
      if (pointLieRight(testPoint, AnnPointGroup[i], AnnPointGroup[i+1])):
        inAnn = not inAnn
  return inAnn

def pointLieRight(testPoint, AnnPoint1, AnnPoint2):
  lieRight = False
  if min(AnnPoint1.y, AnnPoint2.y) < testPoint.y <= max(AnnPoint1.y, AnnPoint2.y)\
     and ( testPoint.x >= AnnPoint1.x or testPoint.x >= AnnPoint2.x):

    if (AnnPoint2.x - AnnPoint1.x) == 0:
        lieRight = True
    else:
      a = (AnnPoint2.y - AnnPoint1.y) / (AnnPoint2.x - AnnPoint1.x)
      b = AnnPoint1.y - a * AnnPoint1.x
      if  testPoint.x > ( testPoint.y - b) / a:
        lieRight = True
  return lieRight
